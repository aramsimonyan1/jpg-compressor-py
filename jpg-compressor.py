import os
from PIL import Image

"""
Compress a JPG image and save it to the output path.
    :param input_path: Path to the input JPG file
    :param output_path: Path to save the compressed JPG file
    :param quality: JPEG quality (1-95), lower means more compression
    :param resize_percent: Percentage to resize image (e.g., 50 = 50% smaller). None or 100 = no resize.
"""
def compress_jpg(input_path, output_path, quality, resize_percent=None):
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Preserve metadata
            exif_data = img.info.get("exif")
            icc_profile = img.info.get("icc_profile")
            
            # Convert if needed (Ensure it's in RGB mode as JPEG doesn't support alpha)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
                    
            # Resize if requested
            if resize_percent and resize_percent != 100:
                width, height = img.size
                new_width = int(width * resize_percent / 100)
                new_height = int(height * resize_percent / 100)
                img = img.resize((new_width, new_height), Image.LANCZOS)

            # Save with optimized settings
            img.save(
                output_path, 
                "JPEG", 
                optimize=True, 
                quality=quality, 
                exif=exif_data, 
                icc_profile=icc_profile
            )
        
        print(f"Compressed: {input_path} → {output_path} (Quality={quality}, Resize={resize_percent or 100}%)")
    
    except Exception as e:
        print(f"Error compressing {input_path}: {e}")

# For bulk processing of all files in a folder: loops through files and calls compress_jpg()
def batch_compress_jpg(input_dir, output_dir, quality, resize_percent=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg")):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            compress_jpg(input_path, output_path, quality, resize_percent)

# entry point / configuration
if __name__ == "__main__":
    source_folder = r"C:\Users\simon\Desktop\im"   # Folder with original JPGs
    destination_folder = r"C:\Users\simon\Desktop\im_compressed"  # Folder for compressed JPGs
    compression_quality = 80  # Lower = smaller file, but less quality
    resize_percent = 50       # e.g., 50% of original size (set None or 100 for no resizing)

    batch_compress_jpg(source_folder, destination_folder, compression_quality, resize_percent)