'''
Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

- it should accept exactly one argument - a string;
- it should return a list of words created from the string, divided in the places where the string contains whitespaces;
- if the string is empty, the function should return an empty list;
its name should be mysplit()

Use the given template. Test your code carefully.

def mysplit(strng):
   #
   # put your code here
   #


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    
Expected Output:
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
[]
['abc']
[]
'''

###############################################################

#python code

def mysplit(strng):
   val = strng.strip()
   a = []
   if len(val)  == 0 or val.isspace():
     return a
   word = "" 
   for i in val:
      if not i.isspace():
         word += i
      else:
         a.append(word)
         word = ''
   else:
      a.append(word)
   return a
    
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print(mysplit("hello there, my name is Samip Shah and this is my own split function."))