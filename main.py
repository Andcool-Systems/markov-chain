import random
import json

with open('model.json', 'r', encoding='utf-8') as f:
    dict_words = json.load(f)


def generate(length: int, allow_context_skip: bool) -> str:
    random_start_pair = random.choice(list(dict_words.items()))
    generated = [random_start_pair[0], random.choice(random_start_pair[1])]

    i = 0
    while i < length:
        if generated[-1] in dict_words:
            generated.append(random.choice(dict_words[generated[-1]]))
        elif allow_context_skip:
            for error in range(len(generated) - 1, 0):
                if generated[error] in dict_words:
                    generated.append(random.choice(dict_words[generated[-1]]))
                    break
            break
        else:
            random_start_pair = random.choice(list(dict_words.items()))
            generated = [random_start_pair[0],
                         random.choice(random_start_pair[1])]
            i = length
        i += 1
    return ' '.join(generated)


print(generate(50, True))
