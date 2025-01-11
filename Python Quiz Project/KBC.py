import pandas as pd
import numpy as np
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1500)
i=[1002,1345,3421,7685,6547,6474,3920,1110]
name=['Rishika','Rohan','Aayat','Amandeep','Sarah','Preeti','Lucas','Faizan']
gender=['F','M','F',np.NaN,'F','F','M','M']
age=[23,27,39,37,26,34,32,19]
correct=[7,14,6,31,28,18,26,39]
wrong=[3,6,4,19,7,2,9,11]
mode=['Easy','Medium','Easy','Brutal','Hard','Medium','Hard','Brutal']
score=[125,250,100,525,525,350,475,725]
area=['Chennai','Mumbai','Noida','Ghaziabad','Meerut','Noida','Lucknow','Ghaziabad']
n={'ID':i,'Player_Name':name,'Gender':gender,'Age':age,'Area':area,'Correct_answer':correct,'Wrong_answer':wrong,'Score':score,'Mode':mode}
df=pd.DataFrame(n)
print(df)
df.to_csv('Players.csv',na_rep='NULL',index=False)