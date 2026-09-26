import json, struct
import numpy as np

with open("assets/explorer.glb", "rb") as f:
    f.seek(12)
    chunk_len, chunk_type = struct.unpack("<I4s", f.read(8))
    gltf = json.loads(f.read(chunk_len).decode("utf-8"))
    bin_chunk_len, bin_chunk_type = struct.unpack("<I4s", f.read(8))
    bin_data = f.read(bin_chunk_len)

print("Images:")
for i, img in enumerate(gltf.get("images", [])):
    bv = gltf["bufferViews"][img["bufferView"]]
    offset = bv.get("byteOffset", 0)
    length = bv["byteLength"]
    mime = img.get("mimeType", "")
    name = img.get("name", f"img_{i}")
    print("  Image {}: {} ({}), bytes: {}".format(i, name, mime, length))
    # Save image
    ext = ".jpg" if "jpeg" in mime else ".png"
    with open(f"assets/extracted_{name}{ext}", "wb") as out_f:
        out_f.write(bin_data[offset:offset+length])
    print("    Saved as assets/extracted_{}{}".format(name, ext))

mesh = gltf["meshes"][0]
prim = mesh["primitives"][0]
print("\nPrimitive attributes:")
for k, v in prim["attributes"].items():
    acc = gltf["accessors"][v]
    print("  {}: count={}, type={}, min={}, max={}".format(k, acc["count"], acc["type"], acc.get("min"), acc.get("max")))

# Inspect positions
pos_acc = gltf["accessors"][prim["attributes"]["POSITION"]]
bv = gltf["bufferViews"][pos_acc["bufferView"]]
pos_bytes = bin_data[bv.get("byteOffset", 0):bv.get("byteOffset", 0) + bv["byteLength"]]
positions = np.frombuffer(pos_bytes, dtype=np.float32).reshape(-1, 3)
print("\nPositions shape:", positions.shape)
print("Min bounds:", positions.min(axis=0))
print("Max bounds:", positions.max(axis=0))

# Y ranges
print("Y < 0.8 (Legs & Shoes):", np.sum(positions[:, 1] < 0.8))
print("0.8 <= Y < 1.35 (Torso, Arms, Backpack):", np.sum((positions[:, 1] >= 0.8) & (positions[:, 1] < 1.35)))
print("Y >= 1.35 (Head & Hair):", np.sum(positions[:, 1] >= 1.35))
# Backpack check:
bp_mask = (positions[:, 1] >= 0.8) & (positions[:, 1] < 1.38) & (positions[:, 2] < -0.12)
print("Backpack vertices (Z < -0.12 in torso):", np.sum(bp_mask))
# Spiky hair check:
hair_mask = (positions[:, 1] >= 1.48)
print("Vertices with Y >= 1.48 (Hair peak):", np.sum(hair_mask))
