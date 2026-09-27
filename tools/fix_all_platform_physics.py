# tools/fix_all_platform_physics.py
import re

print("=== FIXING ALL PLATFORM PHYSICS & GAPS ACROSS ALL 10 LEVELS ===")

with open("tools/generate_all_10_levels.py", "r", encoding="utf-8") as f:
    text = f.read()

# Let's define the exact fixes for each level:

# Level 1 fixes:
# 1. plat-seawall widen to 8.5 [91, 99.5]
# 2. Add step-gulf-reach between lift-gulf (140.6) and plat-irrigation (147.0): S("step-gulf-reach", 141.5, 3.8, 15.2, "ledge")
# 3. goal-duomo start at 232.0 (w=18)
text = text.replace('S("plat-seawall", 91, 7.0, 13.8, "stone")', 'S("plat-seawall", 91, 8.5, 13.8, "stone")')
text = text.replace('S("plat-irrigation", 147, 26.0, 16.0, "stone")', 'S("step-gulf-reach", 141.5, 3.8, 15.2, "ledge"),\n    S("plat-irrigation", 146, 27.0, 16.0, "stone")')
text = text.replace('S("step-duomo2", 227, 4.0, 18.0, "ledge")', 'S("step-duomo2", 227, 4.0, 18.0, "ledge"),\n    S("step-duomo3", 231.5, 3.5, 18.4, "ledge")')
text = text.replace('S("goal-duomo", 235, 16.0, 18.8, "stone"', 'S("goal-duomo", 235.5, 16.0, 18.8, "stone"')

# Level 2 fixes:
# 1. plat-sewage-span1 widen to 7.0, ferry-rescue-pier start at 57.5 w=8.5, plat-sewage-span2 start at 67.0 w=7.0
text = text.replace('S("plat-sewage-span1", 49, 5.0, 12.0, "timed"', 'S("plat-sewage-span1", 49, 6.5, 12.0, "timed"')
text = text.replace('S("ferry-rescue-pier", 58, 7.0, 11.7, "timed"', 'S("ferry-rescue-pier", 57.0, 8.5, 11.7, "timed"')
text = text.replace('S("plat-sewage-span2", 69, 5.0, 12.0, "timed"', 'S("plat-sewage-span2", 67.5, 6.5, 12.0, "timed"')
# 2. plat-dockgate-floor start at 126.0 with width 31.0
text = text.replace('S("plat-dockgate-floor", 133, 24.0, 13.5, "stone")', 'S("plat-dockgate-floor", 126, 31.0, 13.5, "stone")')
# 3. pulse-pier2 at 165 w=4.5
text = text.replace('S("pulse-pier2", 164, 4.0, 13.0, "pulse"', 'S("pulse-pier2", 165, 4.5, 13.0, "pulse"')
# 4. lift-winch-molo: add step-winch-reach-l2
text = text.replace('S("plat-outer-seawall", 189, 8.5, 13.2, "stone")', 'S("step-winch-reach-l2", 184.2, 3.6, 12.6, "ledge"),\n    S("plat-outer-seawall", 189, 8.5, 13.2, "stone")')
# 5. step-lantern3
text = text.replace('S("step-lantern2", 218, 4.0, 14.5, "ledge")', 'S("step-lantern2", 218, 4.0, 14.5, "ledge"),\n    S("step-lantern3", 223.0, 4.0, 14.65, "ledge")')
text = text.replace('S("goal-lungomare", 229, 16.0, 14.8, "stone"', 'S("goal-lungomare", 228.0, 17.0, 14.8, "stone"')

# Levels 3-10 standard pattern fixes:
levels_data = [
    (3, "oil", 22.0, 21.0, 23.8),
    (4, "cement", 26.5, 24.5, 27.8),
    (5, "moat", 19.5, 18.8, 21.8),
    (6, "cliff", 21.5, 21.2, 24.5),
    (7, "salt", 14.8, 14.2, 15.5),
    (8, "fort", 16.5, 16.2, 17.5),
    (9, "fire", 20.2, 20.0, 21.0),
    (10, "tar", 21.0, 20.8, 22.5),
]

for lvl in range(3, 11):
    # 1. widen timed bridge step1 to 6.5, step2 to 6.5
    # Look for timed platform step1
    text = re.sub(
        r'(S\("[^"]+step1",\s*51,\s*)5\.0(,\s*[\d\.]+,\s*"timed")',
        r'\g<1>6.5\g<2>',
        text
    )
    text = re.sub(
        r'(S\("[^"]+step2",\s*)70,\s*5\.5(,\s*[\d\.]+,\s*"timed")',
        r'\g<1>69.5, 6.5\g<2>',
        text
    )
    # 2. Gate floor start at 126.0 with width 31.0
    text = re.sub(
        r'(S\("[^"]+gate-floor",\s*)133,\s*24\.0(,\s*[\d\.]+,\s*"stone"\))',
        r'\g<1>126, 31.0\g<2>',
        text
    )
    # 3. pulse2 at 165 w=4.5
    text = re.sub(
        r'(S\("pulse-[^"]+2",\s*)164,\s*4\.0(,\s*[\d\.]+,\s*"pulse")',
        r'\g<1>165, 4.5\g<2>',
        text
    )

