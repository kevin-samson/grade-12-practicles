"""Read a text file line by line and display each word separated by a #
"""
with open('texts.txt', 'r') as f:
    the_lines = f.readlines()

for i in the_lines:
    words = i.split(" ")
    for word in words:
        print(word+"#", " ")
