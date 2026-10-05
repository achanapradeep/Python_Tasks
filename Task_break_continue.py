#  1)first even digit from the left in 753914286.
n=753914286
count=0
fst=0
while(n!=0):
    digit=n%10
    n=n//10
    if(digit%2==0):
        count+=1
        print(digit) 
        break
        
if(count>fst):
    fst=count 
print(fst)  
# 2) Find the first prime number between 50 and 100.
for i in range(50,101):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i)
        break
# 3)Find the first number whose digit sum is 10.
for i in range(1,101):
    n=i
    rev=0
    sum=0
    while(n>0):
        digit=n%10
        sum+=digit
        n=n//10
    if(sum==10):
        print(i)
        break

# 4) Find the first number with exactly 3 divisors between 1 and 100.
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==3):
        print(i)
        break 
# 5)Stop when 3 consecutive odd numbers occur between 1 and 50.
counts=0
for i in range(1,51):
    if(i%2!=0):
        counts+=1
        print(i)
    if counts==3:
        break 
# 6) Find the first palindrome between 10 and 500.
for i in range(10,501):
    n=i 
    new=n
    reverse=0
    while(n>0):
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
    if(reverse==new):
        print(new) 
        break       
# 7) Find the first perfect number between 1 and 1000.   
for i in range(1,1001):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=j
    if(sum==i):
        print(i)
        break 
# 8)Print the first 5 even numbers.
count=0
for i in range(1,51):
    if(i%2==0):
        count=+1
        print(i)
        if(count==5):
             break
    
# 9)Print the first 5 prime numbers.

found = 0
for i in range(20):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
        found += 1
        if found == 5:
            break

        
# 10)Print the first 3 numbers divisible by 7.
found = 0
for i in range(1, 100):
    if i % 7 == 0:
        print(i)
        found += 1
        if found == 3:
            break           

# 1. Print 1-30, skipping even numbers
for i in range(1, 31):
    if i % 2 == 0:
        continue
    print(i)

# 2. Print 1-40, skipping multiples of 4
for i in range(1, 41):
    if i % 4 == 0:
        continue
    print(i)

# 3. Print 1-30, skipping numbers from 10-20
for i in range(1, 31):
    if 10 <= i <= 20:
        continue
    print(i)

# 4. Print 1-50, skipping multiples of 3
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)

# 5. Extract 502304, skipping digit 0
n = 502304
while n > 0:
    d = n % 10
    n //= 10
    if d == 0:
        continue
    print(d)

# 6. Extract 5832461, printing only even digits
n = 5832461
while n > 0:
    d = n % 10
    n //= 10
    if d % 2 != 0:
        continue
    print(d)

# 7. Extract 1432578, skipping odd digits
n = 1432578
while n > 0:
    d = n % 10
    n //= 10
    if d % 2 != 0:
        continue
    print(d)

# 8. Print 1-200, skipping multiples of 3 or 5
for i in range(1, 201):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

# 9. Print 1-500, skipping numbers with odd digit sum
for i in range(1, 501):
    s = 0
    t = i
    while t > 0:
        s += t % 10
        t //= 10
    if s % 2 != 0:
        continue
    print(i)

# 10. Print 1-500, skipping numbers containing digit 0
for i in range(1, 501):
    has_zero = False
    t = i
    while t > 0:
        if t % 10 == 0:
            has_zero = True
            break
        t //= 10
    if has_zero:
        continue
    print(i)

# 1. Print 1-50, skip multiples of 3, stop at 40
for i in range(1, 51):
    if i == 40:
        break
    if i % 3 == 0:
        continue
    print(i)

# 2. Print odd numbers, skip evens, stop at the first multiple of 7
i = 1
while True:
    if i % 2 == 0:
        i += 1
        continue
    if i % 7 == 0:
        break
    print(i)
    i += 1

# 3. Extract 5830421, skip odd digits, stop at 0
n = 5830421
while n > 0:
    d = n % 10
    n //= 10
    if d == 0:
        break
    if d % 2 != 0:
        continue
    print(d)

# 4. Extract 8325147, print digits until 5
n = 8325147
while n > 0:
    d = n % 10
    n //= 10
    if d == 5:
        break
    print(d)

# 5. Search from 51, skip non-multiples of 9, stop at the first multiple of 9
i = 51
while True:
    if i % 9 != 0:
        i += 1
        continue
    print(i)
    break