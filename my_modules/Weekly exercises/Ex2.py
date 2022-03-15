#!/usr/bin/env python
# coding: utf-8

# In[13]:


#1A
import csv
import platform


def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.read()
        print(content)
    
print_file_content("../../../data/iris_data.csv")


# In[16]:


#1B
def write_list_to_file(output_file, *lst):
    with open(output_file, 'w') as f_obj:
        for i in lst:
            f_obj.write(i + '\n')
list_to_file = ["1", "2", "3"]
write_list_to_file("output_file", "list_to_file", "dsad", "123")


# In[1]:


#1C
def read_csv(input_file):
    with open(input_file) as f_obj:
        #lines = f_obj.readlines()
        #print(lines)
            print([line.strip() for line in f_obj])

read_csv("Ex2_1C.csv")


# In[2]:


#2A
import argparse
if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to csv file')
    
    args = parser.parse_args()


