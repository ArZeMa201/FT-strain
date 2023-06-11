import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#data paths for saving  openning writting
relative_path = os.path.join('..', 'data','raw', '01_Peak_2023_06_02_Condition1.txt')
file_path = os.path.join('..', 'data','treated_data','event1.xlsx')

#dataframe creation
df = pd.read_csv(relative_path, index_col=0, delimiter="\t", parse_dates=(True))

#dataframe formating time

data_time = '2023-06-02 11:05:59.138370'

df['Time'] = df.index
Fix = df.loc[pd.Timestamp(data_time), 'Time']
df.index = df.index.time
df['Time'] = df['Time'] - Fix
df['seconds'] = df['Time'].dt.total_seconds()

i = 0
ts = 95

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
        if x <= ts:
            event[L].append(l)
            event['Time'].append(x)
            


df_events=pd.DataFrame(event)

writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

df_events.to_excel(writer, sheet_name='L1', index=False)
writer.save()



            
            
    
