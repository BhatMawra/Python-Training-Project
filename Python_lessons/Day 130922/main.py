#iterative approach to nth term fibonacci series
# def fiboIter(n):
#     num1= 0
#     num2= 1
#     for i in range(1,n):
#         num3 =  num1
#         num1 = num2
#         num2 = num1 + num3 
       
#     return num2

# n=int(input("Enter the number: "))
# print(fiboIter(n))


#Recursive Approach

# def fiboRecur(n):
#     if n==0:
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fiboRecur(n-1) + fiboRecur(n-2)
# n=int(input("Enter the number: "))
# print (fiboRecur(n))
            
##################################################################################################################################################
#Roll a dice Game

# import random

# #Initialise player scores to 0
# player1_score = 0
# player2_score = 0

# roll_again = "yes"

# # Repeat everything in this block 
# while roll_again == "yes" or roll_again == "y":

#     # Generate random numbers between 1 and 6 for each player.
#     player1_value = random.randint(1, 6)
#     player2_value = random.randint(1, 6)

#     # Display the values
#     print("Player 1 rolled: ", player1_value)
#     print("Player 2 rolled: ", player2_value)

#     # Selection: based on comparison of the values, take the appropriate path through the code.
#     if player1_value > player2_value:
#         print("player 1 wins.")
#         player1_score = player1_score + 1  # This is how we increment a variable
#     elif player2_value > player1_value:
#         print("player 2 wins")
#         player2_score = player2_score + 1
#     else:
#         print("It's a draw")

#     roll_again=input("Press enter to continue.")  # Wait for user input to proceed.
   
        
# print("### Game Over ###")
# print("Player 1 score:", player1_score)
# print("Player 2 score:", player2_score)


##################################################################################################################################################

#Program:Head or Tails

# import random

# coin=("Heads","Tails")
# toss = random.choice(coin)

# selection = input("Heads or Tails: ")
# if selection==toss:
#     print("You won!")
# else:
#     print("You lose! Try again")



