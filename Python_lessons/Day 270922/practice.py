# 1) Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0

# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i
###################################################################################################################################

# 2) Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

# def multiplication_or_sum(num1, num2):
#     # calculate product of two number
#     product = num1 * num2
#     # check if product is less then 1000
#     if product <= 1000:
#         return product
#     else:
#         # product is greater than 1000 calculate sum
#         return num1 + num2

# # first condition
# result = multiplication_or_sum(20, 30)
# print("The result is", result)

# # Second condition
# result = multiplication_or_sum(40, 30)
# print("The result is", result)
###############################################################################################################################

# 3) Write a program to accept a string from the user and display characters that are present at an even index number.

# accept input string from a user
# User_input = input('Enter word ')
# print("Original String:", User_input)

# # get the length of a string
# size = len(User_input)

# # iterate a each character of a string
# # start: 0 to start with first character
# # stop: size-1 because index starts with 0
# # step: 2 to get the characters present at even index like 0, 2, 4
# print("Printing only even index chars")
# for i in range(0, size - 1, 2):
#     print("index[", i, "]", User_input[i])
##################################################################################################################################

# 4)Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# def first_last_same(numberList):
#     print("Given list:", numberList)
    
#     first_num = numberList[0]
#     last_num = numberList[-1]
    
#     if first_num == last_num:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print("Result is", first_last_same(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("Result is", first_last_same(numbers_y))

######################################################################################################################################

# 5) Display numbers divisible by 5 from a list

# num_list = [10, 20, 33, 46, 55]
# print("Given list:", num_list)
# print('Divisible by 5:')
# for num in num_list:
#     if num % 5 == 0:
#         print(num)

######################################################################################################################################

# 6) Print the following pattern
    #  1 
    #  2 2 
    #  3 3 3 
    #  4 4 4 4 
    #  5 5 5 5 5

# for num in range(10):
#     for i in range(num):
#         print (num, end=" ") 
#     # new line after each row to display pattern correctly
#     print("\n")

########################################################################################################################################

# 7)Write a program to check if the given number is a palindrome number.
# def palindrome(number):
#     print("original number", number)
#     original_num = number
    
#     # reverse the given number
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10

#     # check numbers
#     if original_num == reverse_num:
#         print("Given number palindrome")
#     else:
#         print("Given number is not palindrome")

# palindrome(121)
# palindrome(125)

#############################################################################################################################################

# 8) Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list 
# and even numbers from the second list.

# def merge_list(list1, list2):
#     result_list = []
    
#     # iterate first list
#     for num in list1:
#         # check if current number is odd
#         if num % 2 != 0:
#             # add odd number to result list
#             result_list.append(num)
    
#     # iterate second list
#     for num in list2:
#         # check if current number is even
#         if num % 2 == 0:
#             # add even number to result list
#             result_list.append(num)
#     return result_list

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print("result list:", merge_list(list1, list2))

##########################################################################################################################################

# 9) Print downward Half-Pyramid Pattern with Star (asterisk)

# for i in range(6, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

############################################################################################################################################

# 10) Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. 
# Also, it must return both addition and subtraction in a single return call.

# def calculation(a, b):
#     addition = a + b
#     subtraction = a - b
#     # return multiple values separated by comma
#     return addition, subtraction

# # get result in tuple format
# result = calculation(40, 10)
# print(result)

#############################################################################################################################################

# 11) Swap two tuples in Python
# tuple1 = (11, 22)
# tuple2 = (99, 88)

# tuple1 = (11, 22)
# tuple2 = (99, 88)
# tuple1, tuple2 = tuple2, tuple1
# print(tuple2)
# print(tuple1)

#############################################################################################################################################

# 12) Rotate an array by k times

# List slicing approch to rotate the array
def rotateArray(a,d):
    n=len(a)
    a[:]=a[d:n]+a[0:d]
    return a

arr = [1, 2, 3, 4, 5]

print("Rotated list is")
print(rotateArray(arr,2)) 

