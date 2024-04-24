test = int(input("how many tests?  "))

for i in range(test):
    information = input("Enter 1-inch, 5-inch, and target length.")
    information = information.split()
    one = int(information[0])
    five = int(information[1])
    target = int(information[2])
    length = (one)+(five*5)
    print (length)
    if length == target:
        goal = "true"
    else:
        goal = "false"
    print (goal)
