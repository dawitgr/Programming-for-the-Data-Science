#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Dawit Reda
ID#10189420
Module 3 Assignment
Programming for the Data Science
Submitted to Dr. Daniel Wu
"""


# In[2]:


"""
Question 3.1 Transform your code from assignment 2.3 (Pig Latin game) into a function, pig_latin, that takes parameters, 
instead of asking the user for input.
Make sure to return your answer rather than printing it.
"""


# I am going to and make some modification  my last assignemnt 
def pig_latin(input_word):
    VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    #split the input word and convert it to lower case
    first_letter = input_word[0].lower()
    #check if the first word in in vowels
    if first_letter in VOWELS: 
        #if the first word is vowel add hay and print it out
        print(input_word + "hay"  )
        check_input_ = input('Please enter "y or Yes" to continue the game or "No or any other word" to stop it:')
        lowercase_input = check_input_.lower()
        #check if the user want to continue to play the game
        if lowercase_input == 'y' or lowercase_input =='yes':
            #user input when they want to play again
            input_word = input('Please Enter a word: ')
            #Recursive Function 
            pig_latin(input_word)
        #thank you message if the user does not want to play the game      
        else:
            return print('Thank you for playing Pig latin game. \n')
                
    else:
        #if the first word is not a vowel, remove the first word and add it at the end and add ay at the end too and print
        print(input_word[1:] + input_word[0] + "ay"  )
        check_input_ = input('Please enter "y or Yes" to continue the game or "No or any other word" to stop it:')
        #check if the user want to continue to play the game
        lowercase_input = check_input_.lower()
        if lowercase_input == 'y' or lowercase_input =='yes':
            #user input when they want to play again
            input_word = input('Please Enter a word: ')
            #Recursive Function 
            pig_latin(input_word)
        #thank you message if the user does not want to play the game    
        else:
            return print('Thank you for playing Pig latin game. \n')

#let's call the function and pass an input
input_word = input('Please Enter a word: ')
pig_latin(input_word)
# In[ ]:


"""
Question 3.2 Write a function, roll_dice, that takes in 2 parameters - the number of sides of the die, 
and the number of dice to roll - and generates random roll values for each die rolled. 
Print out each roll and then return the string “That’s all!” An example output:

>>> roll_dice(6, 3)

4

1

6

That’s all!

(Note: For this function, we’ll use the random module. At the top of your code, add the line -  import random.
To generate a random integer, use the function randint, which works like this: random.randint(lo, hi),
where lo and hi are integers that tell the code the range in which to generate a random integer (this range is inclusive).)
"""
#take two parametrs for the number of sides of the die, and the number of dice to roll
import random
def roll_dice(dice_sides, dice_rolls):
    
    for x in range(dice_rolls):
        print(random.randint(1,dice_sides))
    print("That's all!")
    
    
#let's test the function by passing two user input

#user input for the number of sides of the die
dice_sides_input = input("Please enter the number of sides of the die: ")

#user input for the the number of dice to roll
dice_rolls_input =input("Please enter the number of dice to roll: ")    

#call the function and pass these two user input
roll_dice(int(dice_sides_input),int(dice_rolls_input))


# In[ ]:


"""
Question 3.3 Write a function, is_palindrome, which takes a string as parameter, and returns True 
if the string is a palindrome (meaning it is the same forwards as backwards), and False otherwise. 
For an additional challenge, try writing this as a recursive function.
"""
#i am going to create a function that reverse any given word
def reverse_a_word(input_word):
    return input_word[::-1]

#sometimes we might have a word with some additional character. like: dad/ or dad. or dad, or dad@ the remove_unnecessary function 
#will help us to remove any additional unnecessary things from the given word
def remove_unnecessary(inputs):
    inputs = inputs.lower()
    replace_these =  (' ', '.', '?', '!', ':', ';', '-', '—', '(', ')', '[', ']', '’', '“', '”', '/', ',', '"')
    for x in replace_these:
        inputs = inputs.replace(x, '')
    return inputs

#check if the word is palindrome
def is_palindrome(input_word):
    return remove_unnecessary(input_word) == reverse_a_word(remove_unnecessary(input_word))

#let's call the function and pass any word to check if the word is palindrome
user_input = input('Please enter a word to check if it is a Palindrome: ')
print(is_palindrome(user_input))


# In[ ]:


### Recursive Function


# In[5]:


"""
For an additional challenge, try writing this as a recursive function.
"""
#sometimes we might have a word with some additional character. like: dad/ or dad. or dad, or dad@ the remove_unnecessary function 
#will help us to remove any additional unnecessary things from the given word
def remove_unnecessary(inputs):
    inputs = inputs.lower()
    remove_these =  (' ', '.', '?', '!', ':', ';', '-', '—', '(', ')', '[', ']', '’', '“', '”', '/', ',', '"')
    for x in remove_these:
        inputs = inputs.replace(x, '')
    return inputs

def is_Palindrome_recursive_function(input_word):
    convert_input =remove_unnecessary(input_word)
    if len(convert_input) <= 1:
        return True
    if convert_input[0] == convert_input[len(convert_input) - 1]:
        #returns true if the input string is palindrome
        return is_Palindrome_recursive_function(convert_input[1:len(convert_input) - 1])
    else :
        #otherwise it will return false
      return False

#testing the recursive function
user_input = input('Please enter a word to check if it is a Palindrome: ')
print(is_Palindrome_recursive_function(user_input))

