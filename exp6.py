import random

while True:
    print("1.Roll a die")
    print("0. to stop")
    ch = int(input("Enter the option "))
    if ch == 1:
        print(random.randrange(1, 6))
    if ch == 0:
        break
    else:
        print("Invalid option")
