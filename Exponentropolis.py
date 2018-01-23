import math

## Julia's Exponent Program
print("\n This is Julia's Explonent-Tropolis Program \n")
base = input("BASE:  ")
exponent = input("EXPONENT:  ")

#  X^Y - in computer language - the ** is the exponent sign (not ^ like in R)

##result = (base)**(exponent)
result = math.pow(base,exponent)


print("\n The result is: ", result)
