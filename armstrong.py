# Armstrong number: 153 = 1^3 + 5^3 + 3^3
n = int(input("Enter a number: "))
temp = n
sum = 0
length=len(str(n))

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
