def equilateral(sides):
    if 0 not in sides:
        if sides[0]+sides[2]>=sides[1]:
            return sides[0]==sides[1] and sides[1]==sides[2]
    return False

def isosceles(sides):
    if 0 not in sides:
        if sides[0]==sides[1]:
            return sides[0]+sides[1]>=sides[2]
        if sides[1]==sides[2]:
            return sides[1]+sides[2]>=sides[0]
        if sides[0]==sides[2]:
            return sides[0]+sides[2]>=sides[1]

    return False

def scalene(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0: return False
    if a + b <= c or a + c <= b or b + c <= a: return False
        
    return a != b and b != c and a != c


    