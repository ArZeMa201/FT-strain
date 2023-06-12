import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#data paths for saving  openning writting
relative_path = os.path.join('..', 'data','raw','03_Peaks_2023_06_02_condition2.txt')

#just change the file name 
file_path = os.path.join('..', 'data','treated_data','C2_Event_3.xlsx')

#dataframe creation
df = pd.read_csv(relative_path, index_col=0, delimiter="\t", parse_dates=(True))

#dataframe formating time

data_time = '2023-06-02 12:25:06.30507'

df['Time'] = df.index
Fix = df.loc[pd.Timestamp(data_time), 'Time']
df.index = df.index.time
df['Time'] = df['Time'] - Fix
df['seconds'] = df['Time'].dt.total_seconds()

i = 0
#Seconds where the events happen
lowerbound= 800
upperbound= 970

event={}
e = []

L = 'Lambda'+str(i)


while i <= 5:
    i=i+1
    L = 'Lambda'+str(i)
    event['Time']=[]
    event[L] = []
    
    print(event)
    for x, l in zip(df['seconds'], df[L]):
        if lowerbound<= x <= upperbound:
            event[L].append(l)
            event['Time'].append(x)
            


df_events=pd.DataFrame(event)

writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

df_events.to_excel(writer, sheet_name='L1', index=False)
writer.save()



            
            
    
