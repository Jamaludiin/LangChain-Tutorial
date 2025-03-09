# pip install diffusers transformers torch


from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")
pipe.to("cpu")

prompt = "A cyberpunk city at night with neon lights"
image = pipe(prompt).images[0]
image.show()
