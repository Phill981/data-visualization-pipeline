import pandas as pd
import os

#First we define the needed columns from the datatable 
filterItems = ['UNITID',    #an identifier for unviersities
               'INSTNM',    #the name of the institution, as the id appears more ofte, 
                            #we use that as the main identifier
               'SAT_AVG',   #The average SAT
               'ACTMTMID',  #The average ACT scored from the different topics.
               'ACTENMID',  #We use all of them to form an average within the file
               'ACTCMMID', 
               'NPT4_PUB'   #Earnings after the degree is obtained
               ]

count = len(os.listdir('./data')) #total amount of datasets
#if this file appears in the folder, we skip that
for i, data in enumerate(os.listdir('./data')):
    if(data == '.DS_Store'): 
        continue
    # extracting from the dataset name 
    num = int(data.split("_")[1]) -1 
    #special case for year 2000
    if(num == -1 ):
        num = 99
    #special case for the first loop where we have to initialize the dataset
    if(i == 0):
        #initializing dataset
        main_df = pd.read_csv('./data/' + data).filter(items=filterItems)
        #setting a row containing the year for each datapoint
        index = [num for _ in range(len(main_df.index))]
        #adding year as a column 
        main_df['year'] = index
        print(f"{i + 1}/{count}", len(main_df.index))
    else:
        #reading the dataset into a seperat dataset
        df = pd.read_csv('./data/' + data)
        #same process as before
        index = [num for _ in range(len(df.index))]
        df['year'] = index
        #merge dataset with main dataset
        main_df = main_df.append(df, ignore_index=True)
        print(f"{i + 1}/{count}", len(main_df.index))
#writing dataset to csv
main_df.to_csv('merged_data.csv')

