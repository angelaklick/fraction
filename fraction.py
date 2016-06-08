def multiply(fraction1, fraction2):
    numerator = fraction1[0] * fraction2[0]
    denominator = fraction1[1] * fraction2[1]

    total = (numerator, denominator)

    
    return total


print(multiply((2,1),(4,5)))


def add(fraction1, fraction2):
    n = fraction2[0]* fraction1[1]
    n2 = fraction1[0] * fraction2[1]
    numerator = n + n2
    denominator = fraction1[1] * fraction2[1]
    

    total = (numerator, denominator)

    
    return total


print(add((2,5),(2,1)))
