def letter_counter(text):
    text = text.lower()
    ret = {}

    for n in text:
        try:
            ret[n] += 1
        except KeyError:
            ret[n] = 1
    return ret


print(letter_counter('Katarzyna'))
