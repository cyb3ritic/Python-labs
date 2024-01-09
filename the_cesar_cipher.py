'''
The task is to write a program to encode a message using cesar cipher concept. You need to ask user by how many places they wist to rotate the letters and print the encrypted message.

for example:
    if its ROT13:
    
    input  ==> This is an example for ROT_13
    
    output: ==> Guvf vf na rknzcyr sbe EBG_13

'''

# Python code for cesar cipher

message = input("Enter your message here:\t")
rot = int(input("By how many do you wish to rotate yout message?\t"))
rot %= 26      # binding down the value of rot to 0 to 26
cipher = ''
for char in message:
    
    # if it's alphabet, then only we are going to rotate it.

    if char.isalpha():
        
        # For upper case characters
        if char.isupper():
            if (ord(char) + rot) <= ord('Z'):
                cipher += chr(ord(char) + rot)
            else:
                cipher += chr(ord('A') + (ord(char) + rot) % ord('Z') - 1)
        
        # For lower case characters        
        elif char.islower():
            if (ord(char) + rot) <= ord('z'):
                cipher += chr(ord(char) + rot)
            else:
                cipher += chr(ord('a') + (ord(char) + rot) % ord('z') - 1)
        
    else:  # if the character is not alphabet, it will get concatenated as it it
        cipher += char    
            
print (cipher)    # Printing the final encrypted message