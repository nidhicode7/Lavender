# Program to calculate factorial of a number using a loop

n = int(input("Enter a number: "))
fact = 1


# Multiply all numbers from 1 to n
for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)
