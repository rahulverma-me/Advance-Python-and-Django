#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
import string

def get_random_password_string(letters_count=6, digits_count=4,splchar_count=2):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))
    sample_str += ''.join((random.choice(string.punctuation) for i in range(splchar_count)))

    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

get_random_password_string()


# In[ ]:





# In[ ]:





# In[ ]:




