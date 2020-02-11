import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
import pickle
from machinelearning.data_cleaning import convert_word_to_int

PATH = Path(Path.cwd())
DATA = Path(PATH, 'machinelearning', 'data', 'raw', 'tree_months_sales.csv')

df = pd.read_csv(DATA)
df['rate'].fillna(0, inplace=True)
df['sales_in_first_month'].fillna(df['sales_in_first_month'].mean(), inplace=True)

# Training
X = df.iloc[:, :3]
X['rate'] = X['rate'].apply(lambda x: convert_word_to_int(x))
y = df.iloc[:, -1]
regressor = LinearRegression()
regressor.fit(X, y)
pickle.dump(regressor, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))