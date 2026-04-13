# 🛠️ Setup Guide — GenAI Playground

## ✅ System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.8 | 3.10+ |
| RAM | 8 GB | 16 GB |
| GPU VRAM | — (CPU mode) | 4 GB+ (for local Stable Diffusion) |
| Disk Space | 5 GB | 15 GB |
| Internet | Required | Required |

---

## 🔧 Installation (Step by Step)

### Step 1: Install Python
Download Python 3.10+ from https://python.org/downloads/

### Step 2: Clone or Download the Project
```bash
git clone https://github.com/yourusername/genai-playground.git
cd genai-playground
```
*Or download and unzip the ZIP from GitHub.*

### Step 3: Create Virtual Environment
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```
*This may take 5–10 minutes to download all packages.*

### Step 5: Launch Jupyter
```bash
jupyter lab
```
Then open `notebooks/AI_Playground.ipynb`

---

## ☁️ Google Colab Setup (No Installation Needed)

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. File → Upload notebook → Upload `AI_Playground.ipynb`
3. Runtime → Change runtime type → **T4 GPU**
4. Run Cell 1 to install packages
5. Enjoy free GPU power!

---

## 🔑 API Keys

### Hugging Face Token (for Image Generation)
1. Sign up free at https://huggingface.co
2. Go to https://huggingface.co/settings/tokens
3. Click "New token" → name it → Create
4. Copy the token (starts with `hf_`)
5. In the notebook:
```python
import os
os.environ['HF_TOKEN'] = 'hf_xxxxxxxxxxxxxxxxxxxx'
```

---

## ❓ Troubleshooting

### "CUDA out of memory"
- Restart the kernel and run only the section you need
- Reduce `max_length` or `num_inference_steps`
- Use CPU mode (automatic fallback)

### "Model loading failed" or "Connection error"
- Check internet connection
- Models download automatically from Hugging Face on first run
- Some models are ~1–5 GB, wait for download to finish

### Slow on CPU
- Image generation is very slow on CPU (30+ mins per image)
- Use Hugging Face API (Cell 11a) instead — no GPU needed
- Or use Google Colab for free GPU

### Import errors
- Make sure you activated the virtual environment
- Re-run: `pip install -r requirements.txt`

---

## 📞 Support

- Open an [Issue on GitHub](https://github.com/yourusername/genai-playground/issues)
- Check existing issues first
- Include your Python version and error message
