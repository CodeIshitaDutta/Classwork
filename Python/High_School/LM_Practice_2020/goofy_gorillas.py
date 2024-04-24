tests = int(input("how many test cases?  "))

for i in range(tests):
    gorillas = input("enter smile factor for both gorillas:  ")
    gorillas = gorillas.split()
    g_one = gorillas[0]
    g_two = gorillas[1]
    if g_one == g_two:
        alert = "true"
    else:
        alert = "false"
    print(alert)
