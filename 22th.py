# Q22. Create a program to print all Armstrong numbers between 1 to 1000. 
for i in range(1,1001):
    temp = i
    sum = 0
    while temp>0:
       digits = temp%10
       sum+=digits**3
       temp//=10
    if sum == i :   
        print(i)

   