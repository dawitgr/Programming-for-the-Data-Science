#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Dawit Reda
#ID#10189420
#Module 2.2 Assignment
#Programming for the Data Science
#Submitted to Dr. Daniel Wu


# In[ ]:


#2.2 Write a program using a while loop that asks the user to enter a number that is divisible by 2. 
#Give the user a witty message if they enter something that is not divisible by 2 and make them enter a new number.
#Don’t let them stop until they enter an even number! Print a congratulatory message when they *ﬁnally* get it right. 


# In[1]:


#the input_number function will validate the user input, if the user input is a number it will continue, 
#if not will suggest to the user to input a number again
def check_user_input(input_message):
    while True:
        try:
            user_input = int(input(input_message))       
        except ValueError:
            print("Your input is not a number! Please try again")
            continue
        else:
            return user_input
            break 
#call the check_user_input function and check if the input is numeric
input_num = check_user_input("Please enter a number that is divisible by 2 ")
#check if the input is divisible by 2
while (input_num%2) != 0:
    input_num = float(input('The number you entered is not divisible by 2, Please try again: '))
else:
    #if the input is divisible by 2, congrats message witll pop up
    print('Congratulations, the number you entered is divisible by 2!')      


# In[ ]:




