from flask import Flask, request, jsonify, render_template
import ollama

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(chat.html)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    prompt = data['prompt']
    mode = data.get('mode', 'chat')

    try:
        response = ollama.chat(
            model='deepseek-r1:14b',  # or any model you've pulled
            messages=[{
                "role": "user",
                "content": f"{mode} mode: {prompt}"
            }]
        )
        return jsonify({"response": response['message']['content']})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=1194)