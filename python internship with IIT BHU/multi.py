"""import math

num=int(input("please enter the num :"))
print("multiplication table of {} is given below".format(num))

for i in range(1,11):
        print("{} x  {} = {}".format(num,i,num*i))

a=[[3,5,7],[2,5,8],[5,1,2]]
b=[[1,5,9],[6,0,4],[3,1,7]]
c=[[0,0,0],[0,0,0],[0,0,0]]

print("matrix a is :",a)
print("matrix a is :",b)
print("multiply of  a and b  is :")

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c [i][j] +=a[i][k]*b[k][j]
for r in c :
    print(r)
    """    








        

a=[[3,5,7],[2,5,8],[5,1,2]]
b=[[1,5,9],[6,0,4],[3,1,7]]
c=[[0,0,0],[0,0,0],[0,0,0]]

print("matrix a is :",a)
print("matrix a is :",b)
print("multiply of  a and b  is :")
for j in range(len(b)):
    for i in range(len(a[0])):
        for k in range(len(b)):
            c [i][j] +=a[i][k]*b[k][j]
for l in c :
    print(l)
        
        
       
