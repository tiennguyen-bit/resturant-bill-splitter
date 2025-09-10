#Resturant Bill Splitter
#Tien Nguyen
#9/10/25


#Ask the user the meal cost
meal_cost = float(input("Enter the cost of the meal: "))

#Ask the user how much they want to tip
tipping = float(input("How much you want to tip: "))

#Ask the user how many people are splitting the bill
splitting = int(input("How many are you are gonna pay: "))

#convert the tipping number into a decimal
tips = tipping / 100

#Calculate the total
total_meal = meal_cost + tips

#Calculate the split payment
separate = total_meal / splitting

#Display the tip amount, total bill, and each person's share
print(f"This is the amount you are tipping:$", tips)
print(f"Your total bill:$", total_meal)
print(f"Your pay separately:$", separate)