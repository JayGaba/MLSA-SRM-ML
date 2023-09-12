import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#dataset - https://www.kaggle.com/datasets/mmek31/titantic
data = pd.read_csv('/content/train.csv')

#grouping passengers by Pclass
pclass_counts = data['Pclass'].value_counts().reset_index().rename(columns={'index': 'Pclass', 'Pclass': 'Count'})

#grouping passengers by Sex
sex_counts = data['Sex'].value_counts().reset_index().rename(columns={'index': 'Sex', 'Sex': 'Count'})

#grouping passengers by embarked
embarked_counts = data['Embarked'].value_counts().reset_index().rename(columns={'index': 'Embarked', 'Embarked': 'Count'})

#grouping passengers by age range
age_bins = [0, 18, 30, 50, 100]
age_labels = ['0-18', '19-30', '31-50', '51+']
data['AgeRange'] = pd.cut(data['Age'], bins=age_bins, labels=age_labels)
age_counts = data['AgeRange'].value_counts().reset_index().rename(columns={'index': 'AgeRange', 'AgeRange': 'Count'})

#bar plots to visualize passenger counts in each group
plt.figure(figsize=(12, 4))
plt.subplot(131)
sns.barplot(x='Pclass', y='Count', data=pclass_counts)
plt.title('Passenger Count by Pclass')
plt.subplot(132)
sns.barplot(x='Sex', y='Count', data=sex_counts)
plt.title('Passenger Count by Sex')
plt.subplot(133)
sns.barplot(x='Embarked', y='Count', data=embarked_counts)
plt.title('Passenger Count by Embarked')
plt.tight_layout()
plt.show()
plt.figure(figsize=(5, 3))
sns.barplot(x='AgeRange', y='Count', data=age_counts, order=age_labels)
plt.title('Passenger Count by Age Range')
plt.xlabel('Age Range')
plt.ylabel('Count')
plt.show()
