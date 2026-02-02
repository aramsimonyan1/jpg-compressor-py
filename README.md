# 🖼️ JPEG Compressor (Python)

A lightweight **Python tool for compressing and resizing JPEG images** in bulk using the [Pillow (PIL)](https://pypi.org/project/pillow/) library.  
This project helps reduce image file sizes efficiently — ideal for web optimization, storage management, or faster data transfer.

---

## 🚀 Features

- 🗜️ **Batch Compression** — Compresses all `.jpg` and `.jpeg` files in a folder.
- ⚙️ **Custom Quality Control** — Set JPEG quality (1–95) to balance file size and visual quality.
- 📏 **Optional Resizing** — Reduce image dimensions by a given percentage.
- 🧠 **Automatic Optimization** — Uses Pillow’s optimized saving for efficient compression.
- 🧩 **Cross-Platform** — Works on Windows, macOS, and Linux.

---

## 🧰 Requirements

- Python 3.7 or higher  
- Pillow library  

Install Pillow via pip:

```bash
pip install pillow
```

---

## 📂 Project Structure

```
jpg-compressor-py/
│
├── jpg-compressor.py       # Main script for compression
└── README.md               # Project documentation
```

---

## ⚡ Usage

### 1. Update your folder paths

Edit the following lines in `jpg-compressor.py` to match your system:

```python
source_folder = r"C:\input\folder\path\input-folder-name"        # Replace with Input folder/path with original JPGs
destination_folder = r"C:\output\folder\path\output-folder-name" # Replace with Output folder/path for compressed images
```

### 2. Adjust compression settings (optional)

```python
compression_quality = 70  # JPEG quality (1–95)
resize_percent = 25       # Resize to 25% of original (set None or 100 to skip resizing)
```

### 3. Run the script

```bash
python jpg-compressor.py
```

You’ll see a log of each file processed:

```
Compressed: image1.jpg → image1.jpg (Quality=70, Resize=25%)
```

---

## 🧩 Example Output

| Original | Compressed |
|-----------|-------------|
| 2.4 MB (100%) | 350 KB (25% resized, 70% quality) |

---

## 🧠 Functions Overview

### `compress_jpg(input_path, output_path, quality, resize_percent=None)`
Compresses a single JPEG image with optional resizing.

### `batch_compress_jpg(input_dir, output_dir, quality, resize_percent=None)`
Compresses all JPEGs in a directory and saves them to the output folder.

---

## 💡 Use Cases

- Preparing images for websites or apps  
- Reducing storage usage on servers  
- Optimizing datasets for machine learning  
- Compressing large photo collections

---

## 🪪 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.