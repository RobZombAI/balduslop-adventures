import re

with open("bundle/index-gta-v1.js", "r") as f:
    content = f.read()

levels = re.findall(r"const\s+(augustaL\d+)\s*=\s*yr\(\{(.*?)\n\}\);", content, re.DOTALL)

for lvl_name, lvl_body in levels:
    decor_match = re.search(r"decor:\s*\[(.*?)\]", lvl_body, re.DOTALL)
    if decor_match:
        items = re.findall(r'kind:\s*["\']([^"\']+)["\']', decor_match.group(1))
        print(f"{lvl_name}: {len(items)} decor items: {set(items)}")
    else:
        print(f"{lvl_name}: NO decor found!")
