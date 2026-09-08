def is_valid_triangle(sides):
    if 0 in sides:
        return False
    
    return (sides[0] + sides[1] >= sides[2] 
            and sides[1] + sides[2] >= sides[0] 
            and sides[0] + sides[2] >= sides[1])

def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    return len(set(sides)) == 1

def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    
    return len(set(sides)) <= 2

def scalene(sides):
    if not is_valid_triangle(sides):
        return False

    return len(set(sides)) == 3