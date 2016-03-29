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

		#The operators +, -, *, / and ** perform addition, subtraction, multiplication, division and exponentiation, as in the following examples:
		#20+32 
		#hour-1 
		#hour*60+minute minute/60 
		#5**2 
		#(5+9)*(15-7)
		#PEMDAS

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
