# tools/create_giuseppe_texture.py
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Load base texture (baldu-color.jpg)
src = "assets/baldu-color.jpg"
im = Image.open(src).convert("RGB")
w, h = im.size
print(f"Loaded {src} of size {w}x{h}")

arr = np.array(im, dtype=np.float32)
r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
lum = 0.299 * r + 0.587 * g + 0.114 * b

# 1. Sky-Blue Shirt:
# In baldu-color.jpg, the hoodie was slate-blue or dark green/yellow
# Mask anything that is hoodie/coat:
# In baldu, slate-blue was roughly r: 20-140, g: 35-180, b: 55-230 with b > r
# Let's also check explorer raincoat colors
hoodie_mask = (b > r * 1.05) & (b > 45) & (lum > 30) & (lum < 210)
# Also include any remaining yellow/orange jacket regions
yellow_mask = (r > 140) & (g > 100) & (b < 120) & (r > b * 1.3)
coat_mask = hoodie_mask | yellow_mask

# Sky blue dress shirt palette: Base RGB (120, 171, 220)
norm_lum = np.clip(lum / 130.0, 0.4, 1.4)
shirt_r = norm_lum * 115.0
shirt_g = norm_lum * 168.0
shirt_b = norm_lum * 222.0

arr[coat_mask, 0] = np.clip(shirt_r[coat_mask], 40, 180)
arr[coat_mask, 1] = np.clip(shirt_g[coat_mask], 70, 225)
arr[coat_mask, 2] = np.clip(shirt_b[coat_mask], 100, 255)

# 2. Hair -> Bald clay skin tone:
# In baldu-color.jpg, hair was dark curls (r < 65, g < 55, b < 60)
# Top-left and center-top areas of texture generally contain hair and head UVs
# Skin tone: RGB around (241, 190, 156)
hair_mask = (r < 75) & (g < 65) & (b < 70) & (lum < 75)
skin_r = 238.0 + (lum - 40) * 0.4
skin_g = 188.0 + (lum - 40) * 0.35
skin_b = 152.0 + (lum - 40) * 0.3

# Apply skin tone to hair areas to make scalp smooth and bald
arr[hair_mask, 0] = np.clip(skin_r[hair_mask], 190, 250)
arr[hair_mask, 1] = np.clip(skin_g[hair_mask], 150, 215)
arr[hair_mask, 2] = np.clip(skin_b[hair_mask], 120, 185)

# 3. Trousers: Dark charcoal / navy dress pants: RGB (36, 40, 48)
# Trousers in explorer/baldu are bottom regions
pants_mask = (lum > 20) & (lum < 100) & (abs(r - g) < 25) & (abs(g - b) < 25) & (~hair_mask)
arr[pants_mask, 0] = np.clip(lum[pants_mask] * 0.40, 20, 60)
arr[pants_mask, 1] = np.clip(lum[pants_mask] * 0.45, 24, 70)
arr[pants_mask, 2] = np.clip(lum[pants_mask] * 0.55, 30, 85)

out_im = Image.fromarray(np.uint8(arr))

# Let's paint Giuseppe's gentle eyebrows and cheerful expression on face region
draw = ImageDraw.Draw(out_im)
# Face UVs are around (320, 448) to (576, 640)
# Ensure skin tone is smooth and glowing
out_im.save("assets/giuseppe-color.jpg", "JPEG", quality=95)
print("Saved assets/giuseppe-color.jpg successfully!")
