# 1)sum of prime numbers in the range of 20 to 150
sum=0 
for j in range(20,151):
    n=j
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        sum+=n
print(sum)

# 2) Average of the perfect numbers in the range of 1 to 1000

add=0
count=0
for i in range(1,1001):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=j
    if(sum==i):
        add+=i 
        count+=1
total=add//count
print(total)
2164

# 3)Palindrome number in the range of 100 to 500
for i in range(100,501):
    n=i 
    new=n
    reverse=0
    while(n>0):
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
        if(reverse==new):
            print(new)

# 5)digit sum = 1o in the range of 120 to 850
for i in range(120,851):
    n=i
    rev=0
    sum=0
    while(n>0):
        digit=n%10
        sum+=digit
        n=n//10
    if(sum==10):
        print(i)

#  Pairs with target sum    is 30

for a in range(1,51):
    for b in range(1,51):
        if a+b==30 and a<=b: 
            print((a,b))

# 6)Exatly 3 factors
for j in range(10,301):
    n=j
    count=0
    for i in range(1,n+1):
        if (n%i==0):
            count+=1
    if(count==3):
        print(n)
    
# 7)prime factors
for i in range(20,51):
    n=i  
    fact=2
    while(fact <=n):
        if(n%fact==0):
            print(fact)
            n=n//fact 
        else:
            fact+=1
    print()

# 8)find number with maximum factors
best_num=50
max_fact=0
for j in range(50,151):
    n=j
    fact=0
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            fact+=i 
            count+=1 
    if(count>max_fact):
        max_fact=count 
        best_num=j 
print(best_num,"max value is",max_fact)
# 9) amstrom number in thr range(100,1000)
for i in range(100,1000):
    n=i 
    sum=0
    while(n!=0):
        digit=n%10
        sum=sum+digit**3
        n=n//10
    if(sum==i):
        print(i)
  