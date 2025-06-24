from diffusers import StableDiffusionPipeline
import torch
import gradio as gr
import os
# Optional: Check if CUDA is available
print("Using GPU:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Device name:", torch.cuda.get_device_name(0))
else:
    print("Running on CPU! May be very slow.")

# Hugging Face token (yours)
HUGGINGFACE_TOKEN = os.getenv("HF_TOKEN")

# Load the Stable Diffusion v1.4 pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16,  # Use float16 for GPU speed
    use_auth_token=HUGGINGFACE_TOKEN
)

# Move the pipeline to GPU (or fallback to CPU)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

# Function to generate image
def generate_image(prompt):
    print(f"Generating image for: {prompt}")
    image = pipe(prompt, num_inference_steps=20).images[0]  # Faster generation
    return image

# Gradio Web Interface
gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(lines=2, placeholder="e.g., A cyberpunk city at night with glowing lights"),
    outputs="image",
    title="🖼️ AI Image Generator (GPU Powered)",
    description="Enter a creative prompt to generate an image using Stable Diffusion v1.4"
).launch()
