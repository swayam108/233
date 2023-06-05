import pandas as pd
df=pd.read_csv("projectC233_studentData.csv")

df['Total_marks_obtained']=df.iloc[:, [3,4,5]].sum(1)

df.loc[df['Total_marks_obtained'] > 250, 'Grade'] = 'A'
df.loc[df['Total_marks_obtained'] < 250, 'Grade'] = 'B'

df['Percentage']=df['Total_marks_obtained'] / df['Overall_Total'] *100

print(df)