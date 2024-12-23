# 🌟 AI Image Generator: Create Stunning AI-Generated Images!

Welcome to the **AI Image Generator** repository! 🎨✨ This project uses the power of **Stable Diffusion** to create stunning images from text prompts. Whether you're looking to generate surreal landscapes, futuristic cities, or artistic visuals, this tool is here to bring your imagination to life!

---

## 🚀 Features

- **Custom Image Prompts**: Enter your own text descriptions to generate unique images.
- **Dynamic Resolution Support**: Choose custom image resolutions or stick with the default.
- **Random Prompt Generator**: Feeling uninspired? Let AI generate a prompt for you!
- **Prompt Suggestions**: Get ideas based on categories like `nature`, `fantasy`, or `space`.
- **Image History Logging**: Keeps track of all your prompts and image outputs.
- **GPU Acceleration**: Leverages CUDA for fast image generation (falls back to CPU if unavailable).

---

## 🛠️ Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- `torch` (with CUDA support if using GPU)
- `diffusers`
- `Pillow`

Install dependencies with the following command:
```bash
pip install torch torchvision diffusers Pillow
```

---

## 📖 How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/AI-Image-Generator.git
   cd AI-Image-Generator
   ```

2. **Run the Script**:
   ```bash
   python main.py
   ```

3. **Follow the Prompts**:
   - Enter a text prompt (e.g., `A futuristic cityscape at night`).
   - Optionally specify a resolution (e.g., `1024,768`).
   - Choose whether to retry if errors occur.

4. **View & Save**:
   - The generated image will be saved to the working directory.
   - Image history is logged in `image_history.log`.

---

## 🎉 Example Prompts

- 🌄 `A tranquil forest at sunset`
- 🌌 `A nebula with vibrant colors`
- 🐉 `A dragon flying over a medieval castle`
- 🤖 `A high-tech robot in a neon-lit city`

---

## 💡 Advanced Features

### Prompt Suggestions
Type `suggest <keyword>` to get ideas. Example keywords:
- `nature`
- `fantasy`
- `space`

### Random Prompts
Type `random` for a surprise AI-generated prompt! 🎲

### Error Handling
The program automatically catches and displays errors with options to retry your prompt.

---

## 📂 Output Files

- **Generated Images**: Saved as `generated_<prompt>.png`
- **Prompt History**: Logged in `image_history.log`

---

## 🤝 Contributing

Want to improve the project? Here’s how you can help:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add a cool new feature!"
   ```
4. Push and submit a Pull Request. 💾

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- 🤗 [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index) for providing the Stable Diffusion pipeline.
- 🧑‍💻 [PyTorch](https://pytorch.org/) for powering the computations.

---

## 📬 Contact

Questions or suggestions? Feel free to reach out:
- GitHub: [darknecrocities](https://github.com/darknecrocities/Python-AI-Image-Generator/tree/main/Documents/Portfolio%20Projecr/AI%20Image%20Generator)
- Email: parejasarronkian@gmail.com
Happy Generating! 🌟

