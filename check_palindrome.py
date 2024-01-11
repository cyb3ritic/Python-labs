'''
Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:
- asks the user for some text;
- checks whether the entered text is a palindrome, and prints the result.

Note:
- assume that an empty string isn't a palindrome;
- treat upper- and lower-case letters as equal;
- spaces are not takes into account during the check - treat them as
  non-existent;
- there are more than a few correct solutions - try to find more than one

'''

# Python code to check palindrome

text = input("enter the text you want to check:\t")

# remove all the spaces
text = text.replace(' ','')

# check if word is equal to its reverse
if len(text) > 0 and text.lower() == text[::-1].lower():
    print("It's a palindrome")
else:
    print("It's not a palindrome")
    
