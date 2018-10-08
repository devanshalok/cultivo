import numpy as np
import pandas as pa
import matplotlib.pyplot as plt
from minor import *
#from datset_create import filtering
#%%
datset=pa.read_csv('datasets/agricuture-crops-production-in-india/datafile(2).csv',header=0)
#%%
crops=['rice','wheat','sugarcane','cotton','groundnut','tea','coffee','bajra','soyabean','maize','barley','mustard','peas','ragi','jowar','coconut','jute','rubber']
for i in range(0,len(crops)):
    crops[i]=crops[i].capitalize()
    #%%
g=datset[datset.Crop.isin(crops)]
#dat_sample=filtering(datset)