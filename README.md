# 🤖 All-in-One Generative AI Playground

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![HuggingFace](https://img.shields.io/badge/🤗-Transformers-yellow)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red?logo=pytorch)
![Stars](https://img.shields.io/github/stars/yourusername/genai-playground?style=social)

**A comprehensive Jupyter Notebook exploring the full landscape of Generative AI —  
Text, Images, Stories, Poetry, Q&A, Chatbots, Translation and more.**

[🚀 Quick Start](#quick-start) · [📖 Features](#features) · [🛠️ Tech Stack](#tech-stack) · [📸 Screenshots](#screenshots) · [🤝 Contributing](#contributing)

</div>

---

## 📖 About

This project is a **hands-on, all-in-one AI playground** built inside a single Jupyter Notebook. It's designed for:

- 🎓 **Students** learning about Generative AI and NLP
- 🔬 **Researchers** quickly experimenting with pre-trained models
- 💻 **Developers** building a portfolio showcase
- 🤩 **Enthusiasts** exploring the power of modern AI

Every section is self-contained and fully documented with docstrings and comments — just run the cells!

---

## ✨ Features

| # | Feature | Model Used | Description |
|---|---------|-----------|-------------|
| 1 | ✍️ **Text Generation** | GPT-2 | Continue any text prompt with AI |
| 2 | ❓ **Question Answering** | DistilBERT | Extract answers from a given context |
| 3 | 📝 **Summarization** | BART-large-CNN | Condense long articles to key points |
| 4 | 😊 **Sentiment Analysis** | DistilBERT SST-2 | Detect positive/negative tone with charts |
| 5 | 📖 **Story Generator** | GPT-2 | Generate stories in 5 genres (sci-fi, fantasy, mystery…) |
| 6 | 🎭 **Poem Generator** | GPT-2 | Write poems on 5 themes (nature, love, AI…) |
| 7 | 🎨 **Image Generation** | Stable Diffusion 2.1 | Create images from text prompts (API + local) |
| 8 | 🔍 **Image Captioning** | BLIP | Automatically describe any image |
| 9 | 🌍 **Translation** | Helsinki-NLP | Translate between 7 language pairs |
| 10 | 💬 **Interactive Chatbot** | DialoGPT-medium | Have a multi-turn conversation with an AI |
| 11 | 📊 **Dashboard** | Matplotlib | Beautiful summary visualization of all features |

---

## 🚀 Quick Start

### Option A — Run on Google Colab (Recommended, Free GPU!)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/genai-playground/blob/main/notebooks/AI_Playground.ipynb)

1. Click the badge above
2. Set runtime to **T4 GPU**: `Runtime → Change runtime type → T4 GPU`
3. Run all cells from top to bottom!

---

### Option B — Run Locally

#### 1. Clone the repository
```bash
git clone https://github.com/yourusername/genai-playground.git
cd genai-playground
```

#### 2. Create a virtual environment (recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Launch Jupyter
```bash
jupyter lab
# or
jupyter notebook
```

#### 5. Open the notebook
Navigate to `notebooks/AI_Playground.ipynb` and run the cells!

---

## 🔑 Image Generation API Setup (Optional)

For the **Image Generation** section (Cell 11a), you need a free Hugging Face API token:

1. Create a free account at [huggingface.co](https://huggingface.co)
2. Go to [Settings → Access Tokens](https://huggingface.co/settings/tokens)
3. Create a new token (Read access is enough)
4. In the notebook, set your token:
   ```python
   import os
   os.environ['HF_TOKEN'] = 'hf_your_token_here'
   ```

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---------|---------|---------|
| 🐍 Python | 3.8+ | Core language |
| 🤗 Transformers | 4.35+ | NLP models (GPT-2, BERT, BART, BLIP…) |
| 🎨 Diffusers | 0.21+ | Stable Diffusion image generation |
| 🔥 PyTorch | 2.0+ | Deep learning backend |
| 📊 Matplotlib | 3.7+ | Charts and visualizations |
| 🖼️ Pillow | 10.0+ | Image loading and processing |
| 🌐 Requests | 2.31+ | API calls |

---

## 📁 Project Structure

```
genai-playground/
│
├── 📓 notebooks/
│   ├── AI_Playground.ipynb      ← Main notebook (start here!)
│   └── utils.py                 ← Helper functions
│
├── 📤 outputs/                  ← Auto-generated outputs
│   ├── sentiment_analysis.png
│   ├── dashboard.png
│   ├── story_sci-fi.txt
│   ├── poem_AI.txt
│   └── ...
│
├── 🖼️ assets/                   ← Place your own images here
│
├── 📋 requirements.txt          ← Python dependencies
├── 📄 LICENSE                   ← MIT License
└── 📖 README.md                 ← This file
```

---

## 💡 Usage Examples

### Generate a story
```python
story = generate_story(genre="fantasy", max_length=300)
```

### Analyze sentiment
```python
analyze_sentiment([
    "This project is amazing!",
    "I'm not impressed at all."
])
```

### Caption an image
```python
caption_image("https://example.com/my_photo.jpg", title="My Photo")
```

### Translate text
```python
translate("Hello, how are you?", src_lang="en", tgt_lang="fr")
# 🇫🇷 FR: Bonjour, comment allez-vous ?
```

### Chat with AI
```python
bot = Chatbot()
response = bot.chat("What do you think about AI?")
print(response)
```

---

## ⚙️ Configuration

You can tune these parameters throughout the notebook:

| Parameter | Default | Effect |
|-----------|---------|--------|
| `temperature` | 0.9 | Higher = more creative/random |
| `max_length` | 200 | Controls output length |
| `num_return_sequences` | 1 | Number of generations |
| `top_p` | 0.92 | Nucleus sampling threshold |
| `num_inference_steps` | 25 | Image quality (more = better, slower) |
| `guidance_scale` | 7.5 | How strictly to follow the prompt |

---

## 📸 Screenshots

> *(Generated outputs will appear in `outputs/` after you run the cells)*

**Dashboard Overview**
![Dashboard](outputs/dashboard.png)

**Sentiment Analysis Chart**
![Sentiment](outputs/sentiment_analysis.png)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

Ideas for contributions:
- 🎵 Audio/Music generation (MusicGen)
- 🗣️ Text-to-Speech (Bark, SpeechT5)
- 📹 Video generation
- 🔄 More translation language pairs
- 🎮 Interactive widgets with ipywidgets

---

## 📚 Learning Resources

- [Hugging Face Course](https://huggingface.co/course) — Free NLP course
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [Diffusers Documentation](https://huggingface.co/docs/diffusers)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Stable Diffusion Guide](https://stability.ai/blog/stable-diffusion-public-release)



---

## ⭐ Show Your Support

If you found this project helpful, please consider:
- ⭐ **Starring** this repository
- 🍴 **Forking** it to build your own version
- 📢 **Sharing** it with friends and colleagues

---

<div align="center">

Made with ❤️ and 🤖 AI

**Happy Generating!**

</div>
