#!/usr/bin/env python
# coding: utf-8

# In[36]:


#Dawit Reda
#ID#10189420
#Module 2.1 Assignment
#Programming for the Data Science
#Re-Submitting to Dr. Daniel Wu


# In[37]:


#2.1 Using a for loop, write a program that prints out the decimal equivalents of 1/2, 1/3, 1/4, ..., 1/10. 


# In[12]:


def print_decimal_equivalents():
    #let's store the range between 1 to 10 in a range_value
    range_value = range(1,11)
    for x in range_value:
        #convert the number to string
        given_number = "1/" + str(x)
        decimal_equivalents_value = given_number + " is equal to decimal value of  " + str(1.0/x)
        print(decimal_equivalents_value)
#call the function and print out the result      
print_decimal_equivalents()


# In[ ]:




