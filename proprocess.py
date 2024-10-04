import pandas as pd

# Read the CSV file
df = pd.read_csv('population_state.csv')

# Filter for overall ethnicity and age
df_filtered = df[(df['ethnicity'] == 'overall') & (df['age'] == 'overall')]

# Extract year from date
df_filtered['year'] = pd.to_datetime(df_filtered['date']).dt.year

# Multiply population by 1000
df_filtered['population'] = (df_filtered['population'] * 1000).astype(int)

# Select and rename columns
result = df_filtered[['year', 'state', 'population']]
result = result.rename(columns={'year': 'Year', 'state': 'State', 'population': 'Population'})

# Group by Year and State, summing the population
result = result.groupby(['Year', 'State'])['Population'].sum().reset_index()

# Sort by Year and State
result = result.sort_values(['Year', 'State'])

# Write to a new CSV file
result.to_csv('state_population.csv', index=False)

print("Preprocessing complete. Output saved to 'state_population.csv'")