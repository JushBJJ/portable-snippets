"""
Freedom of input snippet for windows systems. To exit, press q. 

With this program, this will translate both the ascii value and undecoded 
value of whatever is pressed in the keyboard. 

Docs: https://docs.python.org/3/library/msvcrt.html
"""

import msvcrt as msv
import string

essential_keys={
	"H":"Up Arrow",
	"P":"Down Arrow",
	"K":"Left Arrow",
	"M":"Right Arrow"
}

# Function keys, delete key can be suppported. 

normal_keys=string.printable
special_keys=(b"\x00", b"\xe0")

def input_socket():
	while True:
		key=msv.getch()
	
		if key in special_keys:
			key=msv.getch().decode()
			key=essential_keys[key]
			print(key)

		else:
			key=key.decode()
			if key in normal_keys:
				if key=="q": # Exit
					return key
				else:
					print(key)
			else:
				# For other key presses like ctrl+c
				print("Decoded: ", key)
				print("Encoded: ", key.encode())
				
def fully_free_input():
	# You must kill this program to stop it from getting keybaord input.
	while True:
		print(msv.getch())

if __name__=="__main__":
	print("Exit: ", input_socket()) # do fully_free_input for free flow input
