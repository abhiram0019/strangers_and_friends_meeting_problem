import pandas as pd
import numpy as np

def subg(df):
    if(len(df)==0):
        return
    i = 0
    cont = df['name1'].mode()
    lt = []
    lt.append(cont[0])
    drop = []
    while i < len(lt):
        comp = lt[i]
        #print(comp)
        for j in range(len(df)):
            if(str(df['name1'][j]) == str(comp)):
                lt.append(df['name2'][j])
                #print(df['name2'][j])
                drop.append(j)
            if(str(df['name2'][j]) == str(comp)):
                lt.append(df['name1'][j])
                #print(df['name1'][j])
                drop.append(j)

        for j in range(len(drop)):
            df = df.drop(drop[j])
        drop = []
        df = df.reset_index()
        df = df.drop(['index'],axis=1)
        
        #print(i)
        #print(lt)
        i+=1
        
    lt = list(set(lt))
    print(lt)
    subg(df)
    return


df = pd.read_csv("sample_2.csv")
#print(df.head())

subg(df)

print("---------------------------------------------------------------------------------------------------------------")
users = set(df['name1'].unique().tolist()+df['name2'].unique().tolist())
print("No of users: ",len(users))
print(users)
