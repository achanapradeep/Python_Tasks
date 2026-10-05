# 1)average of numbers

a=int(input())
sum=0
for i in range(a+1):
    sum+=i
avg=sum/a
print(avg)  
# input 10
# output is 5.5

# 2)sum of squares
n=int(input())
n=4
sum=0
for i in range(1,n+1):
    print(i*i)
    sum=sum+(i*i)  
print("sum of squares is",sum)
# input is 15
# output is
# 1
# 4
# 9
# 16
# sum of squares is 30

# 3)sum of cubes
m=int(input())
m=4
sum=0
for i in range(1,m+1):
    print(i**i)
    sum=sum+(i**i)  
print("sum of cubes is",sum)
# input is 8
# output is
# 1
# 4
# 27
# 256
# sum of cubes is 288

# 4)power of a number 
p=2
sum=0
for i in range(1,6):
    print(pow(p,i))
    sum=sum+(pow(p,i))
print("sum of powers is ",sum)
# input is 2 and 5
# output is
# 2
# 4
# 8
# 16
# 32
# sum of powers is  62

# 5)febonisi series
r=int(input())
a=0
b=1
s=" "
for i in range(r):
    s=s+str(a)+" "
    c=a+b
    a=b
    b=c 
print("febonisi series is:",s)
# input is 6
# output is
# febonisi series is:  0 1 1 2 3 5

# 6)first n terms of a series(1,1/2,1/3....)
o=5
for i in range(o+1):
    print(1,"/",i)
# input is 5
# output is
# 1
# 1/1
# 1/2
# 1/3
# 1/4

# 7)first n terms of a series (1,11,111,1111....)
b=5
s="1"
s1=""
for i in range(b):
    s=s+s1
    s1="1" 
    print(s)
# input is 
# output is 
# 1
# 11
# 111
# 1111
# 11111

# 8)first n terms of a series(1,3,9,27......)
mul=3
n=int(input())
for i in range(n+1):
    print(mul**i)
# input is 9 
# output is 
# 3
# 9
# 27
# 81
# 243
# 729
# 2187
# 6561
# 19683