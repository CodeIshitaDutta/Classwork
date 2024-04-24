test = int(input("how many tests?  "))

for i in range(test):
    information = input("enter speed and if it is your birthday  ")
    information = information.split()
    speed = int(information[0])
    b_day = information[1]
    if b_day == "false":
        if speed <= 60:
            alert = "no ticket"
        if 61 <= speed <= 80:
            alert = "small ticket"
        if 81 <= speed:
            alert = "big ticket"
    if b_day == "true":
        if speed <= 65:
            alert = "no ticket"
        if 66 <= speed <= 85:
            alert = "small ticket"
        if 86 <= speed:
            alert = "big ticket"
    print (alert)
