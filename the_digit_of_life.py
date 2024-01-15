'''
        LAB: The Digit of Life

Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more then one digit, you have to repeat the addition until you get exactly one digit. For example:
- 1 January 2017 = 2017 01 01
- 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
- 1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:
- asks the user her/his birthday (in the   format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
- outputs the Digit of Life for the date.

sample input: 19991229
sample output: 6
sample input: 20000101
sample output: 4
'''

# Python code to find the Digit of Life using strings

DOB = input("enter your birth date in YYYYMMDD format:\t")
if len(DOB) == 8 and DOB.isdigit():
    while len(DOB) > 1: 
        digitOfLife = 0
        for digits in DOB:
            digitOfLife += int(digits)
        else:
            DOB = str(digitOfLife)
    else:
        print(digitOfLife)
else:
    print("Invalid Format")
    
    
    
# Alternative: Python code to find Digit of Life using mathematics tricks ;)

def digit_of_life(DOB):
 
    if (DOB == 0):
        return 0
    elif (DOB % 9 == 0):
        return 9
    else:
       return (DOB % 9)

 
# Driver program to test the above function
DOB = input("enter your birth date in YYYYMMDD format:\t")
if len(DOB) == 8 and DOB.isdigit():
    print(f'Your Digit of Life is: {digit_of_life(int(DOB))}')
else:
    print("Invalid Format")