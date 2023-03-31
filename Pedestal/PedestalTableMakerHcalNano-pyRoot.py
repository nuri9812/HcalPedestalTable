#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import ROOT
import sys

# In[2]:


input_file = sys.argv[1]
hcalNano = ROOT.TFile.Open(input_file)
TTree = hcalNano.Get("Events")


# In[3]:


def make_arrayes(Branches):
    event_list = []     
    for ii in range(TTree.GetEntries()):
        TTree.GetEntry(ii)
        branch_list = []
        for jj in range(len(Branches)):
            channel_list = []
            for kk in range(len(Branches[jj])):
                
                channel_list.append(Branches[jj][kk])
            
            branch_list.append(channel_list)
        event_list.append(branch_list)
        
    return(np.array(event_list).transpose(1,0,2))


# In[4]:


Branches_HB = [TTree.DigiHB_fc0, TTree.DigiHB_fc1,TTree.DigiHB_fc2,TTree.DigiHB_fc3,TTree.DigiHB_fc4,
           TTree.DigiHB_fc5,TTree.DigiHB_fc6,TTree.DigiHB_fc7,TTree.DigiHB_capid0, TTree.DigiHB_capid1,
            TTree.DigiHB_capid2,TTree.DigiHB_capid3,TTree.DigiHB_capid4,TTree.DigiHB_capid5,TTree.DigiHB_capid6,
            TTree.DigiHB_capid7, TTree.DigiHB_ieta, TTree.DigiHB_iphi, TTree.DigiHB_depth, TTree.DigiHB_rawId]

Branches_HE = [TTree.DigiHE_fc0, TTree.DigiHE_fc1,TTree.DigiHE_fc2,TTree.DigiHE_fc3,TTree.DigiHE_fc4,
           TTree.DigiHE_fc5,TTree.DigiHE_fc6,TTree.DigiHE_fc7,TTree.DigiHE_capid0, TTree.DigiHE_capid1,
            TTree.DigiHE_capid2,TTree.DigiHE_capid3,TTree.DigiHE_capid4,TTree.DigiHE_capid5,TTree.DigiHE_capid6,
            TTree.DigiHE_capid7, TTree.DigiHE_ieta, TTree.DigiHE_iphi, TTree.DigiHE_depth, TTree.DigiHE_rawId]

Branches_HO = [TTree.DigiHO_fc0, TTree.DigiHO_fc1,TTree.DigiHO_fc2,TTree.DigiHO_fc3,TTree.DigiHO_fc4,
           TTree.DigiHO_fc5,TTree.DigiHO_fc6,TTree.DigiHO_fc7,TTree.DigiHO_fc8,TTree.DigiHO_fc9,TTree.DigiHO_capid0, TTree.DigiHO_capid1,
            TTree.DigiHO_capid2,TTree.DigiHO_capid3,TTree.DigiHO_capid4,TTree.DigiHO_capid5,TTree.DigiHO_capid6,
            TTree.DigiHO_capid7,TTree.DigiHO_capid8,TTree.DigiHO_capid9,TTree.DigiHO_ieta, TTree.DigiHO_iphi, TTree.DigiHO_depth, TTree.DigiHO_rawId]

Branches_HF= [TTree.DigiHF_fc0, TTree.DigiHF_fc1,TTree.DigiHF_fc2,TTree.DigiHF_capid0, TTree.DigiHF_capid1,
            TTree.DigiHF_capid2, TTree.DigiHF_ieta, TTree.DigiHF_iphi, TTree.DigiHF_depth, TTree.DigiHF_rawId]


# In[5]:


array_HB=make_arrayes(Branches_HB)


# In[6]:


array_HE=make_arrayes(Branches_HE)


# In[7]:


array_HO=make_arrayes(Branches_HO)

array_HF=make_arrayes(Branches_HF)


# In[ ]:





# In[63]:


#it returns boolian array that False for (eta,phi,depth) = (0,0,0) or (0-100,0).

not_000_HB = np.logical_or(array_HB[-2] != 0 , array_HB[-3] !=0, array_HB[-4] !=0)
not_000_HE = np.logical_or(array_HE[-2] != 0 , array_HE[-3] !=0, array_HE[-4] !=0)
not_000_HO = np.logical_or(array_HO[-2] != 0 , array_HO[-3] !=-100, array_HO[-4] !=0)
not_100_HO = np.logical_or(array_HO[-2] != 0 , array_HO[-3] !=0, array_HO[-4] !=0)
good_HO = np.logical_and(not_000_HO,not_100_HO)

not_000_HF = np.logical_or(array_HF[-2] != 0 , array_HF[-3] !=0, array_HF[-4] !=0)





# In[ ]:





# In[162]:


