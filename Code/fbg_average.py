import pandas as pd
import numpy as np

file_path = os.path.join('..', 'data','treated_data','event0.xlsx')


dfE={}
j=0
while j <= 4:
    j=j+1
    event='L'+str(j)
    dfE[event] = pd.read_excel(file_path,sheet_name=event)
   
   
mean_values = {}

for key, value in dfE.items():
    mean_values[key] = value.mean()
df_mean_values = pd.DataFrame(mean_values)






subtracted_values = {}
for i in range(2, 6):
    current_key = 'L' + str(i)
    previous_key = 'L1'
    subtracted_values[current_key] = mean_values[current_key] - mean_values[previous_key]

df_deltalambda =pd.DataFrame(subtracted_values)

file_path2 = os.path.join('..', 'data','treated_data','C2_Event_DL.xlsx')
writer = pd.ExcelWriter(file_path2, engine='xlsxwriter')


df_mean_values.to_excel(writer, sheet_name='L1', index=True)
df_deltalambda.to_excel(writer, sheet_name='L2', index=True)


writer.save()
writer.close()

# i = 0
# mean={}

# while i <= 5:
#     i=i+1
#     L = 'Lambda'+str(i)
#     mean[L]=[]
#     meanvalue =df[L].mean()
# #     pm= meanvalue * 1000 
#     mean[L].append(pm)
    
# df_mean=pd.DataFrame(mean)


    
    
    
    

