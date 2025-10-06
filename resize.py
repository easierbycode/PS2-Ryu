from PIL import Image
import os

input_folder = "frames-edit"
output_folder = "frames"

# Target dimensions - adjust these if needed
TARGET_WIDTH = 80
TARGET_HEIGHT = 128

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# Process each frame
for i in range(36):
    filename = f"frame_{i:03d}.png"
    input_path = os.path.join(input_folder, filename)
    
    if not os.path.exists(input_path):
        print(f"Skipping {filename} - not found")
        continue
    
    # Load original frame
    img = Image.open(input_path)
    original_width, original_height = img.size
    
    # Create new canvas with target size (transparent background)
    canvas = Image.new('RGBA', (TARGET_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))
    
    # Calculate position to center horizontally and align to bottom
    x_offset = (TARGET_WIDTH - original_width) // 2
    y_offset = TARGET_HEIGHT - original_height
    
    # Paste original image onto canvas
    canvas.paste(img, (x_offset, y_offset), img if img.mode == 'RGBA' else None)
    
    # Save
    output_path = os.path.join(output_folder, filename)
    canvas.save(output_path)
    print(f"Processed {filename}: {original_width}x{original_height} -> {TARGET_WIDTH}x{TARGET_HEIGHT}")

print(f"\nAll frames resized and aligned to {TARGET_WIDTH}x{TARGET_HEIGHT}")
print("Bottom-aligned, horizontally centered")