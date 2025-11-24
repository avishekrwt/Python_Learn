def is_armstrong_number(number):
    numerical = str(number)
    power = len(numerical)
    total = 0
    for num in numerical:
        total += int(num) ** power

    return total == number