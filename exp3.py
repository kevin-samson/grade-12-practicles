"""
Create a binary file with name and roll number. Search for a given roll number and display the name,
if not found display appropriate message
"""
import pickle


def Insert(roll, name):
    with open('binary.ni', 'ab') as f:
        data = {"roll": roll, "name": name}
        pickle.dump(data, f)
        print(f"{name} with {roll} is inserted")


def Read():
    with open('binary.ni', 'rb') as f:
        print("\nRoll No.", ' ', 'Name', '\t', end='')
        print()
        while True:
            try:
                rec = pickle.load(f)
                print(' ', rec['roll'], '\t  ', rec['name'])
            except EOFError:
                break


def Search(roll):
    with open('binary.ni', 'rb') as f:
        while True:
            try:
                data = pickle.load(f)
                if data['roll'] == roll:
                    print("Roll NO:", data['roll'])
                    print("Name:", data['name'])

            except EOFError:
                break


while True:
    print('\nYour Choices are: ')
    print('1.Insert Records')
    print('2.Dispaly Records')
    print('3.Search Records (By Roll No)')
    print('0.Exit (Enter 0 to exit)')
    ch = int(input('Enter Your Choice: '))
    if ch == 1:
        roll = input("Enter the roll no")
        name = input("Enter the name")
        Insert(roll, name)
    elif ch == 2:
        Read()
    elif ch == 3:
        r = int(input("Enter a Rollno to be Search: "))
        Search(r)
    else:
        break
