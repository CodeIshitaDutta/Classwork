import math

test = int(input("how many tests?  "))
pi_val = math.pi
radius = 40075/(2*pi_val)

for i in range(test):
    distance = int(input("enter distance from earth in km "))
    t_radius = radius + distance
    circumference = (2*pi_val * t_radius)
    circumference = round(circumference, 1)
    print(circumference)
