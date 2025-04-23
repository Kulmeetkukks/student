#create dataframe and import in csv
import pandas as pd
import streamlit as st
student={'name':['A',None,'C','D'],'hindi':[67,None,88,66],'maths':[None,90,92,43]}
df=pd.DataFrame(student)
print(df)
#exporting dataframe to csv
df.to_csv('student.csv')
f=open('student.csv')
print(f.read())
print(df.isnull())
#print(df.dropna())
ndf=df.fillna({'name':'Lvis','hindi':0,'maths':10})
print(ndf)
st.write(ndf)
