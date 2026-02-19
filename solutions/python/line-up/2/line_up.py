def line_up(name, number):
    num = number%100
    rank = 'th'
    if num%10 == 1 and num != 11:
        rank = 'st'
    if num%10 == 2 and num != 12:
        rank = 'nd'
    if num%10 == 3 and num != 13:
        rank = 'rd'
    return f"{name}, you are the {number}{rank} customer we serve today. Thank you!"