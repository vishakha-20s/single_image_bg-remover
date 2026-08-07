# single_image_bg-remover

A simple Python script that removes the background from a single image using AI, powered by [rembg](https://github.com/danielgatis/rembg).

## Features
- Accepts JPG, JPEG, and PNG images
- Automatically saves output as `<filename>_no_bg.png`
- Simple command-line usage

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python remove_background.py <path_to_image>
```

**Example:**
```bash
python remove_background.py mycat.jpg
```

This will create `mycat_no_bg.png` in the same folder.

## Tech Used
- [rembg](https://github.com/danielgatis/rembg) – AI-based background removal
- [Pillow](https://pypi.org/project/Pillow/) – Image handling
