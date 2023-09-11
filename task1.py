#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Employee_HR.csv')

#Q1-variance, standard deviation, and interquartile range (IQR) of the salaries of employees in the HR and Marketing departments.
hr_marketing_salaries = df[df['Department'].isin(['hr', 'marketing'])]['Salary_INR'].to_numpy()
variance = np.var(hr_marketing_salaries)
std_deviation = np.std(hr_marketing_salaries)
q1 = np.percentile(hr_marketing_salaries, 25)
q3 = np.percentile(hr_marketing_salaries, 75)
iqr = q3 - q1
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"IQR: {iqr}")

#Q2-range of experience in the IT department
it_experience = df[df['Department'] == 'IT']['time_spent_company']
experience_range = it_experience.max() - it_experience.min()
print(f"Range of experience in IT department: {experience_range}")

#Q3-boxplot
plt.figure(figsize=(10, 6))
ax = sns.boxplot(x='Department', y='time_spent_company', data=df)
plt.title('Experience by Department')
plt.xlabel('Department')
plt.ylabel('Experience (years)')
plt.show()

#Q4-feature with the highest standard deviation in the dataset.
std_deviations = df.std(numeric_only=True)
highest_std_feature = std_deviations.idxmax()
print(f"The feature with the highest standard deviation is: {highest_std_feature}")
