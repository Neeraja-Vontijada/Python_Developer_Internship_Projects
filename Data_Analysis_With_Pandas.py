import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data2.csv')
#display the first few rows of the data
print(df.head())
#display the data, get descritption statistics for all numbers
print(df.describe())
#find missing values in each column
mv=df.isnull().sum()
print("Missing vales in each column:\n",mv)
#avg of column
avg=df['Age'].mean()
print("avg of age",avg)
#count the number of usnique values
uv=df['Age'].nunique()
print(f"unique values",uv)
#Filter Rows based on a condition, eg - filter
eng_emp=df[df['Department'] == 'Engineering']
print(eng_emp)
#maximum of the salary
max_salary=df['Salary'].max()
max_salary_emp=df[df['Salary'] == max_salary]
print("highest paid employee",max_salary_emp)
#no of emplyees in each department
dep_count=df['Department'].value_counts()
print("Number of employees in each department:",dep_count)
#sort by column data
sort=df.sort_values(by='Age',ascending=False)
print("Senior to junir employee",sort)
#add a new column based on condn ,eg - add Experience based on age
df['Experience']=df['Age'].apply(lambda x:'Senior' if x>=30 else 'Junior')
print("Data with Experience column:",df)
#data visualization
plt.figure(figsize=(8, 6))
plt.pie(dep_count, labels=dep_count.index,autopct='%1.1f%%', startangle=140)
plt.title("Department")
plt.show()