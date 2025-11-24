def steps(number):
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number!=1:
        counter += 1
        number = collatz(number)
        
    return counter
    
def collatz(number):
    if number%2==0:
        return number//2
    return ((number*3)+1)