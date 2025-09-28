## Inputs we need from the User :-
# 1. Rent Amount 
# 2. Food Ordered Amount
# 3. Electricity Units spent 
# 4. Charge per unit of electricity
# 5. Number of people staying in the accommodation

# ## Outputs we need to give to the User :-
# 1. Total Amount you have to pay is
totalRent = int(input("Enter your accommodation rent: "))
totalFood = int(input("Enter your food ordered amount: "))
electricitySpent = int(input("Enter your electricity units spent: "))
chargePerUnit = int(input("Enter your charge per unit of electricity: ")) 
numberOfPeople = int(input("Enter number of people staying in the accommodation: "))

totalBill = totalRent + totalFood + (electricitySpent * chargePerUnit)
amountPerPerson = totalBill / numberOfPeople
print(f"Total Amount you have to pay is: {totalBill}")
print(f"Amount per person is: {amountPerPerson}")

# To Run Python program in terminal :-