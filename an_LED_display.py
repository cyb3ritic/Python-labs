'''
You've surely seen a seven-segment display.

Your task is to write a program which is able to simulate the work of a seven-segment display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

  #  ###  ###  # #  ###  ###  ###  ###  ###  ###
  #    #    #  # #  #    #      #  # #  # #  # # 
  #  ###  ###  ###  ###  ###    #  ###  ###  # # 
  #  #      #    #    #  # #    #  # #    #  # # 
  #  ###  ###    #  ###  ###    #  ###  ###  ###

Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpfull
 
'''

# Python code to simulate seven-segment display

digits = [
    '1111110',  # 0
    '0110000',	# 1
    '1101101',	# 2
    '1111001',	# 3
    '0110011',	# 4
    '1011011',	# 5
    '1011111',	# 6
    '1110000',	# 7
    '1111111',	# 8
    '1111011',	# 9
]


def setLEDs(num):
	global digits
	dgt = str(num)
	lines = [ '' for lin in range(5) ]
	for d in dgt:
		LEDs = [ [' ',' ',' '] for lin in range(5) ]
		pattern = digits[int(d)]
		if pattern[0] == '1':
			LEDs[0][0] = LEDs[0][1] = LEDs[0][2] = '#'
		if pattern[1] == '1':
			LEDs[0][2] = LEDs[1][2] = LEDs[2][2] = '#'
		if pattern[2] == '1':
			LEDs[2][2] = LEDs[3][2] = LEDs[4][2] = '#'
		if pattern[3] == '1':
			LEDs[4][0] = LEDs[4][1] = LEDs[4][2] = '#'
		if pattern[4] == '1':
			LEDs[2][0] = LEDs[3][0] = LEDs[4][0] = '#'
		if pattern[5] == '1':
			LEDs[0][0] = LEDs[1][0] = LEDs[2][0] = '#'
		if pattern[6] == '1':
			LEDs[2][0] = LEDs[2][1] = LEDs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(LEDs[lin]) + '\t'
	for lin in lines:
		print(lin)


setLEDs(int(input("Enter the number you wish to display:\t")))
    
    
