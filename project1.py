#printing in terminal to check the outcome of 'str' and 'int'
print('Hello, World!')
print(100)

#to check what type of values
type('Hello, World!')
type(25)
type(3.2)
type('10')
type('3.2')

#veriables
message='and now for different World'
pi=3.1415926535897931
n=17
cool=pi+n
print(cool)	

#The type of a variable is the type of the value it refers to
type(message)
type(pi)
type(n)

"""The operators +, -, *, / and ** perform addition, subtraction, multiplication, division and exponentiation, as in the following examples:
20+32 
hour-1 
hour*60+minute minute/60 
5**2 
(5+9)*(15-7)

Arthametic operation happens from left to right
PEMDAS

order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.

"""

#some time we need to use backlash to skip over single quote
'this isn\'t the case for keep over backlash'

#String methods
len()
lower()
upper()
str()

	parrot="Norwegian Blue"
print len(parrot)

	parrot = "Norwegian Blue"

print parrot.lower()

	parrot = "norwegian blue"

print parrot.upper()

	"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi=3.14
print str(pi)



# meal calculater

meal=45
tax=12/100
meal=meal+meal*tax
tip=15/100
total=meal+meal*tip
print (total)
57.96


control following

def using_control_once():
    if 5>=5:
        return "Success #1"

def using_control_again():
    if 10>9:
        return "Success #2"

print using_control_once()
print using_control_again()		
		
def clinic():
	print "You've just entered the clinic!"
	print "Do you take the door on the left or the right?"
	answer = raw_input("Type left or right and hit 'Enter'.").lower()
	if answer == "left" or answer == "l":
	    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
	elif answer == "right" or answer == "r":
	    print "Of course this is the Argument Room, I've told you that already!"
	else:
	    print "You didn't pick left or right! Try again."
	    clinic()

	clinic()

# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if (10>=9) or (9>=10):    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
        return True
    elif (10>=9) and (9>=10):
        # Keep going here.
        # You'll want to add the else statement, too!
        return False
    
    print the_flying_circus()


name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is ___, your quest is ___, " \
"and your favorite color is ___." ___ (name, quest, color)

from datetime import datetime
now=datetime.now()
print now

from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)

from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)

from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

Equal to (==)
02. Not equal to (!=)
03. Less than (<)
04. Less than or equal to (<=)
05. Greater than (>)
06. Greater than or equal to (>=)

# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False


#Pig Latin Translater

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original=raw_input("Enter a word:")
if len(original)>0 and original.isalpha():
    print (original)
else:
    print "empty"

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word=original.lower()
    first=word[0]
    new_word=word+first+pyg
    new_word=new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'
    
#this is all about functions

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
