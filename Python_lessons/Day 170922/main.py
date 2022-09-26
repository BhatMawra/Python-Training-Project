#palidrome Program
#Method 1:
# def palindrome(s):
#     rs = s[::-1]
#     if rs == s:
#         print("It is a palindrome")
#     else:
#         print("It is not a palindrome")

# s = input("Enter the word: ")
# palindrome(s)

#Method 2:
# def palindrome(s):
#     i=0
#     n = len(s) - 1
#     while(i<n):
#         if(s[n] == s[i]):
#             i += 1
#             n -= 1
#         else:
#             print("It is not a palindrome")
#             return
#     print("It is a palindrome")        

# s = input("Enter the word: ")
# palindrome(s)



# f = open("exercises.txt","r")

# content = f.read()
# print("1",content)
# content = f.read(5)
# print("2",content)

# f.close()

# content = f.readline()
# print(content,end='')
# content = f.readline()
# print(content,end='')

# for line in f:
#     print(line,end='')

# content = f.readlines()
# print(content)

# f.write("\nsay something\n")
# f.write("good morning\n")
# f.write("good afternoon\n")


# f.close()

# content = f.read()
# content_list = content.split(',')
# print(content)
# print(content_list)

