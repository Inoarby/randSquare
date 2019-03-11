
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot as plt


# In[225]:


colors = np.array([(255, 102, 102), (255, 140, 102), (255, 179, 102), (255, 217, 102), (255, 255, 102), (217, 255, 102), 
                  (179, 255, 102), (140, 255, 102), (102, 255, 102), (102, 255, 140), (102, 255, 179), (102, 255, 217), 
                  (102, 255, 255), (102, 217, 255), (102, 204, 255), (102, 179, 255), (102, 140, 255), (102, 102, 255), 
                  (140, 102, 255), (179, 102, 255), (217, 102, 255), (255, 102, 255), (255, 102, 217), (255, 102, 179), 
                  (255, 102, 140), (255, 102, 102)])/255


# In[16]:


row = 6
column = 6
step = 50

img = np.zeros((row*step, column*step, 4), 'float32')

for i in range(row):
    for j in range(column):
        img[i*step:(i+1)*step, j*step:(j+1)*step, 0:3] = colors[np.random.randint(colors.shape[0]), :]
        img[i*step:(i+1)*step, j*step:(j+1)*step, 3] = 0.5

for k in range(5):
    r = np.random.randint(row)
    c = np.random.randint(column)
    img[r*step:(r+1)*step, c*step:(c+1)*step, 3] = 0
plt.imshow(img)


# In[287]:


plt.imsave('randcolor.png', img)


# In[579]:


block_num = 10
r = 50
c = 50
img = np.zeros((r, c, 4), 'float32')

for i in range(block_num):
    r_position = np.random.randint(0, r)
    c_position = np.random.randint(0, c)
    height = np.random.randint(0, r-r_position)
    length = np.random.randint(0, c-c_position)
    
    color_index = np.random.randint(colors.shape[0])
    img[r_position : r_position+height, c_position : c_position+length, 0:3] += colors[color_index, :]
    img[r_position : r_position+height, c_position : c_position+length, 3] = np.random.randn() % 1

img[:, :, 0:3] %= 1
plt.imshow(img)


# In[580]:


plt.imsave('randsquare.png', img)

