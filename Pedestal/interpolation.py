#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


import sys

table_name=sys.argv[1]



# In[6]:


ref_table=open("ref_table.txt","r")
recent_table=open(table_name,"r")


# In[7]:


lines_ref = []
lines_rec = []


for line in ref_table:
    v = line.split()
    lines_ref.append(v)
    
for line in recent_table:
    v = line.split()
    lines_rec.append(v)


# In[8]:


tag_missing = 0
missing_channels = []
for ii in range(len(lines_ref)):
    for jj in range(len(lines_rec)):
        is_same = int(lines_ref[ii][0:4] == lines_rec[jj][0:4])
        tag_missing = tag_missing + is_same
    if (tag_missing != 1):
        missing_channels.append(lines_ref[ii])
    tag_missing = 0


# In[9]:


miss_array=np.array(missing_channels)


# In[10]:


sur = np.zeros([len(miss_array),9,4])

pm1 = [-1,-1,-1,0,0,0,1,1,1]
pm2 = [-1,0,1,-1,0,1,-1,0,1] 

for ii in range(len(miss_array)):
    for jj in [-1,0,1]:
        for kk in [-1,0,1]:
            for ll in range(9):
                sur[ii,ll,0] = int(miss_array[ii,0])+pm1[ll]
                sur[ii,ll,1] = int(miss_array[ii,1])+pm2[ll]
                sur[ii,ll,2] = int(miss_array[ii,2])
                if miss_array[ii,3] == "HE":
                    sur[ii,ll,3] = 0
                if miss_array[ii,3] == "HB":
                    sur[ii,ll,3] = 1
                if miss_array[ii,3] == "HF":
                    sur[ii,ll,3] = 2
                if miss_array[ii,3] == "HO":
                    sur[ii,ll,3] = 3
                else:
                    sur[ii,ll,3] == -999


# In[11]:


sur_list = sur.astype(int).astype(str).tolist()


# In[12]:


for ii in range(len(sur_list)):
    for jj in range(len(sur_list[ii])):
        if (sur_list[ii][jj][3] != "0")and(sur_list[ii][jj][3] != "1")and(sur_list[ii][jj][3] != "2")and(sur_list[ii][jj][3] != "3"):
            sur_list[ii][jj][3] = "-999"
        if sur_list[ii][jj][3] == "0":
            sur_list[ii][jj][3] = "HE"
        if sur_list[ii][jj][3] == "1":
            sur_list[ii][jj][3] = "HB"
        if sur_list[ii][jj][3] == "2":
            sur_list[ii][jj][3] = "HF"
        if sur_list[ii][jj][3] == "3":
            sur_list[ii][jj][3] = "HO"


# In[13]:


miss_list = missing_channels


# In[14]:


data_sur_list = []

for ii in range(len(lines_rec)):
    for jj in range(len(sur_list)):
        for kk in range(len(sur_list[jj])):
            if lines_rec[ii][0:4] == sur_list[jj][kk]:
                data_sur_list.append([np.array(lines_rec[ii][4:-1]), sur_list[jj][4]] )


# In[15]:


sur_mean = []
for ii in range(len(miss_list)):
    sum_B0 = np.zeros(8)
    i = 0 
    for jj in range(len(data_sur_list)):

        #key_1 = float(mis[ii][0]) + np.sqrt(2)*float(mis[ii][1])+np.sqrt(2)*float(mis[ii][2])
        #key_2 = float(B[jj][1][0]) + np.sqrt(2)*float(B[jj][1][1])+np.sqrt(2)*float(B[jj][1][2])
        
        if miss_list[ii][0:4] == data_sur_list[jj][1]:
            sum_B0 = sum_B0 + data_sur_list[jj][0].astype(float)
            i = i + 1
            #print("-----")
            #print(mis[ii])
            #print(B[jj][1])
            #print("-----")

    
    if i != 0:
        sur_mean.append([(1/i)*sum_B0, miss_list[ii]])
    #if i == 0:


# In[16]:


