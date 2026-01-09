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