import json
import re

with open('text_normalized.txt', encoding='utf-8') as f:
    lines = f.read().split('\n')

dict_words = {}

for line in lines:
    words = line.split(' ')
    for i in range(len(words) - 1):
        v = re.sub(r'\\?n$', '',  words[i + 1])
        if words[i] not in dict_words:
            dict_words[words[i]] = [v]
        elif v not in dict_words[words[i]]:
            dict_words[words[i]].append(v)

with open('model.json', 'w', encoding='utf-8') as f:
    json.dump(dict_words, f, indent=2, ensure_ascii=False)
