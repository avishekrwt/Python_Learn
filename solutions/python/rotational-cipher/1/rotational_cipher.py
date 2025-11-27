def rotate(text_string, key):
    text = list(text_string)
    offset = 0
    for i in range(len(text)):
        if text[i].isalpha():
            text_ascii = ord(text[i])
            if text[i].islower():
                offset = ord('a')
            if text[i].isupper():
                offset = ord('A')
            new_char = chr((text_ascii - offset + key) % 26 + offset)
            text[i] = new_char

    return ''.join(text)