import re

def normalize(string):
    remove_non_words = re.compile(r"[^\w\s]+")

    temp = string.lower()

    temp =  remove_non_words.sub(" ", temp)

    temp = re.sub(r"\s+", " ", temp)

    return temp
