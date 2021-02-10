"""
remove all the a
"""
lines_without_letter_a = []
with open('texts.txt', 'r') as f:
    the_lines = f.readlines()

for i in the_lines:
    if 'a' not in i:
        lines_without_letter_a.append(i)

with open('No letter a.txt', 'w') as f:
    print("file created")
    for i in lines_without_letter_a:
        f.write(i)
        
