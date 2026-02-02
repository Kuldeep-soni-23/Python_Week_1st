# Q30. Write a program to display the cube of the number up to an integer. 
# num = int(input("Enter an integer: "))
# for i in range(1, num + 1):
#     cube = i * i * i 
#     # or cube = i ** 3
#     print("Cube of", i, "is", cube)

#Print list add tuple

# a = [1, 2, 3, 4]
# b = (5, 6, 7, 8)
# c = a + list(b)
# print(c)
# set = {9, 10, 11,'abc',True}
# print(set)
# Dictionary = {'name': 'John', 'age': 30, 'city': 'New York'}
# print(Dictionary)

# #create a program using funstion prime or not 
# num = int(input("Enter a number: "))
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, (num+1)//2):
#         if num % i == 0:
#             return False
#     return True
# if is_prime(num):
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")
#  print even of number
# x = [1, 2, 3, 4, 5]
# even =list( filter(lambda n: n%2==0, x))
# print(even)
# #sum of number in lamnda and using reduce
# import functools
# x= [1, 2, 3, 4, 5]
# print(functools.reduce(lambda a, b: a + b, x))
# print(functools.reduce(lambda a, b: a * b, x))
# import numpy as np
# n = [1, 2, 3, 4, 5]
# print(type(n))
# ary = np.array(n)
# print(type(ary))
# print(ary**2)
# square = lambda x: x**2
# squared_numbers = list(map(square, n))
# print(squared_numbers)
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([6, 7, 8, 9, 10])
# print(np.add(a,b))
# print(a.ndim)
# print(a + b)
# 
# num = np.array([[1, 2, 3], [4, 5, 6]])
# print(num)
# print("Number of dimensions:", num.ndim)
# print("Shape of the array:", num.shape)     
# a = np.array([1, 2, 3, 4, 5])
# b = a.astype(np.float64)
# print(a)
# print(a.dtype)
# a = np.arange(1,13)
# print(a)
# print(a[-5:-1:1]) 
# print(a<6)

# print(a[a<6])

# a = np.arange(12).reshape(3,4)
# print(a)
# print(a.T)
# np.product(a)
# prices = np.array([30, 35, 50, 75, 100])
# budget = 25
# affordable = np.all(budget >= prices)
# print(affordable)
# if affordable:
#     print("There are items within your budget.")
# else:
#     print("No items are within your budget.")

# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[7, 8, 9], [10, 11, 12]])
# c = 

# import math


# x1 = int (input("Enter the number: "))
# y1 = int (input("Enter the number: "))
# x2 = int (input("Enter the number: "))
# y2 = int (input("Enter the number: "))
# sum = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print("sum =", sum)


# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# print(f"{a} + {b} = {a + b}")


