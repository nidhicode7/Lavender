# Program to count frequency of elements in a list

# Taking input from the user
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    item = input(f"Enter element {i+1}: ")
    lst.append(item)

# Creating an empty dictionary to store frequencies
freq = {}

# Looping through the list to count frequencies
for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Printing the frequency of each element
print("\nFrequency of elements:")
for key, value in freq.items():
    print(f"{key}: {value}")
