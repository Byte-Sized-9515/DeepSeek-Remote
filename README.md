<h1>How to Install</h1>

- Install [miniconda3](https://www.anaconda.com/docs/getting-started/miniconda/install). (see documentation for installation instructions)

- Install [Cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/). (step may vary, see documentation).

- Clone the repo: `git clone https://github.com/Byte-Sized-9515/DeepSeek-Remote.git`

- Go into your local repo and create a conda environment: `conda create -n <Env_Name> python=3.12.3`

- Install Ollama and Flask: `pip install ollama flask`

<h1>Starting Your AI Server</h1>

- Run `./start.sh`

- Open the Cloudflare URL from <b>ANYWHERE</b>

    - Example URL output `Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):
       https://gary-domain-solving-trademark.trycloudflare.com`