import random
import os

from collections import defaultdict


def generate_markov_table(text):

    table = defaultdict(lambda: defaultdict(int))
    text_length = len(text)

    for i in range(text_length - 4):
        key = text[i: i + 4]
        count = text[i + 4: i + 8]
        table[key][count] += 1
    return table


def generate_markov_text(length, table):

    keys = list(table.keys())
    output = []
    char = None

    for i in range(round(length / 4)):
        if char is None:
            char = random.choice(keys)
        d = table[char]

        new_char = get_weighted_char(d)

        if new_char:
            char = new_char
            output.append(new_char)

    return "".join(output)


def get_weighted_char(d):
    if not d:
        return None
    total = sum(d.values())
    score = random.randint(1, total)
    for char, weight in d.items():
        if score <= weight:
            return char
    return None


if __name__ == "__main__":

    source = []
    lyrics_dir = os.path.join(os.path.dirname(__file__), "lyrics")
    for filename in os.listdir(lyrics_dir):
        source.append(open(os.path.join(lyrics_dir, filename)).read())
    table = generate_markov_table("".join(source))
    text = generate_markov_text(2000, table)
    print(text)
