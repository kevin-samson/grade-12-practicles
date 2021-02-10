"""
input roll number and update marks
"""
import pickle


def Write(roll, name, marks):
    with open('binary.ni', 'ab') as f:
        srecord = {"roll": roll, "name": name, "marks": marks}
        pickle.dump(srecord, f)


def Read():
    with open('binary.ni', 'rb') as f:
        print("\nRoll No.", ' ', 'Name', '\t', end='')
        print('Marks')
        while True:
            try:
                rec = pickle.load(f)
                print(' ', rec['roll'], '\t  ', rec['name'], '\t ', end='')
                print(rec['marks'])
            except EOFError:
                break


def Input():
    n = int(input("How many records you want to create :"))
    for ctr in range(n):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Percentage: "))
        Write(roll, name, marks)


def Modify(roll):
    with open('binary.ni', 'rb') as f:
        newRecord = []
        while True:
            try:
                rec = pickle.load(f)
                newRecord.append(rec)
            except EOFError:
                break
    found = 1
    for i in range(len(newRecord)):
        if newRecord[i]['roll'] == roll:
            name = input("Enter Name: ")
            marks = float(input("Enter Percentage: "))

            newRecord[i]['name'] = name
            newRecord[i]['marks'] = marks
            found = 1
        else:
            found = 0

    if found == 0:
        print("Record not found")
    with open('binary.ni', 'wb') as f:
        for j in newRecord:
            pickle.dump(j, f)


while True:
    print('\nYour Choices are: ')
    print('1.Insert Records')
    print('2.Dispaly Records')
    print('3.Update Records')
    print('0.Exit (Enter 0 to exit)')
    ch = int(input('Enter Your Choice: '))
    if ch == 1:
        Input()
    elif ch == 2:
        Read()
    elif ch == 3:
        r = int(input("Enter a Rollno to be update: "))
        Modify(r)
    else:
        break
