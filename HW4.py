#Name:Anthony Martinez
#Class: 5th Hour
#Assignment: HW4

#1. Print "Hello World!"
print("Hello World")
#2. import the 'math' library
import math
#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
x = float(input("Enter a number with a decimal: "))
y = int(input("Enter another number with a integer: "))
#4. Create a variable with the value that is x and y added together.
Var = x + y
#5. Print the variable from #4.
print (Var)
#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
Var1 = (Var/3)
#7. Print the variable from #6.
print (Var1)
#8. Create a variable with the value of the square root of y, then print the result.
Var2 = math.sqrt(y)
print (Var2)
#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
print (round (x,1))
#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
print (math.ceil(x))
#11. Use the floor function to round x down to the nearest whole number. Print the result.
print (math.floor(x))