def find_anagrams(org_word, candidates):
    expected = []
    for words in candidates:
        candidate_word = words.lower()
        test_word = org_word.lower()

        if sorted(candidate_word)==sorted(test_word) and candidate_word != test_word:
            expected.append(words)
    return expected