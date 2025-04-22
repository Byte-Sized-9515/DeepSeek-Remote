import threading
import time
import logging
from flask import Flask, request, jsonify, render_template
import ollama

app = Flask(__name__)

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Global variables to track the current process
current_process_thread = None
abort_flag = False

@app.route('/')
def index():
    return render_template('chat-mobile.html')

# Define the method to run the LLM inference
def run_inference(prompt, mode, result_holder, process_id):
    global abort_flag
    try:
        # Track the current process
        global current_process_thread
        current_process_thread = threading.current_thread()  # Track the thread

        logging.debug("Running inference for prompt: %s", prompt)

        # If the abort flag is set, cancel the task
        if abort_flag:
            result_holder['response'] = "Process was aborted by the user."
            return

        response = ollama.chat(
            model='deepseek-r1:14b',
            messages=[{
                "role": "user",
                "content": f"{mode} mode: {prompt}"
            }]
        )
        result_holder['response'] = response['message']['content']
        logging.debug("Inference response: %s", result_holder['response'])
    except Exception as e:
        logging.error("Error during inference: %s", str(e))
        result_holder['error'] = str(e)
    finally:
        current_process_thread = None  # Reset after processing is complete
        abort_flag = False  # Reset abort flag

# Handle the POST request to process the chat
@app.route('/process', methods=['POST'])
def process():
    data = request.json
    prompt = data['prompt']
    mode = data.get('mode', 'chat')

    result_holder = {}
    process_id = str(time.time())  # Unique process ID (e.g., timestamp)
    
    logging.debug("Starting processing for prompt: %s", prompt)
    
    # Create a new thread to run the LLM task
    t = threading.Thread(target=run_inference, args=(prompt, mode, result_holder, process_id))
    t.start()
    
    # Set a longer timeout (e.g., 30 seconds instead of 15)
    t.join(timeout=30)  # Timeout after 30 seconds

    # If the process is still running after the timeout
    if t.is_alive():
        logging.warning("Processing timeout reached for prompt: %s", prompt)
        return jsonify({"response": "Server took too long to respond."}), 504
    if 'error' in result_holder:
        logging.error("Error result during processing: %s", result_holder['error'])
        return jsonify({"response": f"Error: {result_holder['error']}"}), 500
    logging.debug("Processing finished successfully.")
    return jsonify({"response": result_holder['response']})

# Handle server-side refresh (abort request when needed)
@app.route('/refresh', methods=['POST'])
def refresh():
    global abort_flag
    global current_process_thread

    if current_process_thread is not None:
        # Trigger the abort flag to stop the ongoing process
        abort_flag = True
        logging.debug("Aborting the ongoing process.")
        return jsonify({"response": "Server-side task aborted."}), 200
    else:
        logging.debug("No process to abort.")
        return jsonify({"response": "No process to abort."}), 200

if __name__ == '__main__':
    app.run(port=1194)