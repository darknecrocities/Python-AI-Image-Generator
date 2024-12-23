from diffusers import StableDiffusionPipeline
import torch
from datetime import datetime
import random

def setup_pipeline():
    """
    Sets up the Stable Diffusion pipeline using the specified model.
    Attempts to use GPU (CUDA) if available, falls back to CPU otherwise.
    """
    model_id = "runwayml/stable-diffusion-v1-5"
    pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    
    # Check for GPU availability
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    pipeline = pipeline.to(device)
    return pipeline

def generate_image(prompt, pipeline, output_path="generated_image.png", resolution=(512, 512)):
    """
    Generates an image based on the given text prompt using the specified pipeline.
    Saves the generated image to the output path.
    """
    print(f"Generating image for: '{prompt}' with resolution {resolution}")
    
    # Update resolution dynamically
    generator = torch.Generator(device=pipeline.device)
    generator.manual_seed(random.randint(0, 10000))  # Random seed for diversity
    
    image = pipeline(prompt, height=resolution[0], width=resolution[1], generator=generator).images[0]
    image.save(output_path)
    print(f"Image saved to {output_path}")
    return image

def save_prompt_history(prompt, output_path):
    """
    Saves the prompt and its corresponding image path to a history log file.
    """
    with open("image_history.log", "a") as log_file:
        log_file.write(f"{datetime.now()} - Prompt: '{prompt}' - Saved as: {output_path}\n")

def suggest_prompt(keyword):
    """
    Provides a random suggestion based on a keyword.
    """
    suggestions = {
        "nature": ["A tranquil forest at sunset", "Snow-covered mountains with a bright sky", "A serene beach with waves"],
        "space": ["A nebula with vibrant colors", "An astronaut floating in space", "A futuristic space station"],
        "fantasy": ["A dragon flying over a medieval castle", "An enchanted forest with glowing plants", "A wizard casting a spell"]
    }
    return random.choice(suggestions.get(keyword.lower(), ["No suggestions available for this keyword."]))

if __name__ == "__main__":
    # Initialize the pipeline
    pipeline = setup_pipeline()
    
    print("Welcome to the Enhanced AI Image Generator!")
    print("Type 'exit' at any time to end the program.")
    
    while True:
        # Prompt user for input
        prompt = input("\nEnter a text prompt for the image (or 'exit' to quit, 'random' for AI-generated prompt): ").strip()
        
        if prompt.lower() == "exit":
            print("Thank you for using the AI Image Generator. Goodbye!")
            break
        
        if prompt.lower() == "random":
            prompt = random.choice([
                "A futuristic cityscape at night",
                "A magical unicorn in a mystical forest",
                "A high-tech robot in a neon-lit city"
            ])
            print(f"Random prompt chosen: {prompt}")
        
        if prompt.lower().startswith("suggest"):
            keyword = prompt.split(" ", 1)[-1] if len(prompt.split()) > 1 else "nature"
            print(f"Suggestion for '{keyword}': {suggest_prompt(keyword)}")
            continue
        
        # Ask for resolution
        try:
            resolution = input("Enter image resolution as 'width,height' (default 512,512): ").strip()
            if resolution:
                width, height = map(int, resolution.split(","))
            else:
                width, height = 512, 512
        except ValueError:
            print("Invalid resolution input. Using default 512x512.")
            width, height = 512, 512
        
        # Generate unique filename based on the prompt or timestamp
        sanitized_prompt = "_".join(prompt.split())[:50]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"generated_{sanitized_prompt or timestamp}.png"
        
        try:
            # Generate and save the image
            image = generate_image(prompt, pipeline, output_path=output_path, resolution=(height, width))
            save_prompt_history(prompt, output_path)
            image.show()
        except Exception as e:
            print(f"An error occurred: {e}")
            retry = input("Do you want to retry this prompt? (yes/no): ").strip().lower()
            if retry != "yes":
                continue
