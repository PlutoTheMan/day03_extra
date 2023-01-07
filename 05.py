def find_first_duplicate(text):
    text = text.lower()
    slownik = {}

    for n in text:
        try:
            slownik[n] += 1
            return n
        except KeyError:
            slownik[n] = 1

    return None


print(find_first_duplicate('Makumba'))