for ii in range(len(lines_rec)):
    if lines_rec[ii][0:4] == ['-19', '16','5','HE']:
        print(lines_rec[ii])
        avg_mean = (float(lines_rec[ii][5]) + float(lines_rec[ii][6]) +float(lines_rec[ii][7]))/3
        avg_width = (float(lines_rec[ii][9]) + float(lines_rec[ii][10]) +float(lines_rec[ii][11]))/3
        lines_rec[ii][4] = format(float(avg_mean),".3f")
        lines_rec[ii][8] = format(float(avg_width),".3f")
        print(lines_rec[ii])
        


# In[17]:


add_line = []
for ii in range(len(lines_rec)):
    lines = ""
    if ii == 0:
        lines = lines+lines_rec[0][0]
        lines = lines +" "
        lines = lines+lines_rec[0][1]
        lines = lines +"  "
        lines = lines+lines_rec[0][2]
        lines = lines +" "
        lines = lines+lines_rec[0][3]
        lines = lines +" "
        lines = lines+lines_rec[0][4]
        lines = lines +" "
        lines = lines+lines_rec[0][5]
        lines = lines +" "
        lines = lines+lines_rec[0][6]
        lines = lines +" "
        
        
    if ii == 1:
        lines = lines+lines_rec[1][0]
        lines = lines +"             "
        lines = lines+lines_rec[1][1]
        lines = lines +"             "
        lines = lines+lines_rec[1][2]
        lines = lines +"             "
        lines = lines+lines_rec[1][3]
        lines = lines +"             "
        lines = lines+lines_rec[1][4]
        lines = lines +"     "
        lines = lines+lines_rec[1][5]
        lines = lines +"     "
        lines = lines+lines_rec[1][6]
        lines = lines +"     "
        lines = lines+lines_rec[1][7]
        lines = lines +"     "
        lines = lines+lines_rec[1][8]
        lines = lines +" "
        lines = lines+lines_rec[1][9]
        lines = lines +" "
        lines = lines+lines_rec[1][10]
        lines = lines +" "
        lines = lines+lines_rec[1][11]
        lines = lines +" "
        lines = lines+lines_rec[1][12]
        lines = lines +" "
        lines = lines+lines_rec[1][11]
        lines = lines +"      "
        
        
    if ii>1:
        if len(lines_rec[ii][0]) == 1:
            lines = lines + "                "
        if len(lines_rec[ii][0]) == 2:
            lines = lines + "               "
        if len(lines_rec[ii][0]) == 3:
            lines = lines + "              "
        
        lines = lines + str(lines_rec[ii][0])
    
        if len(lines_rec[ii][1]) == 1:
            lines = lines + "               "
        if len(lines_rec[ii][1]) == 2:
            lines = lines + "              "
        lines = lines + str(lines_rec[ii][1])
        
        lines = lines + "               "
        
        lines = lines + str(lines_rec[ii][2])
        
        lines = lines + "              "
        lines = lines + lines_rec[ii][3]
        
        if len(format(float(lines_rec[ii][4]),".3f")) == 7:
            lines = lines + "  "
        if len(format(float(lines_rec[ii][4]),".3f")) == 6:
            lines = lines + "   "
        if len(format(float(lines_rec[ii][4]),".3f")) == 5:
            lines = lines + "    "
        lines = lines + format(float(lines_rec[ii][4]),".3f")
        
        if len(format(float(lines_rec[ii][5]),".3f")) == 7:
            lines = lines + "  "   
        if len(format(float(lines_rec[ii][5]),".3f")) == 6:
            lines = lines + "   "
        if len(format(float(lines_rec[ii][5]),".3f")) == 5:
            lines = lines + "    "
        lines = lines + format(float(lines_rec[ii][5]) ,".3f")
        
        if len(format(float(lines_rec[ii][6]),".3f")) == 7:
            lines = lines + "  "   
        if len(format(float(lines_rec[ii][6]),".3f")) == 6:
            lines = lines + "   "
        if len(format(float(lines_rec[ii][6]),".3f")) == 5:
            lines = lines + "    "
        lines = lines + format(float(lines_rec[ii][6]), ".3f")
        
        if len(format(float(lines_rec[ii][7]),".3f")) == 7:
            lines = lines + "  "   
        if len(format(float(lines_rec[ii][7]),".3f")) == 6:
            lines = lines + "   "
        if len(format(float(lines_rec[ii][7]),".3f")) == 5:
            lines = lines + "    "
        lines = lines + format(float(lines_rec[ii][7]), ".3f")
        
        lines = lines + "   "
        lines = lines + format(float(lines_rec[ii][8]),".3f")
        
        lines = lines + "   "
        lines = lines + format(float(lines_rec[ii][9]),".3f")
        
        lines = lines + "   "
        lines = lines + format(float(lines_rec[ii][10]), ".3f")
        
        lines = lines + "   "
        lines = lines + format(float(lines_rec[ii][11]), ".3f")
        
        lines = lines + "   "
        lines = lines + lines_rec[ii][12]
    add_line.append(lines)


