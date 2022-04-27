"""
ATTENTION
THIS CODE IS NO LONGER BEING WORKED ON, SO IT MAY STILL HAVE SOME BUGS HERE AND THERE!
"""
# Welcome to my Python calculator!
# It currently supports Exponentiation, Multiplication, Division (with optional remainders)
# Addition, Substraction, and checking for equalities. This includes one-line input!
# If you have anyting to say, please leave it in the comment section so that I can review it :-)
# If you copy this in any way or edit it for reposting, please leave a comment saying that you did (with a link), so that I know about it :-)
# Version log and other information about this program at the bottom the code

from math import sqrt as squart
from math import pi
print("""/---------------------------------------------------------------\\\n|          Pritam's Python Calculator - Version 1.7.2          |""")
print("""|---------------------------------------------------------------|
| Seperate all different input with a SPACE. First off, the 1st |
| number. Next, one of symbols below. Lastly, the 2nd number.   |
| Exponentiation is '^'                                         |
| Multiplication is '*'                                         |
| Division is '/'                                               |
| Addition is '+'                                               |
| Substraction is '-'                                           |
| Checking Equality is '_'                                      |""")
print("""|---------------------------------------------------------------|
| NOTE: When dividing, If you want a remainder instead of an    |
|       'infinite' number, write 'yes' ON ANOTHER LINE.         |
| NOTE: The '≈' are just there in case Python cannot handle     |
|       the lenght of a number. In most cases, your result      |
|       will be exact. Decimals over 15 digits will be cut.     |
\\---------------------------------------------------------------/\n""")
wantremain = " "
try:
    num1,action,num2 = input("Enter your input: ").split()
    num1 = float(num1)
    action = str(action)
    num2 = float(num2)
    if action == "/":
        try:
            wantremain = input("(Y/N) Do you want a remainder? ")
        except EOFError:
            pass
        else:
            pass
except EOFError:
    pass
except ValueError:
    quit("""ValueError\n
Maybe one of the following occured:
  - You added things after your equation
    - Do not go farther than three variables
  - You forgot to put a space between arguments
  - You didn't make the numbers integers/floats
    - Make sure that there aren't any letters
  - There's something you didn't fill in
  - There is an error in the code (report the issue in the comments)
  
Here are some tips - with 'X' being any number,
'+' being any symbol, and '>>>' symbolyzing a new line:

A correct input would be as follows:
>>> X + X

When dividing, if you want a remainder,
do as follows ('Yes' can also be 'yes')
>>> X / X
>>> Yes
Otherwise, you don't need to write 'no,' you can just leave it blank
""")
else:
    pass
# The following line is useless for the program, it just lists the variables before the equation actually happens. This just helps with the development of the calculator:
#print("Num1: " + str(num1) + "\nAction: " + str(action) + "\nNum2: " + str(num2) + "\n")
def firstnum():
    print("\nYour first number is " + str(num1))
def secondnum():
    print("Your second number is " + str(num2) + "\n")
def symbol(word):
    print("Your action is to " + str(word))
if action == "+":
    firstnum()
    symbol("add (+)")
    secondnum()
    print(str(num1) + " + " + str(num2) + " ≈ " + str(num1 + num2))
elif action == "-":
    firstnum()
    symbol("substract (-)")
    secondnum()
    print(str(num1) + " - " + str(num2) + " ≈ " + str(num1 - num2))
elif action == "*":
    firstnum()
    symbol("multiply (*)")
    secondnum()
    print(str(num1) + " • " + str(num2) + " ≈ " + str(num1 * num2))
elif action == "/":
    firstnum()
    symbol("divide (/)")
    secondnum()
    try:
        num1 / num2
    except ZeroDivisionError:
        quit("ZeroDivisionError:\nIt seems that you tried to divide a number by zero, which is not possible.\n")
    else:
        remainder = num1 % num2
        fullnum1 = num1 - remainder
        if wantremain == "yes":
            print(str(num1) + " ÷ " + str(num2) + " = " + str(fullnum1 / num2) + "\nWith a remainder of: " + str(remainder))
        elif wantremain == "Yes":
            print(str(num1) + " ÷ " + str(num2) + " = " + str(fullnum1 / num2) + "\nWith a remainder of: " + str(remainder))
        elif wantremain != "yes":
            print(str(num1) + " ÷ " + str(num2) + " ≈ " + str(num1 / num2))
        else:
            quit("Your remainder choice was not recognised, try again with either an empty line, 'no,' or 'yes.\n'")
elif action == "^":
    firstnum()
    symbol("exponentiate (^)")
    secondnum()
    print(str(num1) + " ^ " + str(num2) + " ≈ " + str(num1 ** num2))
elif action == "_":
    firstnum()
    symbol("check the equality of these two numbers (_)")
    secondnum()
    if num1 > num2:
        print(str(num1) + " > " + str(num2))
    elif num1 < num2:
        print(str(num1) + " < " + str(num2))
    elif num1 == num2:
        print(str(num1) + " = " + str(num2))
    else:
        quit("There has been an error checking the equality of " + str(num1) + " and " + str(num2) + ".\nTry again to see if the issue has been fixed\nIf the issue persists, write a comment describing it so that may be resolved.")
else:
    quit("""Your action was not recognised, try again and see if it is fixed.
Try spelling everything correcly, and make sure to check the case-sensitive options.
    
If you did everything correctly, then there has been an unexpected error.
Try using the calculator again and see if the issue is still there.
If the issue persists, contact AnonymaCoding via the comment section.
Don't forget to describe it, that way it can be fixed properly.
Thanks!
""")
print("\nThanks for using this calculator!\nLeave a comment if you have any ideas or \nwant to report a bug, it really helps a lot!\n")

# ----------- Updates Log ----------- #
# BETA1 - Added Addition, Substraction, and Multiplication
# BETA2 - Added Division
# 1.1.0 - Added ZeroDivisionError 'quit' message
# 1.2.0 - Swapped the first three letters of actions with symbols (eg: 'add' becomes '+')
#   1.2.1 - Added Version Log with previous versions included
#   1.2.2 - Added message at the end (does not pop up if exceptions appear)
#   1.2.3 - Fixed grammar, spelling errors, and overall English
#   1.2.4 - Added ValueError 'quit' message/pass if no error
# 1.3.0 - Added Exponentiation, reorganized actions in lines 12-16 as PEMDAS, added '≈' in case of long numbers
# 1.4.0 - Added a remainder option for division, added option message on lines 18-21 and added 'quit' message if wantremain is wrongly defined
#     1.4.1 - Changed some messages (including error messages)
# 1.5.0 - Added one line input, fixed title box to have the right message
#   1.5.1 - Added 'extra' variable in case someone adds anything after 'num2'
#   1.5.2 - Added option for an empty line for 'wantremain'
#   1.5.3 - Changed 'ValueError' Message to list some example of common errors + tips
#   1.5.4 - Fixed indentation errors
#   1.5.5 - Removed 'extra' as it caused ValueErrors
# 1.6.0 - Turned print actions into functions for better code organization
# 1.7.0 - Added equalities
#   1.7.1 - Fixed prompts
#   1.7.2 - Fixed remainder prompt to only appear if action is '/'
# ------ CURRENT VERSION 1.7.2 ------ #

# ------- Undeveloped Updates ------- #
# - Suggestions from the comments:
#    - Currently none
# ------- Undeveloped Updates ------- #

# -------- BY ANONYMA CODING -------- #
" www.sololearn.com/Profile/11574076 "
# -------- BY ANONYMA CODING -------- #