nch_HB=int(len(array_HB[0][not_000_HB])/1000)
nch_HE=int(len(array_HE[0][not_000_HE])/1000)
nch_HO=int(len(array_HO[0][good_HO])/1000)
nch_HF=int(len(array_HF[0][not_000_HF])/1000)


# In[ ]:





# In[64]:


cap0_HB = []
cap1_HB = []
cap2_HB = []
cap3_HB = []
for ii in range(8):
    if (int(np.mean(array_HB[ii+8][not_000_HB])) == 0):
        cap0_HB.append(array_HB[ii][not_000_HB].reshape(1000,nch_HB))
    if (int(np.mean(array_HB[ii+8][not_000_HB])) == 1):
        cap1_HB.append(array_HB[ii][not_000_HB].reshape(1000,nch_HB))
    if (int(np.mean(array_HB[ii+8][not_000_HB])) == 2):
        cap2_HB.append(array_HB[ii][not_000_HB].reshape(1000,nch_HB))
    if (int(np.mean(array_HB[ii+8][not_000_HB])) == 3):
        cap3_HB.append(array_HB[ii][not_000_HB].reshape(1000,nch_HB))


# In[65]:


cap0_HE = []
cap1_HE = []
cap2_HE = []
cap3_HE = []
for ii in range(8):
    if (int(np.mean(array_HE[ii+8][not_000_HE])) == 0):
        cap0_HE.append(array_HE[ii][not_000_HE].reshape(1000,nch_HE))
    if (int(np.mean(array_HE[ii+8][not_000_HE])) == 1):
        cap1_HE.append(array_HE[ii][not_000_HE].reshape(1000,nch_HE))
    if (int(np.mean(array_HE[ii+8][not_000_HE])) == 2):
        cap2_HE.append(array_HE[ii][not_000_HE].reshape(1000,nch_HE))
    if (int(np.mean(array_HE[ii+8][not_000_HE])) == 3):
        cap3_HE.append(array_HE[ii][not_000_HE].reshape(1000,nch_HE))


# In[73]:


cap0_HO = []
cap1_HO = []
cap2_HO = []
cap3_HO = []
for ii in range(10):
    if (int(np.mean(array_HO[ii+10][good_HO])) == 0):
        cap0_HO.append(array_HO[ii][good_HO].reshape(1000,nch_HO))
    if (int(np.mean(array_HO[ii+10][good_HO])) == 1):
        cap1_HO.append(array_HO[ii][good_HO].reshape(1000,nch_HO))
    if (int(np.mean(array_HO[ii+10][good_HO])) == 2):
        cap2_HO.append(array_HO[ii][good_HO].reshape(1000,nch_HO))
    if (int(np.mean(array_HO[ii+10][good_HO])) == 3):
        cap3_HO.append(array_HO[ii][good_HO].reshape(1000,nch_HO))


# In[74]:


cap0_HF = []
cap1_HF = []
cap2_HF = []
cap3_HF = []
for ii in range(3):
    if (int(np.mean(array_HF[ii+3][not_000_HF])) == 0):
                cap0_HF.append(array_HF[ii][not_000_HF].reshape(1000,nch_HF))
    if (int(np.mean(array_HF[ii+3][not_000_HF])) == 1):
                cap1_HF.append(array_HF[ii][not_000_HF].reshape(1000,nch_HF))
    if (int(np.mean(array_HF[ii+3][not_000_HF])) == 2):
                cap2_HF.append(array_HF[ii][not_000_HF].reshape(1000,nch_HF))
    if (int(np.mean(array_HF[ii+3][not_000_HF])) == 3):
                cap3_HF.append(array_HF[ii][not_000_HF].reshape(1000,nch_HF))


# In[100]:


len(np.mean(np.concatenate(tuple(cap0_HO), axis = 0) , axis = 0))


# In[105]:



# In[ ]:





# In[189]:


cap0_array = np.concatenate(tuple(cap0_HB), axis = 0)
cap1_array = np.concatenate(tuple(cap1_HB), axis = 0)
cap2_array = np.concatenate(tuple(cap2_HB), axis = 0)
cap3_array = np.concatenate(tuple(cap3_HB), axis = 0)


cap0 = np.mean(cap0_array, axis = 0)
cap1 = np.mean(cap1_array, axis = 0)
cap2 = np.mean(cap2_array, axis = 0)
cap3 = np.mean(cap3_array, axis = 0)

widthcap0=np.std(cap0_array, axis = 0)
widthcap1=np.std(cap1_array, axis = 0)
widthcap2=np.std(cap2_array, axis = 0)
widthcap3=np.std(cap3_array, axis = 0)

ieta = array_HB[-4][not_000_HB][:nch_HB].astype(int)
iphi = array_HB[-3][not_000_HB][:nch_HB].astype(int)
depth = array_HB[-2][not_000_HB][:nch_HB].astype(int)
rawId = array_HB[-1][not_000_HB][:nch_HB]

