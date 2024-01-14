'''
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:
- asks the user for two separate texts;
- checks whether, the entered texts are anagrams and prints the result.

Note:
- assume that two empty strings are not anagrams;
- treat upper- and lower-case letters are equal;
- spaces are not taken into account during the check - treat them as
  non-existent
  
'''

########################################################################

# pyhton code to check anagrams

text1 = input("enter first test:\t")
text2 = input("enter second test:\t")

def check_anagram(text1,text2):
  
  # removing spaces
  text1 = text1.replace(" ","")
  text2 = text2.replace(" ","")
  
  #checking for empty string and the length of string is equal or not
  if len(text1) * len(text2) > 0 and len(text1) == len(text2):
    
    # traversing through all the elements present
    for letters in text1.uppercase() + text2.uppercase():
      
      # All the letters must be present in both the texts
      if letters not in text1.uppercase() or letters not in text2.uppercase():
        print("not an anagram")
        break
    else:
      print("anagram")
  else:
    print("not an anagram")


check_anagram(text1,text2)


# Alternative:

text1 = input("enter first test:\t")
text2 = input("enter second test:\t")

# removing spaces
text1 , text2 = text1.replace(' ','') , text2.replace(' ','')

# converting letters to uppercase and changing string to list
list1 , list2 = list(text1.upper()) , list(text2.upper())


# sorting the lists
list1.sort()
list2.sort()

if len(list1) > 0 and list1 == list2:
  print("anagram")
else:
  print("not an anagram")