"""
utils.py — Helper utilities for the GenAI Playground
=====================================================
Import this in your notebook with:
    from utils import display_image_grid, save_outputs, banner
"""

import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image
from io import BytesIO
import requests
from datetime import datetime


# ─────────────────────────────────────────────────────────────
#  Banner
# ─────────────────────────────────────────────────────────────
def banner(title: str, subtitle: str = ""):
    """Print a styled banner."""
    width = max(len(title), len(subtitle)) + 6
    border = "═" * width
    print(f"\n╔{border}╗")
    print(f"║  {title.center(width - 2)}  ║")
    if subtitle:
        print(f"║  {subtitle.center(width - 2)}  ║")
    print(f"╚{border}╝\n")


# ─────────────────────────────────────────────────────────────
#  Image helpers
# ─────────────────────────────────────────────────────────────
def load_image_from_url(url: str) -> Image.Image:
    """Load a PIL image from a URL."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return Image.open(BytesIO(response.content)).convert("RGB")


def display_image_grid(images, titles=None, cols=3, figsize_per_img=(4, 4)):
    """
    Display multiple images in a grid.

    Args:
        images: list of PIL.Image, file paths, or URLs
        titles: optional list of captions
        cols: number of columns
        figsize_per_img: size of each image cell
    """
    n = len(images)
    rows = (n + cols - 1) // cols
    fig_w = figsize_per_img[0] * cols
    fig_h = figsize_per_img[1] * rows

    fig, axes = plt.subplots(rows, cols, figsize=(fig_w, fig_h))
    axes = axes.flatten() if n > 1 else [axes]

    for i, (ax, img) in enumerate(zip(axes, images)):
        # Load image if necessary
        if isinstance(img, str):
            if img.startswith("http"):
                img = load_image_from_url(img)
            else:
                img = Image.open(img).convert("RGB")

        ax.imshow(img)
        ax.axis("off")
        if titles and i < len(titles):
            ax.set_title(titles[i], fontsize=10, pad=6)

    # Hide unused axes
    for ax in axes[n:]:
        ax.set_visible(False)

    plt.tight_layout()
    plt.show()


# ─────────────────────────────────────────────────────────────
#  File helpers
# ─────────────────────────────────────────────────────────────
def save_text(content: str, filename: str, output_dir: str = "../outputs"):
    """Save text content to a timestamped file."""
    os.makedirs(output_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(filename)
    ext = ext or ".txt"
    path = os.path.join(output_dir, f"{base}_{ts}{ext}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"💾 Saved to {path}")
    return path


def save_image(img: Image.Image, filename: str, output_dir: str = "../outputs"):
    """Save a PIL image to the outputs folder."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    img.save(path)
    print(f"🖼️  Image saved to {path}")
    return path


# ─────────────────────────────────────────────────────────────
#  Prompt helpers
# ─────────────────────────────────────────────────────────────
STYLE_TAGS = {
    "photorealistic": "photorealistic, 8k, highly detailed, professional photography",
    "anime":          "anime style, vibrant colors, Studio Ghibli, sharp lines",
    "oil_painting":   "oil painting, thick brushstrokes, classical art, museum quality",
    "watercolor":     "watercolor painting, soft edges, pastel colors, artistic",
    "cyberpunk":      "cyberpunk, neon lights, dystopian, dark atmosphere, 4k",
    "fantasy":        "fantasy art, magical, epic, detailed illustration",
    "minimal":        "minimalist, clean, simple shapes, white background",
}

def enhance_image_prompt(base_prompt: str, style: str = "photorealistic") -> str:
    """
    Enhance an image generation prompt with style tags.

    Args:
        base_prompt: Your core description
        style: One of photorealistic, anime, oil_painting, watercolor,
               cyberpunk, fantasy, minimal

    Returns:
        Enhanced prompt string
    """
    tag = STYLE_TAGS.get(style, "")
    enhanced = f"{base_prompt}, {tag}" if tag else base_prompt
    print(f"✨ Enhanced prompt: {enhanced}")
    return enhanced


# ─────────────────────────────────────────────────────────────
#  Device info
# ─────────────────────────────────────────────────────────────
def system_info():
    """Print system and GPU info."""
    import platform
    import torch

    banner("System Info", "GenAI Playground Environment")
    print(f"  OS      : {platform.system()} {platform.release()}")
    print(f"  Python  : {platform.python_version()}")
    print(f"  PyTorch : {torch.__version__}")
    print(f"  CUDA    : {'✅ Available — ' + torch.version.cuda if torch.cuda.is_available() else '❌ Not available (using CPU)'}")
    if torch.cuda.is_available():
        for i in range(torch.cuda.device_count()):
            name = torch.cuda.get_device_name(i)
            mem  = torch.cuda.get_device_properties(i).total_memory / 1e9
            print(f"  GPU {i}   : {name}  ({mem:.1f} GB VRAM)")
    print()


if __name__ == "__main__":
    system_info()
