"""
Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in a file
"""
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
v = set("AEIOUaeiou")
c = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")


with open('texts.txt', 'r') as f:
    the_lines = f.readlines()

for i in the_lines:
    words = i.split(" ")
    for word in words:
        for letter in word:
            if letter in v:
                vowels += 1
            elif letter in c:
                consonants += 1
        if word.isupper():
            uppercase += 1
        elif word.islower():
            lowercase += 1

print("vowels = ",vowels)
print("consonants = ",consonants)
print("uppercase = ",uppercase)
print("lowercase = ",lowercase)
