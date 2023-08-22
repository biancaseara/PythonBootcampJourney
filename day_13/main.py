############DEBUGGING#####################

# # Describe Problem
# # we've got a function that loops thru a range of 1 to 20, n once reaches 20, it's supposed to print 'you got it'
# # the problem is when it reaches 20, it doesn't print that line into the console 
# def my_function():
# # the range(1,20) won't reach 20 but 19, to reach 20 we must set the end as 21
#   for i in range(1, 21):  
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# # I've got a list with 6 items [0,5], then I've got a imported function to return a random integer (1,6)
# # the problem is in some point will reach a 6, but there's not a item[6], so will return a indexError
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # to solve that we must just change the randint from (1,6) to (0,5)
# dice_num = randint(0, 5) 
# print(dice_imgs[dice_num])
# # print(dice_imgs[6])

# Play Computer
year = int(input("What's your year of birth? ")) #asking a year
if year > 1980 and year < 1994: #checking a range of year from 1981 to 1993
  print("You are a millenial.")
elif year >= 1994: #checking if is > 1994, the 1994 isn't included, that's the problem
  print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])