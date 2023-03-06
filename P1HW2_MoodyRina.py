# Program calculates the travel expenses
# March 5, 2023
# CTI-110 P2HW1 - Travel
# Rina Moody
#
##**********Pseudocode**********
#Ask user "Enter your budget: "
#Input Initial Budget
#Ask user "Enter travel destination: "
#Input Location
#Ask user "Enter amount you will spend on gas: "
#Input Fuel
#Ask user "Enter amount you will spend on accommodation: "
#Input Accommodation
#Ask user "Enter amount you will spend on food: "
#Input Food
#Set Remaining Balance = Initial Budget - (Fuel + Accommodation + Food)
#Display Location:
#Display Initial Budget:
#Display Fuel
#Display Accommodation:
#Display Food
#Display Remaining Balance

print('This program calculates and displays travel expenses')
initial_budget = int(input('Enter Budget: '))
location = (input('Enter your travel destination: '))
fuel = int(input('How much you think you will spend on gas? '))
accommodation = int(input('Approximately, how much will you need for accommodation/hotel? '))
food = int(input('Last, how much do you need for food? '))
print('\n------------Travel Expenses------------')
print('Location:',location)
print('Initial Budget:',initial_budget)
print('\nFuel:',fuel)
print('Accommodation:',accommodation)
print('Food:',food)
print('\nRemaining Balande:',initial_budget - (fuel + accommodation + food))
