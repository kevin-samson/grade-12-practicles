def isEmpty(lst):
    if len(lst) == 0:
        return True
    else:
        return False


def Enqueue(lst, val):
    lst.append(val)
    if len(lst) == 1:
        front = rear = 0
    else:
        rear = len(lst) - 1


def Dequeue(lst):
    if isEmpty(lst):
        return "UnderFlow"
    else:
        val = lst.pop(0)
    if len(lst) == 0:
        front = rear = None
    return val


def Peek(lst):
    if isEmpty(lst):
        return "UnderFlow"
    else:
        front = 0
        return lst[front]


def Display(lst):
    if isEmpty(lst):
        print("No Item to Dispay in Queue....")
    else:
        tp = len(lst) - 1
        print("[FRONT]", end=' ')
        front = 0
        i = front
        rear = len(lst) - 1
        while i <= rear:
            print(lst[i], '<-', end=' ')
            i += 1
        print()


lst = []
front = rear = 0
while True:
    print()
    print("1. ENQUEUE ")
    print("2. DEQUEUE ")
    print("3. PEEK ")
    print("4. DISPLAY ")
    print("0. EXIT ")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        ele = int(input("Enter element to insert"))
        Enqueue(lst, ele)
    elif choice == 2:
        val = Dequeue(lst)
        if val == "UnderFlow":
            print("Queue is Empty")
        else:
            print("\n Deleted Element was : ", val)

    elif choice == 3:
        val = Peek(lst)
        if val == "UnderFlow":
            print("Queue is Empty")
        else:
            print("Item at Front: ", val)

    elif choice == 4:
        Display(lst)
    elif choice == 0:
        print("Good Luck......")
        break
