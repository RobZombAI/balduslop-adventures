# tools/generate_giuseppe_texture.py
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Load original explorer color texture
src_path = "assets/extracted_explorer-color.jpg"
im = Image.open(src_path).convert("RGB")
w, h = im.size
print(f"Loaded {src_path} ({w}x{h})")

arr = np.array(im, dtype=np.float32)
r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
lum = 0.299 * r + 0.587 * g + 0.114 * b

# 1. SHIRT: Convert Yellow Raincoat -> Giuseppe's Sky-Blue Shirt (#72aadc / RGB 114, 170, 220)
# In explorer-color, yellow jacket has high R, high G, low B (R > 130, G > 100, B < 120, R > B * 1.3)
yellow_jacket = (r > 120) & (g > 90) & (b < 140) & (r > b * 1.25)

# Also check for orange/tan borders of jacket
orange_rim = (r > 130) & (g > 60) & (g < 140) & (b < 80)
jacket_mask = yellow_jacket | orange_rim

# Target sky-blue shirt color
target_r = 114.0
target_g = 170.0
target_b = 220.0

norm_lum = np.clip(lum / 160.0, 0.35, 1.45)
arr[jacket_mask, 0] = np.clip(norm_lum[jacket_mask] * target_r, 20, 230)
arr[jacket_mask, 1] = np.clip(norm_lum[jacket_mask] * target_g, 40, 245)
arr[jacket_mask, 2] = np.clip(norm_lum[jacket_mask] * target_b, 60, 255)

# 2. PANTS & SHOES: Refine to dark charcoal/slate trousers (#222a36)
# Dark pixels in original
dark_mask = (lum < 75) & (lum > 15) & (~jacket_mask)
arr[dark_mask, 0] = np.clip(lum[dark_mask] * 0.40, 20, 55)
arr[dark_mask, 1] = np.clip(lum[dark_mask] * 0.48, 25, 68)
arr[dark_mask, 2] = np.clip(lum[dark_mask] * 0.62, 35, 85)

# 3. SKIN TONE: Warm smooth clay peach (#f2be9e / RGB 242, 190, 158)
skin_mask = (r > 160) & (g > 115) & (b > 85) & (r > g) & (g > b) & (~jacket_mask)
norm_skin_lum = np.clip(lum / 175.0, 0.6, 1.3)
arr[skin_mask, 0] = np.clip(norm_skin_lum[skin_mask] * 242.0, 180, 255)
arr[skin_mask, 1] = np.clip(norm_skin_lum[skin_mask] * 190.0, 140, 230)
arr[skin_mask, 2] = np.clip(norm_skin_lum[skin_mask] * 158.0, 110, 200)

out_im = Image.fromarray(np.uint8(arr))

# Let's save as assets/giuseppe-color.jpg and assets/explorer-giuseppe.jpg
out_im.save("assets/giuseppe-color.jpg", "JPEG", quality=95)
out_im.save("assets/explorer-giuseppe.jpg", "JPEG", quality=95)
print("Saved assets/giuseppe-color.jpg and assets/explorer-giuseppe.jpg successfully!")
