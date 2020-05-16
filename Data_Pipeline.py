#---------Import Libraries-------#
import pandas as pd
import numpy as np
import re
import sys

#--------Read csv file-----------#
df = pd.read_csv('./dataset.csv')

'''
Drop row if any of the column contains empty or nan value. 
This will delete any rows which do not have a name.
'''
df.dropna(inplace=True)

#Since, I drop the rows. I will reset the rolling numbering index value. 
df.reset_index(drop=True,inplace=True)

print(df.head())
print(df.info())