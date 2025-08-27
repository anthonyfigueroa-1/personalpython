from collections import Counter

def counter(tokens, top_x):
    unique_words = 0
    count = Counter(tokens)
    for t in count:
        unique_words += 1
    top = count.most_common(top_x)
    return top, unique_words
