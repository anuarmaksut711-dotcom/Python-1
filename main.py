import math

print("Task 1 ")
print("Anuar Maksut")
print("Aitu")
print("Nur-Sultan, Kazakhstan, 010000")
print()

print("Task 2 ")
length = float(input("Enter the length of the room in meters: "))
width = float(input("Enter the width of the room in meters: "))
print(f"The area of the room is {length * width:.2f} square meters.\n")

print(" Task 3")
field_length = float(input("Enter the length of the field in feet: "))
field_width = float(input("Enter the width of the field in feet: "))
print(f"The area of the field is {(field_length * field_width) / 43560:.2f} acres.\n")

print(" Task 4")
small = int(input("Enter number of containers <= 1 liter: "))
large = int(input("Enter number of containers > 1 liter: "))
print(f"Refund amount: ${small*0.10 + large*0.25:.2f}\n")

print("Task 5")
meal_cost = float(input("Enter the cost of the meal:"))
tax = meal_cost * 0.07
tip = meal_cost * 0.18
print(f"Tax: ${tax:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Grand total: ${meal_cost + tax + tip:.2f}\n")

print("Task 6")
n = int(input("Enter a positive integer n: "))
print(f"Sum of integers from 1 to {n} is {n*(n+1)//2}\n")

print("Task 7")
cents = int(input("Enter amount in cents:"))
coins = {}
coins['toonies'] = cents // 200
cents %= 200
coins['loonies'] = cents // 100
cents %= 100
coins['quarters'] = cents // 25
cents %= 25
coins['dimes'] = cents // 10
cents %= 10
coins['nickels'] = cents // 5
cents %= 5
coins['pennies'] = cents
print("Change:")
for coin, qty in coins.items():
    print(f"{coin.capitalize()}: {qty}")
print()

print("Task 8")
feet = float(input("Enter feet:"))
inches = float(input("Enter inches:"))
print(f"Height in centimeters: {(feet*12 + inches)*2.54:.2f} cm\n")

print("Task 9")
radius = float(input("Enter radius of the circle "))
print(f"Area of the circle: {math.pi * radius**2:.2f}\n")

print("Task 10 ")
while True:
    celsius_input = input("Enter temperature in Celsius: ")
    try:
        celsius = float(celsius_input)
        print(f"{celsius:.2f} °C = {(celsius*9/5)+32:.2f} °F")
        break
    except ValueError:
        print("Invalid input")