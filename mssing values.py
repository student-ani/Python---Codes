# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p-KY-HR2GoKYQTlxtnmifE7f6ix1aamN
"""



import pandas as pd

df = pd.read_csv('/content/24926.csv')

missing_values = df.isnull().sum()
print(missing_values)

cleaned_df = df.dropna()

cleaned_df = df.dropna(axis=1)

mean_age = df['CA_1'].mean()
df['CA_1'].fillna(mean_age, inplace=True)

def count_students_less_than_75(attendance_list):
    count = 0
    for attendance in attendance_list:
        if attendance < 75:
            count += 1
    return count

attendance_list = [80, 60, 90, 70, 65, 85, 55]
less_than_75_count = count_students_less_than_75(attendance_list)
print("Number of students:", less_than_75_count)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/24926.csv')

scholar_hostlers = df[(df['ScholarType'] == 'Day Scholar') & (df['Hostler'] == True)]

low_attendance = scholar_hostlers[scholar_hostlers['Course_Att'] < 75]


plt.scatter(low_attendance['Course_Att'], low_attendance['some_other_variable'], color='red', label='Course_Att < 75%')
plt.xlabel('Course_Att (%)')
plt.ylabel('Some other variable')
plt.title('Relation between Student Scholar Type Hostlers with Attendance < 75%')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
df = pd.read_csv('/content/24926.csv')




schools = list(school_data.keys())
student_counts = list(school_data.values())


plt.figure(figsize=(10, 6))
plt.bar(schools, student_counts, color='skyblue')


plt.xlabel('Schools')
plt.ylabel('Number of Students')
plt.title('Total Number of Students in Different Schools')


plt.xticks(rotation=45, ha='right')


plt.tight_layout()
plt.show()

import pandas as pd

df = pd.read_csv('/content/24926.csv')
#df.shape()
print(df.shape)