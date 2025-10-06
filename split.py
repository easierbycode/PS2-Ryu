from PIL import Image

sheet = Image.open("ryu_sheet.png")

frame_width = 48  # Reduced by 1 more
frame_height = 128
frames_count = 36

import os
os.makedirs("frames", exist_ok=True)

for i in range(frames_count):
    left = i * 50
    frame = sheet.crop((left, 0, left + frame_width, frame_height))
    frame.save(f"frames/frame_{i:03d}.png")

print(f"Extracted {frames_count} frames")