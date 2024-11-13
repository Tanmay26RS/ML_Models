import pandas as pd
data=pd.read_csv('C:\\Users\\my pc\\OneDrive\\Desktop\\ml_model\\archive\\bmi_train.csv')
print(data)

from sklearn.model_selection import train_test_split

X = data.drop('target_column', axis=1)
y = data['target_column']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)