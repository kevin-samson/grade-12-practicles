"""
find the frequnecy of words

"""
import collections

with open('texts.txt', 'r') as f:
    data = f.read()


wordlist = {}

for i in data.lower().split():
    i = i.replace('.', '')
    i = i.replace('!', '')
    if i not in wordlist:
        wordlist[i] = 1
    else:
        wordlist[i] += 1

num = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(num))
word_counter = collections.Counter(wordlist)
for word, count in word_counter.most_common(num):
    print(word, ": ", count)

