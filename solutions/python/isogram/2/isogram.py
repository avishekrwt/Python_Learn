def is_isogram(string):
    string = string.lower()
    aphabets = set()
    for char in string:
        if char.isalpha() and char not in aphabets:
            aphabets.add(char)
        elif char.isalpha() and char in aphabets:
            return False

    return True      