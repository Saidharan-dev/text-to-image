# 🎨 AI Text-to-Image Generator using Stable Diffusion

Generate stunning images from creative text prompts using Stable Diffusion, Hugging Face, and Gradio — powered by your own GPU (like RTX 3060 Ti).


> *Example prompt:* `A futuristic city at night 

---

## 🚀 Features

- 💬 Accepts text prompts and returns unique images
- ⚡ Runs locally on **GPU** (with `torch.float16` for speed)
- 🌐 Clean web UI using **Gradio**
- 🧠 Based on `CompVis/stable-diffusion-v1-4` (Hugging Face)
- ⚙️ Optimized with reduced inference steps for fast generation

## 📁 Project Structure
text-to-image/
├── main.py # Main Python app with Gradio UI
├── requirements.txt # Python dependencies
└── README.md # Project overview 
## 🛠️ Setup Instructions
### ✅ 1. Clone the Repository
git clone https://github.com/your-username/text-to-image.git
cd text-to-image
2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate       # On Windows
# source venv/bin/activate  # On Mac/Linux
3. Install Dependencies
pip install -r requirements.txt
4. Add Your Hugging Face Token
Create a free account: https://huggingface.co
Get your access token: https://huggingface.co/settings/tokens
Replace "your_token_here" in main.py with your token.
Run the App
python main.py
You’ll see output like:
Using GPU: True
Device name: NVIDIA GeForce RTX 3060 Ti
Running on local URL: http://127.0.0.1:7860
Then open your browser and enter prompts like:
A cyberpunk owl with neon feathers sitting on a skyscraper
🧪 Example Prompts
A cat wearing sunglasses surfing a giant wave
A glowing castle floating in the night sky with stars
A robot reading a book in a cozy library
A frog wizard casting spells in a magical swamp
📦 Requirements
Python 3.10 (not 3.13+)
An NVIDIA GPU with CUDA support (e.g., RTX 3060 Ti)
Hugging Face Token
📜 requirements.txt
txt
Copy
Edit
torch==2.5.1+cu121
torchvision==0.20.1+cu121
torchaudio==2.5.1+cu121
diffusers
transformers
accelerate
gradio
🙏 Acknowledgements
🤗 Hugging Face
🧠 Diffusers Library
🖼️ Gradio
🧰 PyTorch