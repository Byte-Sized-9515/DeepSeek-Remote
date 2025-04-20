<h1>Dependencies</h1>

- [Cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/)

- [Ollama](https://ollama.com/download) and an LLM of your choosing
 
- Python 3.10+
 
- Flask

<h1>Setup Process</h1>
I am useing DeepSeek-R1:14b in server.py. Change this to the actual LLM you want to access remotely. To see your installed LLMs in Ollama run `ollama list`.

 - Navigate to the project and run ./start.sh

 -  +--------------------------------------------------------------------------------------------+
    |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
    |  https://afghanistan-apparently-editor-concerned.trycloudflare.com                         |
    +--------------------------------------------------------------------------------------------+

 - Open your URL from ANYWHERE without exposing your IP!!!

I am running a private Cloudflare tunnel. Private tunnels are assigned random URLs at start.

<h2>PLEASE BE AWARE OF CLOUDFLARES <a href="https://www.cloudflare.com/website-terms/#:~:text=You%20may%20not%20use%20the,any%20Websites%20or%20Online%20Services">TERMS AND CONDITIONS</a> BEFORE CLONING THIS PROJECT</h2>