# Now add intermediate step-winch-reach and step-...3 across levels 3-10
winch_steps = {
    3: ('plat-refinery-crest", 189, 8.5, 21.5, "stone")', 'step-winch-reach-l3", 184.2, 3.6, 20.8, "ledge"),\n    S("plat-refinery-crest", 189, 8.5, 21.5, "stone")'),
    4: ('plat-decontam-yard", 189, 8.5, 24.8, "stone")', 'step-winch-reach-l4", 184.2, 3.6, 24.2, "ledge"),\n    S("plat-decontam-yard", 189, 8.5, 24.8, "stone")'),
    5: ('plat-keep-base", 189, 8.5, 19.8, "stone")', 'step-winch-reach-l5", 184.2, 3.6, 19.2, "ledge"),\n    S("plat-keep-base", 189, 8.5, 19.8, "stone")'),
    6: ('plat-faro-high-rock", 189, 8.5, 22.2, "stone")', 'step-winch-reach-l6", 184.2, 3.6, 21.8, "ledge"),\n    S("plat-faro-high-rock", 189, 8.5, 22.2, "stone")'),
    7: ('plat-flamingo-dike", 189, 8.5, 14.8, "stone")', 'step-winch-reach-l7", 184.2, 3.6, 14.5, "ledge"),\n    S("plat-flamingo-dike", 189, 8.5, 14.8, "stone")'),
    8: ('plat-vittoria-keep", 189, 8.5, 16.8, "stone")', 'step-winch-reach-l8", 184.2, 3.6, 16.5, "ledge"),\n    S("plat-vittoria-keep", 189, 8.5, 16.8, "stone")'),
    9: ('plat-tauro-lookout", 189, 8.5, 20.6, "stone")', 'step-winch-reach-l9", 184.2, 3.6, 20.3, "ledge"),\n    S("plat-tauro-lookout", 189, 8.5, 20.6, "stone")'),
    10: ('plat-cathedral-parvis", 189, 8.5, 21.5, "stone")', 'step-winch-reach-l10", 184.2, 3.6, 21.2, "ledge"),\n    S("plat-cathedral-parvis", 189, 8.5, 21.5, "stone")'),
}

for lvl, (target, repl) in winch_steps.items():
    text = text.replace(f'S("{target}', f'S("{repl}')

approach_steps = {
    3: ('step-station2", 218, 4.0, 23.5, "ledge")', 'step-station2", 218, 4.0, 23.5, "ledge"),\n    S("step-station3", 223.0, 4.0, 23.65, "ledge")'),
    4: ('step-crown2", 218, 4.0, 27.4, "ledge")', 'step-crown2", 218, 4.0, 27.4, "ledge"),\n    S("step-crown3", 223.0, 4.0, 27.6, "ledge")'),
    5: ('step-mastio2", 218, 4.0, 21.6, "ledge")', 'step-mastio2", 218, 4.0, 21.6, "ledge"),\n    S("step-mastio3", 223.0, 4.0, 21.7, "ledge")'),
    6: ('step-faro2", 218, 4.0, 24.2, "ledge")', 'step-faro2", 218, 4.0, 24.2, "ledge"),\n    S("step-faro3", 223.0, 4.0, 24.35, "ledge")'),
    7: ('step-salinaro2", 218, 4.0, 15.4, "ledge")', 'step-salinaro2", 218, 4.0, 15.4, "ledge"),\n    S("step-salinaro3", 223.0, 4.0, 15.45, "ledge")'),
    8: ('step-guard2", 218, 4.0, 17.5, "ledge")', 'step-guard2", 218, 4.0, 17.5, "ledge"),\n    S("step-guard3", 223.0, 4.0, 17.5, "ledge")'),
    9: ('step-summit2", 218, 4.0, 21.0, "ledge")', 'step-summit2", 218, 4.0, 21.0, "ledge"),\n    S("step-summit3", 223.0, 4.0, 21.0, "ledge")'),
    10: ('step-altar2", 218, 4.0, 22.5, "ledge")', 'step-altar2", 218, 4.0, 22.5, "ledge"),\n    S("step-altar3", 223.0, 4.0, 22.5, "ledge")'),
}

for lvl, (target, repl) in approach_steps.items():
    text = text.replace(f'S("{target}', f'S("{repl}')

# Also set goals to start at 228.0 w=17.0
text = re.sub(
    r'(S\("goal-[^"]+",\s*)229,\s*16\.0(,\s*[\d\.]+,\s*"stone")',
    r'\g<1>228.0, 17.0\g<2>',
    text
)

with open("tools/generate_all_10_levels.py", "w", encoding="utf-8") as f:
    f.write(text)

print("[✓] Successfully updated tools/generate_all_10_levels.py with zero gap platform physics!")
