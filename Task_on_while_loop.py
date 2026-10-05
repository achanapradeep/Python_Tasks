# 1. Sum of digits
n = int(input("Enter a number: "))
n = abs(n)
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)


# 2. Average of digits
n = int(input("Enter a number: "))
n = abs(n)
total = 0
count = 0
while n > 0:
    total += n % 10
    count += 1
    n //= 10
if count > 0:
    print("Average of digits:", total / count)
else:
    print("Average of digits: 0")


# 3. Sum of first and last digit
n = int(input("Enter a number: "))
n = abs(n)
last = n % 10
first = n
while first >= 10:
    first //= 10
print("Sum of first and last digit:", first + last)


# 4. Average of digits divisible by 5
n = int(input("Enter a number: "))
n = abs(n)
total = 0
count = 0
while n > 0:
    d = n % 10
    if d % 5 == 0:
        total += d
        count += 1
    n //= 10
if count > 0:
    print("Average:", total / count)
else:
    print("No digits divisible by 5")


# 5. Difference between largest and smallest digit
n = int(input("Enter a number: "))
n = abs(n)
largest = 0
smallest = 9
while n > 0:
    d = n % 10
    if d > largest:
        largest = d
    if d < smallest:
        smallest = d
    n //= 10
print("Largest:", largest)
print("Smallest:", smallest)
print("Difference:", largest - smallest)