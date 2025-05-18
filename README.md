<h1>How To Install</h1>

The install process for these dpenedencies may vary depending on your OS and other factors. Please see the linked documentation to correctly install dependencies.

- Install [Cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/)

- Install [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)

- Clone the repo `git clone https://github.com/Byte-Sized-9515/DeepSeek-Remote.git`

- Open your local repo directory and create a conda environment: `conda create -n <condaEnv> python=3.12.3 -y`

- Activate your conda env: `conda activate <condaEnv>`

- Install conda dependencies: `conda install -c conda-forge fastapi uvicorn jinja2 -y`

- Install python dependencies: `pip install ollama python-multipart`

- In `main.py` change the model on line 43 to the model you want to use:

```response = ollama.chat(
    model='<your-ollama-model>',
    messages=[{
        "role": "user",
        "content": f"{mode} mode: {prompt}"
    }]
```

<h1>Starting The AI Server</h1>

- Open your repo directory and run `./start.sh`

<h1>Hardware Specs</h1>

I am running the DeepSeek-r1:14b model on the below hardware. It's not fast, but it's not unsuably slow:

- CPU: 13th Gen Intel i7-13700KF

- GPU: GeForce RTX 4070

- RAM: 16GB DDR5 x2

<h3>PLEASE BE AWARE OF CLOUDFLARES <a href="https://www.cloudflare.com/website-terms/#:~:text=You%20may%20not%20use%20the,any%20Websites%20or%20Online%20Services">TERMS AND CONDITIONS</a> BEFORE CLONING THIS PROJECT</h3>
