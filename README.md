<h1>Dependencies</h1>

- [Cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/)

- [Ollama](https://ollama.com/download) and an LLM of your choosing
 
- Python 3.10+
 
- Flask

<h1>Setup Process</h1>
I am useing DeepSeek-R1:14b in server.py. Change this to the actual LLM you want to access remotely. To see your installed LLMs in Ollama run `ollama list`.

 - Start a cloudflared tunnel to any port >1024. I will be using 1194
   - `cloudflared tunnel --url localhost:1194`
   - Save the generated URL

       +--------------------------------------------------------------------------------------------+

       |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |

       |  https://afghanistan-apparently-editor-concerned.trycloudflare.com                         |

       +--------------------------------------------------------------------------------------------+
       
 - Start `server.py`

 - Open your URL from ANYWHERE without exposing your IP!!!

This URL will be available for a long as the cloudflared tunnel is running. If you stop the tunnel and start another one, a new URL will be generated. For the best anytime anywhere remote experience consider using a capable PC that can be left on 24/7.

<h2>PLEASE BE AWARE OF CLOUDFLARES <a href="https://www.cloudflare.com/website-terms/#:~:text=You%20may%20not%20use%20the,any%20Websites%20or%20Online%20Services">TERMS AND CONDITIONS</a> BEFORE INSTALLING THIS PROJECT</h2>
