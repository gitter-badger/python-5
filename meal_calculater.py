# meal price calculater

#stage 1

meal=input("what is the price of the meal?")
meal=int(meal)
tax=input("what is the percent of tax on meal?(only number)")
tax=int(tax)
tax=tax/100
meal_plus_tax=meal+meal*tax

print ("price of meal plus tax Rs "+ str(meal_plus_tax))

#stage 2

dude=input("did you pay tip to the waiter?")

if  dude=="yes"or dude=="y":
	
	tip=input("what is the tip percent you paid on meal?(only number)")
	tip=int(tip)
	tip=tip/100
	total=meal_plus_tax+meal_plus_tax*tip

	print("price of meal plus tips Rs "+str(total)) 
	
else :
	
	print ("price of your meal is Rs "+str(meal_plus_tax))					

#stage 3

"""1. now i want to select different formulas for calculation
   2. add items in grocery store and calculating tax on them
	  at the end"""