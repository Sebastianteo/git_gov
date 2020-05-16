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

def processing_fn(x):

	try:
		#remove leading and trailing whitespace of the name 
		name_list = x['name'].strip()
		#split by the space inbetween the first_name and the last_name
		name_list = name_list.split(' ')

		#This will take cares of people who did not put their last name.
		if len(name_list) == 1:
			first_name = name_list[0]
			last_name = None

		#This will take cares of people who put thier middle name. 
		elif len(name_list) >= 2:
			first_name = name_list[0]
			last_name = name_list[-1]
            
		x['first_name'] = first_name
		x['last_name'] = last_name

	except Exception as e:
		print('error occured in processing_fn',e)

	else:
		return(x)

df = df.apply(processing_fn,axis=1)
print(df.head())