# In[18]:


missing_list=[]
for ii in range(len(sur_mean)):
    lines = ""
    if len(sur_mean[ii][1][0]) == 1:
        lines = lines + "                "
    if len(sur_mean[ii][1][0]) == 2:
        lines = lines + "               "
    if len(sur_mean[ii][1][0]) == 3:
        lines = lines + "              "
        
    lines = lines + str(sur_mean[ii][1][0])
    
    if len(sur_mean[ii][1][1]) == 1:
        lines = lines + "               "
    if len(sur_mean[ii][1][1]) == 2:
        lines = lines + "              "
    lines = lines + str(sur_mean[ii][1][1])
    
    lines = lines + "               "
    
    lines = lines + str(sur_mean[ii][1][2])
    
    lines = lines + "              "
    lines = lines + sur_mean[ii][1][3]
    
    if(len(format(float(sur_mean[ii][0][0]),".3f")) == 7):
        lines = lines + "  "
    if(len(format(float(sur_mean[ii][0][0]),".3f")) == 6):
        lines = lines + "   "
    if(len(format(float(sur_mean[ii][0][0]),".3f")) == 5):
        lines = lines + "    "
    lines = lines + format(float(sur_mean[ii][0][0]),".3f")
    
    if(len(format(float(sur_mean[ii][0][1]),".3f")) == 7):
        lines = lines + "  "
    if(len(format(float(sur_mean[ii][0][1]),".3f")) == 6):
        lines = lines + "   "
    if(len(format(float(sur_mean[ii][0][1]),".3f")) == 5):
        lines = lines + "    "
    lines = lines + format(float(sur_mean[ii][0][1]) ,".3f")   
    
    if(len(format(float(sur_mean[ii][0][2]),".3f")) == 7):
        lines = lines + "  "
    if(len(format(float(sur_mean[ii][0][2]),".3f")) == 6):
        lines = lines + "   "
    if(len(format(float(sur_mean[ii][0][2]),".3f")) == 5):
        lines = lines + "    "
    lines = lines + format(float(sur_mean[ii][0][2]), ".3f")
    
    if(len(format(float(sur_mean[ii][0][3]),".3f")) == 7):
        lines = lines + "  "
    if(len(format(float(sur_mean[ii][0][3]),".3f")) == 6):
        lines = lines + "   "
    if(len(format(float(sur_mean[ii][0][3]),".3f")) == 5):
        lines = lines + "    "
    lines = lines + format(float(sur_mean[ii][0][3]), ".3f")
    
    lines = lines + "   "
    lines = lines + format(float(sur_mean[ii][0][4]),".3f")
    lines = lines + "   "
    lines = lines + format(float(sur_mean[ii][0][5]),".3f")
    lines = lines + "   "
    lines = lines + format(float(sur_mean[ii][0][6]), ".3f")
    lines = lines + "   "
    lines = lines + format(float(sur_mean[ii][0][7]), ".3f")
    lines = lines + "   "
    lines = lines + missing_channels[ii][-1]
    add_line.append(lines)
    missing_list.append(lines)


# In[19]:


output_name = table_name.replace(".txt","_interploated.txt")
missing_name = table_name.replace(".txt","_missingChannels.txt")


# In[20]:


output_name


# In[21]:


missing_name


# In[22]:


missingChannels = open(missing_name,"w")
for ii in range(len(missing_list)):
    missingChannels.write(missing_list[ii] + "\n")
    
missingChannels.close()


# In[23]:


output = open(output_name,"w")
for ii in range(len(add_line)):
    output.write(add_line[ii] + "\n")
    
output.close()


# In[ ]:





# In[ ]:




