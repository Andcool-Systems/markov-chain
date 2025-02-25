import re

splitters = r"[.;!?]"
allowed_chars = r'0-9a-zA-Zа-яА-ЯёЁ\s\-:\<>\[\]\{\}\+\-=\/*\\'

with open('text.txt', encoding='utf-8') as f:
    lines = f.readlines()

lines_normalized = []
for line in lines:
    result = re.split(splitters, line)
    result = list(filter(None, result))
    clear = [
        re.sub(fr'[^{allowed_chars}]', '', s).strip().lower()
        for s in result
    ]
    clear = [re.sub(r'\\?n', '', s) for s in clear]
    lines_normalized.extend(clear)

with open('text_normalized.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(filter(None, lines_normalized)))
