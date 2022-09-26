# Program 1 ----> Addition of two numbers

# def sum(x,y):

#     z=x+y
#     return z

# result=sum(10,20) 
# print(result)  

##################################################################################################################################################

#Program 2 ---->Factorial of a Number
# import math

# def factorial(n):
#     return(math.factorial(n))

# n=int(input("Enter the Number: "))   
# print("Factorial of", n, "is",factorial(n)) 

##################################################################################################################################################

#Program 3: Sorting the list

# list_fruits = ['apple','orange','orange','apple','orange','orange','apple']
# list_fruits.sort()
# print(list_fruits)

#list1 = ['apple','orange','apple','orange','apple']
# count = 0
# for item in list1:
#     if(item == 'apple'):
#         count += 1
# print(count)
# for i in range(len(list1)):
#     if(i<count):
#         list1[i] = 'apple'
#     else:
#         list1[i] = 'orange'

# print(list1)

################################################################################################################################################

#string1 = input("enter expression ")

# string1 = "2+3*4+1-4/2"
# # print(len(string1))
# s = list(string1)
# # print(s[-2]) 



# s1=[]
# s2=[]
# for i in range(0,len(s)):
#     if(s[i]=="|"):
#         continue
#     s1.append(s[i])
#     if(s[i]=='/'):
#         s1[-2]=str(float(s1[-2])/float(s[i+1])) 
#         s1=s1[:-1]
#         s[i+1] = '|'
# print(s1)

# for i in range(0,len(s1)):
#     if(s1[i]=="|"):
#         continue
#     s2.append(s1[i])
#     if(s1[i]=='*'):

#         s2[-2]=str(float(s2[-2])*float(s1[i+1])) 
#         s2=s2[:-1]
#         s1[i+1] = '|'

# print(s2)

# for i in range(0,len(s2)):
#     if(s2[i] == '+'):
#         s2[i+1]=float(s2[i-1])+float(s2[i+1])
        
#     if(s2[i] == '-'):
#         s2[i+1]=float(s2[i-1])-float(s2[i+1])
# print(s2[-1])



###############################################################################################################################################
# LOOPS IN PYTHON

#FOR LOOP

# numbers = [1, 2, 3, 4, 5]
# # iterate over each element in list num
# for i in numbers:
#     # ** exponent operator
#     square = i ** 2
#     print("Square of:", i, "is:", square)

##################################################################################################################################################

#numbers = [10, 20, 30, 40, 50]

# definite iteration
# run loop 5 times because list contains 5 items

# sum = 0
# for i in numbers:
#     sum = sum + i
# list_size = len(numbers)
# average = sum / list_size
# print(average)

##################################################################################################################################################

# for i in range(1, 21):
#     if i % 2 == 0:
#         print('Even Number:', i)
#     else:
#         print('Odd Number:', i)

#################################################################################################################################################

#Use for loop to generate a list of numbers from 9 to 50 divisible by 2.

# nl=[]
# for x in range(9, 52):
#     if (x%2==0):
#         nl.append(str(x))
# print (','.join(nl)) 

##################################################################################################################################################

#WHILE LOOP

# n = 10
# while n <= 100:
#     print(n ,end = ",")
#     n = n+5

###############################################################################################################################################

# myList = [23,45,12,10,25]
# i = 0 
# sum = 0

# while i < len(myList):
#     sum += myList[i]
#     i += 1

# print(sum)

##################################################################################################################################################

# i = 0 
# word = "Hello"

#print all letters except y and o

# while i < len(word):
#     if word[i] == "e" or word[i] =="o":
#         i += 1
#         continue

#     print(word[i])
#     i += 1

##################################################################################################################################################

# num = int(input("Enter a number: "))
# b = 0
# p = 1
# n = num

# while n>0:
#     rem = n%2
#     b += rem * p
#     p = p*10
#     n = n//2

# print("Binary value: ",b)

##################################################################################################################################################

# p = 5
# sum = 0
# count = 0

# while p > 0:
#     count += 1
#     f = int(input("Enter the number "))
#     sum += f
#     p -= 1
  
# average = sum/count
# print("Average of given Numbers:",average)

##################################################################################################################################################

# n= int(input("Enter an integer: "))

# i = 1
# while i <= 10:
#     mul = i*n
#     i += 1
#     print(mul)

##################################################################################################################################################

# n = int(input("Enter the number: "))
# f =n
# r = 1

# while f != 0 :
#     r *= f 
#     f -= 1
# print("Factorial of",n,"is:",r)
    
#################################################################################################################################################

#Nested Loop


# outer loop
# for i in range(1, 11):
#     # nested loop
#     # to iterate from 1 to 10
#     for j in range(1, 11):
#         # print multiplication
#         print(i * j, end=' ')
#     print()

##################################################################################################################################################

# rows = 10
# # outer loop
# for i in range(1, rows + 1):
#     # inner loop
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print('')


##################################################################################################################################################

#WHILE LOOP INSIDE FOR LOOP

# names = ['Kelly', 'Jessa', 'Emma']
# # outer loop
# for name in names:
#     # inner while loop
#     count = 0
#     while count < 5:
#         print(name, end=' ')
#         # increment counter
#         count = count + 1
#     print()


















 

