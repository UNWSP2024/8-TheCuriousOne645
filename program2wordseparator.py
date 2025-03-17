def separate_words(sentence):
    result = sentence[0]
    for char in sentence[1:]:
        if char.isupper():
            result += ' ' + char.lower()
        else:
            result += char
    return result
