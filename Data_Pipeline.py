#---------Import Libraries-------#
import pandas as pd
import numpy as np
import re
import sys

#--------Read csv file-----------#
df = pd.read_csv('C:/Users/HP/Desktop/gov_tech/dataset.csv')

'''
Drop row if any of the column contains empty or nan value. 
This will delete any rows which do not have a name.
'''
df.dropna(inplace=True)

#Since, I drop the rows. I will reset the rolling numbering index value. 
df.reset_index(drop=True,inplace=True)

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

        #Change the float type of the price to string 
        price = str(x['price'])
        #Remove any zero preappend to the price field 
        price = price.strip('0')

        #Change the string type of price back to float. 
        price = float(price)
        
        #Set the status of the price to True if > 100.
        if price > 100:
            above_100 = True
        elif price < 100:
            above_100 = False

        x['first_name'] = first_name
        x['last_name'] = last_name
        x['processed_price'] = price
        x['above_100'] = above_100

    except Exception as e:
        print('error occured in processing_fn')
        print(e)

    else:
        return(x)

df = df.apply(processing_fn,axis=1)
df.drop(columns=['name','price'],inplace=True)
df.to_csv('C:/Users/HP/Desktop/gov_tech/final_result.csv',index=False)