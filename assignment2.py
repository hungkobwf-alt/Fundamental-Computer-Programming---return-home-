#1 Write a function that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.

def check_zander_size():
    zander_length = float(input("Enter the length of the zander in centimeters: "))
    size_limit = 42
    if zander_length >= size_limit:
        print("The zander meets the size limit.")
    else:
        print(f"The zander is {size_limit - zander_length} centimeters below the size limit.")
        print("Please release the fish back into the lake.")

check_zander_size()
#2 Write a function that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.

def check_cabin_class():
    cabin_class = input("Enter the cabin class of the cruise ship: ").upper()
    if cabin_class == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("A: above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("B: windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")

check_cabin_class()

#3 Write a function that asks for the user's biological sex and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.

def check_hemoglobin():
    sex = input("Enter your biological sex (male/female): ").lower()
    hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
    if sex == "female":
        if hemoglobin_value < 117:
            print("Your hemoglobin value is low.")
        elif hemoglobin_value > 155:
            print("Your hemoglobin value is high.")
        else:
            print("Your hemoglobin value is normal.")
    elif sex == "male":
        if hemoglobin_value < 134:
            print("Your hemoglobin value is low.")
        elif hemoglobin_value > 167:
            print("Your hemoglobin value is high.")
        else:
            print("Your hemoglobin value is normal.")
check_hemoglobin()
    #4 Write a function that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400
def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")    
check_leap_year()
#5 Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in USD. The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas, and tells the user which pizza provides better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.
import math
def calculate_unit_price(diameter_cm, price_usd):
    radius_m = (diameter_cm / 2) / 100  # Convert diameter to radius in meters
    area_m2 = math.pi * (radius_m ** 2)  # Area in square meters
    unit_price = price_usd / area_m2  # Price per square meter
    return unit_price   
# Main program
diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (USD): "))
diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (USD): "))
unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)
if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price2 < unit_price1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")      
    
