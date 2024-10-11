import pandas as pd

# Load your datasets
state_population = pd.read_csv('./state_population.csv')
drug_addicts = pd.read_csv('./drug-addicts-by-state.csv')

# Filter data for years 2000 to 2021
state_population = state_population[(state_population['Year'] >= 2000) & (state_population['Year'] <= 2021)]
drug_addicts = drug_addicts[(drug_addicts['Year'] >= 2000) & (drug_addicts['Year'] <= 2021)]

# Assuming both datasets have 'State' and 'Year' columns
# Perform an outer merge to include all states from both datasets
merged_data = pd.merge(state_population, drug_addicts[['State', 'Year', 'Value']], 
                       on=['State', 'Year'], how='outer')

# Fill NaN values in the Population column with 0 and convert to integer
merged_data['Population'] = merged_data['Population'].fillna(0).astype(int)

# Fill NaN values in the Value column with 0 and convert to integer
merged_data['Value'] = merged_data['Value'].fillna(0).astype(int)

# Rename the 'Value' column to 'Number of Drug Addicts'
merged_data = merged_data.rename(columns={'Value': 'Number of Drug Addicts'})

# Sort the data if needed
merged_data = merged_data.sort_values(['Year', 'State'])

# Reset the index
merged_data = merged_data.reset_index(drop=True)

# Reorder columns
merged_data = merged_data[['Year', 'State', 'Number of Drug Addicts', 'Population']]

# Save the result
merged_data.to_csv('combined_drug_addicts_population1.csv', index=False)