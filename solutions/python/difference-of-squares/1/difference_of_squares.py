def square_of_sum(number):
    sum = number*(number+1)//2
    return sum**2

def sum_of_squares(number):
    sum = number*(number + 1)*(2 * number + 1)//6
    return sum

def difference_of_squares(number):
    sq_of_sum = square_of_sum(number)
    sum_of_sq = sum_of_squares(number)
    return sq_of_sum - sum_of_sq