arr = []
for ii in range (len(rawId)):
    arr.append(format(rawId[ii].astype(int),"X"))
DetId = np.array(arr)

arr = []
for ii in range (len(rawId)):
    arr.append("HB")
Det = np.array(arr)

#format
cap0_f = np.array(["%.3f" % w for w in cap0.reshape(cap0.size)])
cap1_f = np.array(["%.3f" % w for w in cap1.reshape(cap1.size)])
cap2_f = np.array(["%.3f" % w for w in cap2.reshape(cap2.size)])
cap3_f = np.array(["%.3f" % w for w in cap3.reshape(cap3.size)])
widthcap0_f = np.array(["%.3f" % w for w in widthcap0.reshape(widthcap0.size)])
widthcap1_f = np.array(["%.3f" % w for w in widthcap1.reshape(widthcap1.size)])
widthcap2_f = np.array(["%.3f" % w for w in widthcap2.reshape(widthcap2.size)])
widthcap3_f = np.array(["%.3f" % w for w in widthcap3.reshape(widthcap3.size)])



table_HB = np.transpose(np.concatenate(([ieta],[iphi],[depth],[Det],[cap0_f],[cap1_f],[cap2_f],[cap3_f],[widthcap0_f],[widthcap1_f],[widthcap2_f],[widthcap3_f],[DetId]),axis=0))


# In[190]:


cap0_array = np.concatenate(tuple(cap0_HE), axis = 0)
cap1_array = np.concatenate(tuple(cap1_HE), axis = 0)
cap2_array = np.concatenate(tuple(cap2_HE), axis = 0)
cap3_array = np.concatenate(tuple(cap3_HE), axis = 0)


cap0 = np.mean(cap0_array, axis = 0)
cap1 = np.mean(cap1_array, axis = 0)
cap2 = np.mean(cap2_array, axis = 0)
cap3 = np.mean(cap3_array, axis = 0)

widthcap0=np.std(cap0_array, axis = 0)
widthcap1=np.std(cap1_array, axis = 0)
widthcap2=np.std(cap2_array, axis = 0)
widthcap3=np.std(cap3_array, axis = 0)

ieta = array_HE[-4][not_000_HE][:nch_HE].astype(int)
iphi = array_HE[-3][not_000_HE][:nch_HE].astype(int)
depth = array_HE[-2][not_000_HE][:nch_HE].astype(int)
rawId = array_HE[-1][not_000_HE][:nch_HE]

arr = []
for ii in range (len(rawId)):
    arr.append(format(rawId[ii].astype(int),"X"))
DetId = np.array(arr)

arr = []
for ii in range (len(rawId)):
    arr.append("HE")
Det = np.array(arr)

#format
cap0_f = np.array(["%.3f" % w for w in cap0.reshape(cap0.size)])
cap1_f = np.array(["%.3f" % w for w in cap1.reshape(cap1.size)])
cap2_f = np.array(["%.3f" % w for w in cap2.reshape(cap2.size)])
cap3_f = np.array(["%.3f" % w for w in cap3.reshape(cap3.size)])
widthcap0_f = np.array(["%.3f" % w for w in widthcap0.reshape(widthcap0.size)])
widthcap1_f = np.array(["%.3f" % w for w in widthcap1.reshape(widthcap1.size)])
widthcap2_f = np.array(["%.3f" % w for w in widthcap2.reshape(widthcap2.size)])
widthcap3_f = np.array(["%.3f" % w for w in widthcap3.reshape(widthcap3.size)])



table_HE = np.transpose(np.concatenate(([ieta],[iphi],[depth],[Det],[cap0_f],[cap1_f],[cap2_f],[cap3_f],[widthcap0_f],[widthcap1_f],[widthcap2_f],[widthcap3_f],[DetId]), axis =0))


# In[191]:


cap0_array = np.concatenate(tuple(cap0_HO), axis = 0)
cap1_array = np.concatenate(tuple(cap1_HO), axis = 0)
cap2_array = np.concatenate(tuple(cap2_HO), axis = 0)
cap3_array = np.concatenate(tuple(cap3_HO), axis = 0)


cap0 = np.mean(cap0_array, axis = 0)
cap1 = np.mean(cap1_array, axis = 0)
cap2 = np.mean(cap2_array, axis = 0)
cap3 = np.mean(cap3_array, axis = 0)

widthcap0=np.std(cap0_array, axis = 0)
widthcap1=np.std(cap1_array, axis = 0)
widthcap2=np.std(cap2_array, axis = 0)
widthcap3=np.std(cap3_array, axis = 0)

