#2 Write a program that asks your name and then greets you by your name
name = input("Enter your name: ")
print(f"Hello, {name}!")
#3 Write a program that asks the user for the radius of a circle and the prints out the circumference of the circle
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * 3.14159 * radius
print(f"The circumference of the circle is: {circumference}")
#4 Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print(f"The perimeter of the rectangle is: {perimeter}")
print(f"The area of the rectangle is: {area}")
#5 Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
print(f"The sum of the numbers is: {sum}")
print(f"The product of the numbers is: {product}")
print(f"The average of the numbers is: {average}")
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
#7 Write a program that draws two random combinations of numbers for a combination lock 
import random
code_3_digit = [random.randint(0, 9) for _ in range(3)]
code_4_digit = [random.randint(1, 6) for _ in range(4)]
print("3-digit lock code (0–9):", code_3_digit)
print("4-digit lock code (1–6):", code_4_digit)
