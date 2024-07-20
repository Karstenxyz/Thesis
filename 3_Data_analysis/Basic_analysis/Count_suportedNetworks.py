import pandas as pd

# Load the Excel file
file_path = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx'  # Replace with the correct path
df = pd.read_excel(file_path)

# Assuming the column with the networks is named 'networks'
# Replace 'networks' with the actual column name
network_column = 'networks'

# Function to count the number of unique options in each row
def count_unique_options(networks):
    # Split by comma, strip any extra whitespace, and convert to a set to remove duplicates
    unique_options = set([option.strip() for option in str(networks).split(',') if option.strip()])
    return len(unique_options)

# Create a new column to store the count of unique options
df['UniqueOptionCount'] = df[network_column].apply(count_unique_options)

# Display the results
print(df)

# Save the results to a new Excel file
output_file_path = '/Users/karsten/Downloads/Thesis/Results/networks_unique_options_count2.xlsx'
df.to_excel(output_file_path, index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Networks Unique Options Count", dataframe=df)
