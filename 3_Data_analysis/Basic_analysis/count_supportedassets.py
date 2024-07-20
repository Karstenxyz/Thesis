import pandas as pd

# Load the Excel file
file_path = '/Users/karsten/Downloads/Thesis/Results/Playground.xlsx'  # Replace with the correct path
df = pd.read_excel(file_path)

# Assuming the column with the supported assets is named 'supported_assets'
# Replace 'supported_assets' with the actual column name
assets_column = 'symbols'

# Function to count the number of unique assets in each row
def count_unique_assets(assets):
    # Split by comma, strip any extra whitespace, and convert to a set to remove duplicates
    unique_assets = set([asset.strip() for asset in str(assets).split(',') if asset.strip()])
    return len(unique_assets)

# Create a new column to store the count of unique assets
df['UniqueAssetCount'] = df[assets_column].apply(count_unique_assets)

# Display the results
print(df)

# Save the results to a new Excel file
output_file_path = '/Users/karsten/Downloads/Thesis/Results/supported_assets_unique_count.xlsx'
df.to_excel(output_file_path, index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Supported Assets Unique Count", dataframe=df)
