def is_pangram(sentence):
    sentence = sentence.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    test_set = set()
    for char in sentence:
        if char in alpha:
            test_set.add(char)

    alphabets = set(alpha)
    return alphabets==test_set