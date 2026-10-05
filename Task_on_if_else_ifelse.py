

# ---------- if-else ----------

# 1. 3-digit number
n = int(input("Enter a number: "))
if 100 <= abs(n) <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")

# 2. Divisible by both 3 and 5
n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

# 3. Valid triangle
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
if a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Not a valid triangle")

# 4. Multiple of 10
n = int(input("Enter a number: "))
if n % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")


# ---------- if-elif-else ----------

# 1. Triangle type
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

# 2. Electricity bill
units = int(input("Units consumed: "))
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
elif units <= 300:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5
else:
    bill = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7
print("Electricity bill: ₹", bill)

# 3. Age category
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

# 4. Shopping discount
amount = float(input("Shopping amount: ₹"))
if amount < 1000:
    discount = 0
elif amount <= 4999:
    discount = 10
elif amount <= 9999:
    discount = 20
else:
    discount = 30
final = amount - amount * discount / 100
print("Discount:", discount, "%")
print("Final amount: ₹", final)

# 5. Season
m = int(input("Enter month number (1-12): "))
if 3 <= m <= 5:
    print("Spring")
elif 6 <= m <= 8:
    print("Summer")
elif 9 <= m <= 11:
    print("Autumn")
elif m == 12 or m == 1 or m == 2:
    print("Winter")
else:
    print("Invalid month")

# 6. Leap year
year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")


# ---------- Nested if ----------

# 1. Blood donation eligibility
age = int(input("Enter age: "))
if 18 <= age <= 60:
    weight = float(input("Enter weight (kg): "))
    if weight > 50:
        print("Eligible to donate blood")
    else:
        print("Not eligible: weight must be above 50 kg")
else:
    print("Not eligible: age must be between 18 and 60")

# 2. Grade (only if passed in all 4 subjects; pass mark = 35)
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35:
    avg = (m1 + m2 + m3 + m4) / 4
    print("Average:", avg)
    if avg >= 90:
        print("Grade: A")
    elif avg >= 75:
        print("Grade: B")
    elif avg >= 60:
        print("Grade: C")
    elif avg >= 50:
        print("Grade: D")
    else:
        print("Grade: E")
else:
    print("Failed in one or more subjects - no grade")

# 3. Scholarship eligibility
age = int(input("Enter age: "))
if age > 18:
    score = float(input("Enter score: "))
    if score > 86:
        print("Eligible for scholarship")
    else:
        print("Not eligible: score must be above 86")
else:
    print("Not eligible: age must be above 18")