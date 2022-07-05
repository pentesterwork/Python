#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Strings
abubakar='first caliph!'
print(abubakar)


# In[6]:


abubakar="First Caliph!!"
print(abubakar)


# In[26]:


#String Problem Handling

#When Python sees a qoutation mark (either a single or double qoute), it expects a string to start following 
#the first mark and the string to end after the next matching qoutation mark (either single or double)
#on that line.

silly_string='''He said,"Aren't can't shouldn't wouldn't."'''
print(silly_string)


# In[25]:


#Adding a backslash \ or escaping
#Escaping strings can make harder to read, so it's probably better to use multiple strings.
#single qoute string
single_qoute_string='He said,"Aren\'t can\'t shouldn\'t wouldn\'t."'
print(single_qoute_string)


# In[19]:


#double qoute strings
double_qoute_string="He said,\"Aren't can't shouldn't wouldn't.\""
print(double_qoute_string)


# In[24]:


#Embedding Values in Strings
rupees=1000
message='I have %s Rs.'
print(message % rupees)


# In[22]:


nums='What did the number %s say to the number %s? Nice belt!'
print(nums % (0,8))


# In[23]:


#Multiplying Strings

print(10 * 'a')


# In[35]:


#Make fun with this code

spaces=' '*25
print('%s 12 DHA Phase 5 '%spaces)
print('%s Clifton' %spaces)
print('%s West Snoring' %spaces)
print()
print()
print('Dear Sir')
print()
print('I wish to report that tiles are missing from the')
print('outside toilet roof.')
print('I think it was bad wind the other night that blew them away.')
print('Regards')
print('Sharfoo')


# In[38]:


#Make Fuun stuff

print(50*'Air Universiy Islamabad ')


# In[39]:


#List vs. String

sharfoo_list='sabzee, fruit, aloo, chai'
print(sharfoo_list)


# In[44]:


#Creting a List
#Creating a list takes a bit more typing than creating a string, but a list is more
#useful than a string because it can be manipulated.
#For Example we can print the third item in the list.

sharfoo_list=['Sabzee', 'fruit', 'aloo', 'chai']
print(sharfoo_list[2])



# In[43]:


sharfoo_list=['Sabzee', 'fruit', 'aloo', 'chai']
print(sharfoo_list[0:3])


# In[47]:


#List can store all sorts of items, like numbers
#some_numbers=[1,2,3,4,10,20]
#They can also hold strings:
#some_strings=['Which','Witch','is']

#List strings and number example
numbers_and_strings=['Which',3,'Witch',5,'is']
print(numbers_and_strings)


# In[1]:


#Adding Items to list 

numbers=[1,2,3]
strings=['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'score']
mylist=[numbers,strings]
print(mylist)


# In[2]:


#Adding items to a list
#Before adding an item to a list:
wizard_list=['spider legs', 'toe of frog', 'egg of newt', 'bat wing', 'slug butter', 'snake dandruff']
print(wizard_list)


# In[3]:


#After adding item to a list via.append
wizard_list=['spider legs', 'toe of frog', 'egg of newt', 'bat wing', 'slug butter', 'snake dandruff']
wizard_list.append('bear burp')
print(wizard_list)


# In[11]:


#Challenge!
#Now add the following to the previous list and print.
#wizard_list.append('mandrake')
#wizard_list.append('hemlock')
#wizard_list.append('swamp gas')

wizard_list=['spider legs', 'toe of frog', 'egg of newt', 'bat wing', 'slug butter', 'snake dandruff']
wizard_list.append('bear burp')
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)


# In[12]:


#Removing Item from the list
#Remeber that positions start at zero, so wizard_list[5] actually refer to the sixth item in the list.
wizard_list=['spider legs', 'toe of frog', 'egg of newt', 'bat wing', 'slug butter', 'snake dandruff']
wizard_list.append('bear burp')
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
del wizard_list[5]
print(wizard_list)


# In[13]:


#List Arithmetic
#We can join two lists by using +

list1=[1,2,3,4]
list2=['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'score']
print(list1+list2)


# In[14]:


#We can also add the two lists and set the result equal to another variable.
list1=[1,2,3,4]
list2=['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'score']
list3=list1+list2
print(list3)


# In[15]:


#We can multiply a list by a number. For example, to multiply list1 by 5, we write list1*5
#-----------------------------------------------------------------------------------------
list1=[1,2]
print(list1*5)


# In[17]:


#Tuples 
#A tuple is like a list that uses parentheses, as in this example
fibs=(1,2,3,4,5)
print(fibs[3])


# In[18]:


#Creating a map in Python
favorite_sports=['Ali,Football','Omer,Basketball','Osman,Baseball','Abu bakar,Netball','Fatima, Badminton','Faizan,Rugby']
print(favorite_sports)


# In[19]:


#Modifying a value in a map
#if we store this same information in a map, with the person's name as the key
#and their favorite sport as the valuue, the Python code would look like this.
favorite_sports={'Ali':'Football',
                 'Omer':'Basketball',
                 'Osman':'Baseball',
                 'Abu bakar':'Netball',
                 'Fatima':'Badminton',
                 'Faizan':'Rugby'}
print(favorite_sports)


# In[20]:


#We use colons to separate each key from its value, and each key and value is surrounded by single quotes.
#Notice, too that the items in a map are enclosed in braces({}), not parentheses or squre brackets.
#Now to get Ali favorite sport, we access ou rmap favorite_sports using his name as 

favorite_sports={'Ali':'Football',
                 'Omer':'Basketball',
                 'Osman':'Baseball',
                 'Abu bakar':'Netball',
                 'Fatima':'Badminton',
                 'Faizan':'Rugby'}
print(favorite_sports['Ali'])


# In[21]:


#Deleting a value in the map
favorite_sports={'Ali':'Football',
                 'Omer':'Basketball',
                 'Osman':'Baseball',
                 'Abu bakar':'Netball',
                 'Fatima':'Badminton',
                 'Faizan':'Rugby'}
del favorite_sports['Ali']
print(favorite_sports)


# In[23]:


#Replacing a value in a map
favorite_sports={'Ali':'Football',
                 'Omer':'Basketball',
                 'Osman':'Baseball',
                 'Abu bakar':'Netball',
                 'Fatima':'Badminton',
                 'Faizan':'Rugby'}
favorite_sports['Faizan']='Cricket'
print(favorite_sports)


#We can replace the favorite sport of Rugby with Cricket by using the key Faizan.
#As you can see, working with maps is kind of like working with list and tuples, except that you cannot join maps with plus
#operator(+). If you try to do that, you will get an error message.


# In[ ]:





# In[ ]:




