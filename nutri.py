import pandas as pd

# Define file paths
file1 = "food.csv"
file2 = "food_nutrient.csv"
file3 = "nutrient.csv"

# Read CSV files into DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

join_col_left = df1.columns[0]  # First column of the first table
join_col_right = df2.columns[1]  # Second column of the second table

# Perform the inner join
joined_df = pd.merge(df1, df2, left_on=join_col_left, right_on=join_col_right, how="inner")

join_col_left = joined_df.columns[6]  # third column of the first table
join_col_right = df3.columns[0]  # Second column of the second table

# Perform the inner join
joined_df = pd.merge(joined_df, df3, left_on=join_col_left, right_on=join_col_right, how="inner")

# Print the joined DataFrame
print(joined_df)

# Optionally, save the joined DataFrame to a new CSV file
joined_df.to_csv("joined_data.csv", index=False)

