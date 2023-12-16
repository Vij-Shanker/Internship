#!/usr/bin/env python
# coding: utf-8

# In[164]:


import re


# **Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.**

# In[165]:


Text='Python Exercises, PHP exercises.'
replace=re.sub("\s|,|\.",":",Text)
print(replace)


# **Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.**
# 
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# Expected output-
# 0      hello world
# 1             test
# 2    four five six
# 

# In[166]:


import pandas as pd
import re
index=0
Dictionary={'SUMMARY':['hello, world!', 'XXXXX test', '123four, five:; six...']}
for text in Dictionary['SUMMARY']:
    DF=re.sub('[^a-z\s]', '',text)
    print(f"{index} {DF}")
    index+=1


# **Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.**

# In[167]:


pattern=re.compile(r'\w{4,}')
string='John McCarthy is one of the "founding fathers" of artificial intelligence, together with Alan Turing, Marvin Minsky, Allen Newell, and Herbert A. Simon. McCarthy, Minsky, Nathaniel Rochester and Claude E. Shannon coined the term "artificial intelligence" in a proposal that they wrote for the famous Dartmouth conference in Summer 1956. This conference started AI as a field.'
result=re.findall(pattern,string)
print(result)


# **Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.**

# In[173]:


import re
def words(string):
    pattern=re.compile(r'\b\w{3,5}\b')
    matches=re.findall(pattern,string)
    return matches

result=words('John McCarthy is one of the "founding fathers" of artificial intelligence, together with Alan Turing, Marvin Minsky, Allen Newell, and Herbert A. Simon. McCarthy, Minsky, Nathaniel Rochester and Claude E. Shannon coined the term "artificial intelligence" in a proposal that they wrote for the famous Dartmouth conference in Summer 1956. This conference started AI as a field.')
print(result)


# **Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.**

# In[228]:


import re
def parenthesis(strings):
    pattern=re.compile(r"[\(\)]")
    replace1=re.sub(pattern,"",strings)
    return replace1
stringlist=["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for strings in stringlist:
    result1=parenthesis(strings)
    print(result1)    


# **Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.**
# 
# **Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]**
# 
# 
# **Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]**
# 
# **Note- Store given sample text in the text file and then to remove the parenthesis area from the text.**
# 

# In[241]:


import os
import re

os.chdir("F:\\FlipRobo\\")

with open("sample.txt") as file:
    for line in file:
        paran = re.sub((r'\([^)]*\)'), '', line)
        print(paran)


# **Question 7- Write a regular expression in Python to split a string into uppercase letters.**
# 
# **Sample text: “ImportanceOfRegularExpressionsInPython”**
#     
# **Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]**
# 

# In[253]:


import re
text="ImportanceOfRegularExpressionsInPython"
s=re.findall('[A-Z][a-z]*',text)
print(s)


# **Question 8- Create a function in python to insert spaces between words starting with numbers.**
# 
# **Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"**
# 
# **Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython**
# 

# In[275]:


import re

def spaces(strings):
    space = re.sub(r'\d', ' \\g<0>', strings)
    return space

result = spaces('RegularExpression1IsAn2ImportantTopic3InPython')
print(result)


# **Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.**
# 
# **Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"**
#     
# **Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython**
# 

# In[278]:


import re

def spaces(strings):
    space = re.sub(r'\d', ' \\g<0> ', strings)
    return space

result = spaces('RegularExpression1IsAn2ImportantTopic3InPython')
print(result)


# **Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.**
# 
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# In[316]:


import re
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')

six_letters = re.findall(r'\b\w{6}\b', ' '.join(df['Country']))
print(six_letters)


# In[ ]:




