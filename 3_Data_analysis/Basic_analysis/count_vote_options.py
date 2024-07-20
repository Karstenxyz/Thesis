import pandas as pd
import re

# Load the Excel file
file_path = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx'  # Replace with the correct path
df = pd.read_excel(file_path)

# Assuming the column with the proposals is named 'ProposalAnswers'
# Replace 'ProposalAnswers' with the actual column name
proposal_column = 'choices'

# Function to count the number of options in each row
def count_options(proposal):
    # Use regex to find all options within the brackets
    options = re.findall(r"'(.*?)'", proposal)
    return len(options)

# Create a new column to store the count of options
df['OptionCount'] = df[proposal_column].apply(count_options)

# Display the results
print(df)

# Save the results to a new Excel file
output_file_path = '/Users/karsten/Downloads/Thesis/Results/choises_dataset.xlsx'
df.to_excel(output_file_path, index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Corrected Proposal Options Count", dataframe=df)
