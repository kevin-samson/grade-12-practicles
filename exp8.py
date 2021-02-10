front = rear = 0


def isEmpty(lst):
    if len(lst) == 0:
        return True
    else:
        return False


def DoPush(lst, name):
    lst.append(name)
    if len(lst) == 0:
        front = rear = 0
    else:
        rear = len(lst) - 1


def DoPop(lst):
    if isEmpty(lst):
        return "Underflow"
    else:
        val = lst.pop(0)
    if len(lst) == 0:
        front = rear = None
    return val


def peek(lst):
    if front is None:
        return "no elements"
    else:
        print(lst[front])


def main(names):
    ans = input("Push or Pop or display list (display) or peek")
    if ans == "push":
        name = input("Enter the name:-")
        DoPush(names, name)
    elif ans == "pop":
        print(DoPop(names))
    elif ans == "display":
        print(names)
    elif ans == "peek":
        print(peek(names))
    else:
        print("Invalid option")


nameslst = []

while True:
    main(nameslst)
    cont = input("Do you want to proceed")
    if cont == "yes":
        continue
    else:
        break
