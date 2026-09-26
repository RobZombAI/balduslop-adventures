with open("bundle/index-gta-v1.js") as f:
    text = f.read()

import re
matches = re.findall(r',\s*["\']([a-zA-Z0-9_-]+)["\']\s*\(t,\s*e,\s*n\)\s*\{', text)
print(f"Total decor keys in _D: {len(matches)}")
print("Decor keys:", matches)
