import pandas as pd

# Read the CSV files
population_df = pd.read_csv('AS2/data/state_population.csv')
drug_addicts_df = pd.read_csv('AS2/data/drug-addicts-by-state.csv')

# Ensure 'Year' is treated as an integer in both dataframes
population_df['Year'] = population_df['Year'].astype(int)
drug_addicts_df['Year'] = drug_addicts_df['Year'].astype(int)

# Merge the dataframes on 'State' and 'Year'
merged_df = pd.merge(drug_addicts_df, population_df, on=['State', 'Year'], how='inner')

# Rename the 'Value' column to 'Number of Drug Addicts'
merged_df = merged_df.rename(columns={'Value': 'Number of Drug Addicts'})

# Select and reorder the columns
result_df = merged_df[['Year', 'State', 'Number of Drug Addicts', 'Population']]

# Sort the dataframe by Year and State
result_df = result_df.sort_values(['Year', 'State'])

# Ensure 'Number of Drug Addicts' is an integer
result_df['Number of Drug Addicts'] = result_df['Number of Drug Addicts'].astype(int)

# Write the result to a new CSV file
result_df.to_csv('AS2/data/combined_drug_addicts_population.csv', index=False)

print("Data processing complete. Output saved to 'AS2/data/combined_drug_addicts_population.csv'")