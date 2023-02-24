#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#AUTOMATIC FILE SORTER IN FILE EXPLORER


# In[19]:


import os, shutil    #shutil helps us move files


# In[20]:


path = r"C:/Users/Emmanuel Tetteh/Desktop/pythtut/"  #Always change \ to / for this to work


# In[21]:


file_name = os.listdir(path)          #print all files in that path
print(file_name)


# In[18]:


folder_names = ['text files', 'image files', 'pdf files']     #loop through the list, if folder name in list doesnt exist, then create it
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):        
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
for file in file_name: 
    if '.pdf'in file and not os.path.exists(path + "pdf files" + file):    #if .pdf is in file_name but that file isnt in the pdf folder
                                                                           #then move it into the pdf folder
        shutil.move(path + file, path + "pdf files/" + file)
    elif '.png'in file and not os.path.exists(path + "png files" + file):
        shutil.move(path + file, path + "png files/" + file)
    elif '.txt'in file and not os.path.exists(path + "txt files" + file):
        shutil.move(path + file, path + "txt files/" + file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




