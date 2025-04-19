<h1>Dependencies</h1>

- [Cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/)

- [Ollama](https://ollama.com/download) and an LLM of your choosing
 
- Python 3.10+
 
- Flask

<h1>Setup Process</h1>

 - Start a cloudflared tunnel to any port >1024. I will be using 1194
   - `cloudflared tunnel --url localhost:1198`
     - Save the generated URL

       +--------------------------------------------------------------------------------------------+

       |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |

       |  https://afghanistan-apparently-editor-concerned.trycloudflare.com                         |

       +--------------------------------------------------------------------------------------------+
       
 - start server.py

 - Open your URL from ANYWHERE without exposing your IP!!!