ieta = array_HO[-4][not_000_HO][:nch_HO].astype(int)
iphi = array_HO[-3][not_000_HO][:nch_HO].astype(int)
depth = array_HO[-2][not_000_HO][:nch_HO].astype(int)
rawId = array_HO[-1][not_000_HO][:nch_HO]

arr = []
for ii in range (len(rawId)):
    arr.append(format(rawId[ii].astype(int),"X"))
DetId = np.array(arr)

arr = []
for ii in range (len(rawId)):
    arr.append("HO")
Det = np.array(arr)

#format
cap0_f = np.array(["%.3f" % w for w in cap0.reshape(cap0.size)])
cap1_f = np.array(["%.3f" % w for w in cap1.reshape(cap1.size)])
cap2_f = np.array(["%.3f" % w for w in cap2.reshape(cap2.size)])
cap3_f = np.array(["%.3f" % w for w in cap3.reshape(cap3.size)])
widthcap0_f = np.array(["%.3f" % w for w in widthcap0.reshape(widthcap0.size)])
widthcap1_f = np.array(["%.3f" % w for w in widthcap1.reshape(widthcap1.size)])
widthcap2_f = np.array(["%.3f" % w for w in widthcap2.reshape(widthcap2.size)])
widthcap3_f = np.array(["%.3f" % w for w in widthcap3.reshape(widthcap3.size)])



table_HO = np.transpose(np.concatenate(([ieta],[iphi],[depth],[Det],[cap0_f],[cap1_f],[cap2_f],[cap3_f],[widthcap0_f],[widthcap1_f],[widthcap2_f],[widthcap3_f],[DetId]), axis=0))


# In[192]:


cap0_array = np.concatenate(tuple(cap0_HF), axis = 0)
cap1_array = np.concatenate(tuple(cap1_HF), axis = 0)
#cap2_array = np.concatenate(tuple(cap2_HF), axis = 0)
cap3_array = np.concatenate(tuple(cap3_HF), axis = 0)
#cap2_array = 0*cap0_array
cap2_array = np.mean((cap0_array,cap1_array,cap3_array),axis = 0)

cap0 = np.mean(cap0_array, axis = 0)
cap1 = np.mean(cap1_array, axis = 0)
cap2 = np.mean(cap2_array, axis = 0)
cap3 = np.mean(cap3_array, axis = 0)

widthcap0=np.std(cap0_array, axis = 0)
widthcap1=np.std(cap1_array, axis = 0)
widthcap2=np.std(cap2_array, axis = 0)
widthcap3=np.std(cap3_array, axis = 0)

ieta = array_HF[-4][not_000_HF][:nch_HF].astype(int)
iphi = array_HF[-3][not_000_HF][:nch_HF].astype(int)
depth = array_HF[-2][not_000_HF][:nch_HF].astype(int)
rawId = array_HF[-1][not_000_HF][:nch_HF]

arr = []
for ii in range (len(rawId)):
    arr.append(format(rawId[ii].astype(int),"X"))
DetId = np.array(arr)

arr = []
for ii in range (len(rawId)):
    arr.append("HF")
Det = np.array(arr)

#format
cap0_f = np.array(["%.3f" % w for w in cap0.reshape(cap0.size)])
cap1_f = np.array(["%.3f" % w for w in cap1.reshape(cap1.size)])
cap2_f = np.array(["%.3f" % w for w in cap2.reshape(cap2.size)])
cap3_f = np.array(["%.3f" % w for w in cap3.reshape(cap3.size)])
widthcap0_f = np.array(["%.3f" % w for w in widthcap0.reshape(widthcap0.size)])
widthcap1_f = np.array(["%.3f" % w for w in widthcap1.reshape(widthcap1.size)])
widthcap2_f = np.array(["%.3f" % w for w in widthcap2.reshape(widthcap2.size)])
widthcap3_f = np.array(["%.3f" % w for w in widthcap3.reshape(widthcap3.size)])



table_HF = np.transpose(np.concatenate(([ieta],[iphi],[depth],[Det],[cap0_f],[cap1_f],[cap2_f],[cap3_f],[widthcap0_f],[widthcap1_f],[widthcap2_f],[widthcap3_f],[DetId]),axis=0))


# In[ ]:






# In[193]:


table_all = np.concatenate((table_HB,table_HE,table_HO,table_HF),axis=0)


# In[ ]:





# In[ ]:





# In[194]:


header_str="U FC  << this is the unit \n              eta             phi             dep             det     cap0     cap1     cap2     cap3 widthcap0 widthcap1 widthcap2 widthcap3 widthcap2"


# In[195]:


fmt_list=['%17s','%16s','%16s','%16s','%9s','%9s','%9s','%9s','%9s','%9s','%9s','%9s','%11s']

np.savetxt("test.txt",table_all,fmt=fmt_list,header=header_str,delimiter='')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




