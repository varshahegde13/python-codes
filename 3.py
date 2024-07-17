 #patterns program

n = 5
for i in range(n):
    for j in range(n):
        print("*",end =' ')
    print()

n = 5
for i in range(n):
    for j in range(n-1):
        print("*",end =" ")
    print()

n = 5
for i in range(n):
    for j in range(n):
        if j%2==0:
            print("*",end=" ")
        else:
            print("@",end = " ")
    print()

n = 5
for i in range(n):
    for j in range(n):
        if i%2==0:
            print("*",end=" ")
        else:
            print("@",end = " ")
    print()

n= 5
for i in range(n):
    for j in range(n):
        if i ==0 or  i==n-1 or j ==n-1 or j ==0 :
            print("*",end = " ")
        else:
            print(" ",end=' ')
    print()

n = 7
for i in range(n):
    for j in range(n):
        if i ==0 or j ==0 or i ==n-1 or j ==n-1 or j ==n//2:
            print("*",end =" ")
        else:
            print(" ",end=" ")
    print()

n = 5
for i in range(n):
    for j in range(n):
        if i ==0 or i==n-1 or j ==0 or j ==n-1 or i ==j :
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()


n = 5
for i in range(n):
    for j in range(n):
        if i ==0 or i==n-1 or j ==0 or j ==n-1 or i+j == n-1 :
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()

n = 5
for i in range(n):
    for j in range(n):
        if i ==n//2 or j == n//2:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()

n = 5
for i in range(n):
    for j in range(n):
        if i >=j:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()
print()

n = 5
for i in range(n):
    for j in range(n):
        if i <=j:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()


n= 5
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()


