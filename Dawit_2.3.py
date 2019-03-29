#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dawit Reda
#ID#10189420
#Module 2.3 Assignment
#Programming for the Data Science
#Re-Submitting to Dr. Daniel Wu


# In[ ]:


# 2.3 Pig Latin is a game taking the ﬁrst letter of a word, puts it at the end, and appends “ay”. 
#The exception is if the ﬁrst letter is a vowel, you keep it as it is and append “hay” to the end.

# E.g. “boot” → “ootbay” and “image” → “imagehay”

# Write a program using a while loop that asks the user to enter a word (see 2 for user input functions),
#then converts the word to Pig Latin. Save and submit your work in a Python file, e.g. [your_name]_2.3.py.

# (Note: It will be useful to deﬁne a list of VOWELS. 
#This way, you can check if a letter x is a vowel with the expression x in VOWELS. 
#To get a word except for the ﬁrst letter, you can use word[1:].
#Make sure your program exits the while loop if the user does not want to continue to play.)


# In[ ]:


#the function below converts a word into a Pig Latin
def word_into_Pig_Latin(input_word):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    #split the input word and convert it to lower case
    first_letter = input_word[0].lower()
    #check if the first word in in vowels
    while first_letter in VOWELS: 
        #if the first word is vowel add hay and print it out
        print(input_word + "hay"  )
        check_input = input('Do you want to continue? please enter y to continue the game:')
        #check if the user want to continue to play the game
        if check_input == 'y':
            #user input when they want to play again
            input_word = input('Please Enter a word: ')
            #Recursive Function 
            word_into_Pig_Latin(input_word)
        #thank you message if the user does not want to play the game      
        else:
            return print('Thank you for playing Pig latin game \n')
                
    else:
        #if the first word is not a vowel, remove the first word and add it at the end and add ay at the end too and print
        print( input_word[1:] + input_word[0] + "ay"    )
        check_input_ = input('Do you want to continue? please enter y to continue the game:')
        #check if the user want to continue to play the game
        if check_input_ == 'y':
            #user input when they want to play again
            input_word = input('Please Enter a word: ')
            #Recursive Function 
            word_into_Pig_Latin(input_word)
        #thank you message if the user does not want to play the game    
        else:
            return print('Thank you for playing Pig latin game \n')
   
input_word = input('Please Enter a word: ')
word_into_Pig_Latin(input_word)

