'''
        LAB: Find A Word
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to wirte a program which answers the following question: are the characters comprising the first string hidden inside the second string?

For example:
- if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
- if the second string is "vcxzxduybfdsobywuefsas", the answer is no (as the letters "d". "o", or "g" don't appear in this order)

Hints:
- you should use the two argument variants of the pos() functions inside your code;
- don't worry about case senstiity

Sample input :  donor
                Nabucodonosor
Sample output:  Yes

Sample input :  donut
                Nabucodonosor
Sample output:  No


'''

# Python code 

word = list(input("enter a word:\t").upper())
text = list(input("enter combination of any character as text:\t").upper())
test = []

for i in word:
    if i in text:
        test.append(i)
        text = text[text.index(i):]
        continue

if str(test) == str(word):
    print("Yes")
else:
    print("NO")
    
    
# Alternative

word = input("Enter a word:\t")
text = input("Enter combination of any character as text:\t")

found = True
start = 0

for letters in word:
    pos = text.find(letters,start)
    if pos < 0:
        found = False
        break
    start = pos + 1

if found:
    print("Yes")
else:
    print("No")
    
        
