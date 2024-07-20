import pandas as pd
import re

def count_external_links(text):
    if pd.isna(text):
        return 0
    # Find all URLs using a regex pattern
    urls = re.findall(r'(https?://\S+)', text)
    # Return the number of URLs found
    return len(urls)

# Read the Excel file
file_path = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx'  # Update this path to your file
df = pd.read_excel(file_path)

# Assuming the text data is in a specific column named 'body'
specific_column = 'body'  # Change this to the name of your column

# Apply the external link count function to the specific column
df['link_count'] = df[specific_column].apply(count_external_links)

# Save the result to a new Excel file
output_file_path = '/Users/karsten/Downloads/Thesis/Results/urlcount_dataset.xlsx'  # Update this path to your desired output file
df.to_excel(output_file_path, index=False)

print("Word count and link count have been added to the new Excel file.")
