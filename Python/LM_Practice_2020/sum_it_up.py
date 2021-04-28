test_cases = int(input("How many test cases?  "))

for i in range(test_cases):
    numbers = input ("put in two numbers: ")
    numbers = numbers.split()
    val_a = int(numbers[0])
    val_b = int(numbers[1])
    total  = val_a + val_b
    if val_a == val_b:
        total = total * 2
    print (total)
