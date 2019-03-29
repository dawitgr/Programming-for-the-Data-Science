#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dawit Reda
#ID#10189420
#Module 2.4 Assignment
#Programming for the Data Science
#Submitted to Dr. Daniel Wu


# In[2]:


#Quesion 2.4 Write a program to combine the following two lists into a dictionary 
#(hint: what should the keys, and what should the values, of this dictionary be? ):
# NAMES = [’Alice’, ’Bob’, ’Cathy’, ’Dan’, ’Ed’, ’Frank’, ’Gary’, ’Helen’, ’Irene’, ’Jack’, ’Kelly’, ’Larry’] 
#AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
# These lists match up, so Alice’s age is 20, Bob’s age is 21, and so on.


# In[36]:


def dictionary_ages_names():
    #let's assume the Age as a keys
    AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
    #and the Names as a values
    NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry'] 
    #zip the name and age and store in dict
    dictionary = dict(zip(NAMES, AGES))
    #Iterate the dictionary to print name and age 
    for key in dictionary:
        #concatnate verb s at the end of each key to make it like Alice's
        concatnate = key + "'s"
        #print out the name and age
        print(concatnate,'age is', dictionary[key])

#let's initializer method to print out the the dictionary
dictionary_ages_names()    
    


# In[ ]:




