#6 Write a program that asks the user to enter a mass in medieval units: talents, pounds, and lots. The program converts the input to full kilograms and grams and outputs the result to the user:
talents = float(input("Enter the number of talents: "))
pounds = float(input("Enter the number of pounds: "))
lots = float(input("Enter the number of lots: "))
pounds = talents*20 + pounds
grams = lots *13.3  
total_grams = pounds * 32 + grams
kilograms = total_grams // 1000
remaining_grams = total_grams % 1000
print(f"The mass is {kilograms} kilograms and {remaining_grams} grams.")