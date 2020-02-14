import pandas as pd

# Importing dataset
train_df= pd.read_csv('train.csv')
X_train= train_df.drop("Survived",axis=1)
Y_train= train_df["Survived"]

# Training on Sex column
train_df['Sex'] = train_df['Sex'].map({'female': 1, 'male': 0}).astype(int)

# Calculating the correlation
print("Correlation: ",train_df['Survived'].corr(train_df['Sex'])*100)