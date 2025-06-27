import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from database import load_table, write_table

# Load your table
df = load_table("my_table")

# Select the target column (the one with missing values)
target_column = "age"

# Separate rows with and without missing target values
train_data = df[df[target_column].notnull()]
missing_data = df[df[target_column].isnull()]

# Choose which features to use for prediction
features = ["income", "education_years"]

# Train a model
model = RandomForestRegressor()
model.fit(train_data[features], train_data[target_column])

# Predict and fill in missing values
predicted = model.predict(missing_data[features])
df.loc[df[target_column].isnull(), target_column] = predicted

# Write back to DB
write_table(df, "my_table")
print("Missing data filled and table updated.")
