# square problem
n = 5
for i in range(n):
    for j in range(n):
        print("* ", end=" ")
    print()
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *     

# Right Angle triangle problem
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# Inverted right angle triangle problem
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# Pyramid problem
n = 5
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("* " * i)

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

# Number pyramid problem
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# Diamond Pattern problem
n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# Floyd's Triangle problem
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

# Pascal's Triangle problem
n = 5
for i in range(n):
    val = 1
    print(" "*(n-i), end="")
    for j in range(i+1):
        print(val, end=" ")
        val = val * (i-j) // (j+1)
    print()

#      1 
#     1 1 
#    1 2 1 
#   1 3 3 1 
#  1 4 6 4 1 