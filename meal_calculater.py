# meal price calculater

#stage 1

meal=input("what is the price of the meal?")
meal=float(meal)
tax=input("what is the percent of tax on meal?(only number)")
tax=float(tax)
tax=tax/100
meal_plus_tax=meal+meal*tax

print ("price of meal plus tax Rs "+ str(meal_plus_tax))

#stage 2

answer=input("did you pay tip to the waiter?")

if  answer=="yes"or answer=="y":
	
	tip=input("what is the tip percent you paid on meal?(only number)")
	tip=float(tip)
	tip=tip/100
	total=meal_plus_tax+meal_plus_tax*tip

	print("price of meal plus tips Rs "+str(total)) 
	
else :
	
	print ("price of your meal is Rs "+str(meal_plus_tax))					

#stage 3

"""1. now i want to select different formulas for calculation
   2. add items in grocery store and calculating tax on them
	  at the end"""
