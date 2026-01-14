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