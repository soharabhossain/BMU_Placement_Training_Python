
# Python program to demonstrate Command-Line arguments
# This script is saved fith the following name: cmdarg.py 
 
import sys
 
# Total arguments
n = len(sys.argv)
print("\n Total arguments passed:", n)
 
# Arguments passed
print("\n Name of Python script:", sys.argv[0])
 
print("\n Arguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0

# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\n Result (sum of all the arguments) : ", Sum)

