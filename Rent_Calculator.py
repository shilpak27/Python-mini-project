# inputs- total rent,elecricity bill,food bill
# output-total amount you have to pay
Rent = int(input("Enter your apartment rent= "))
Food = int(input("Enter your food bill= "))
elecricity_bill = (int(input("Enter your electricity bill= ")))
Person = int(input("Enter the number of persons living in apartment= "))

output = (Food+Rent+elecricity_bill)//Person

print("Each Person will pay= ", output)
