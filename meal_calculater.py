meal=input("what is the price of the meal?")
meal=int(meal)
tax=input("what is the percent of tax on meal?(only number)")
tax=int(tax)
tax=tax/100
meal_plus_tax=meal+meal*tax
print ("price of meal plus tax Rs "+ str(meal_plus_tax))
tip=input("what is the tip percent paid on meal?(only number)")
tip=int(tip)
tip=tip/100
total=meal_plus_tax+meal_plus_tax*tip
print("price of meal plus tips Rs "+str(total))