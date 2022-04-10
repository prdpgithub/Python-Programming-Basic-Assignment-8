#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.	Write a Python Program to Add Two Matrices?

 
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)


# In[2]:


#  2.	Write a Python Program to Multiply Two Matrices?

# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix   
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
     
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
 
# iterating by row of A
for i in range(len(A)):
 
    # iterating by column by B
    for j in range(len(B[0])):
 
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)


# In[3]:


#  3.	Write a Python Program to Transpose a Matrix?


# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


# In[4]:


# 4.	Write a Python Program to Sort Words in Alphabetic Order?


my_str = "Hello this Is an Example With cased letters"

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
   print(word)


# In[5]:


# 5.	Write a Python Program to Remove Punctuation From a String?

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)


# In[ ]:





# In[ ]:




