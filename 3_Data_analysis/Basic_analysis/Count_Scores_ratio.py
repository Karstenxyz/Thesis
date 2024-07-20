import pandas as pd

def calculate_winning_ratio(row):
    total = row.sum()
    if total == 0:
        return float('nan')
    winning_ratio = row.max() / total
    return winning_ratio

# Load the Excel file
input_file = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx'  # Replace with your input file path
output_file = '/Users/karsten/Downloads/Thesis/Results/winning_ratios.xlsx'  # Replace with your desired output file path

# Specify the column name or index
column_name = 'scores'  # Replace with the column name containing the scores
# Or you can use the column index if you prefer
# column_index = 0  # Replace with the column index containing the scores

# Read the data from the Excel file
df = pd.read_excel(input_file)

# Select the specific column containing the scores
# If using column name:
scores_df = df[column_name].apply(lambda x: pd.Series(eval(x)))
# If using column index:
# scores_df = df.iloc[:, column_index].apply(lambda x: pd.Series(eval(x)))

# Calculate the winning ratios
winning_ratios = scores_df.apply(calculate_winning_ratio, axis=1)

# Save the winning ratios to a new Excel file
winning_ratios_df = pd.DataFrame(winning_ratios, columns=['winning_ratio'])
winning_ratios_df.to_excel(output_file, index=False)

print(f"Winning ratios have been calculated and saved to {output_file}")
