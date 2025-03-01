import pandas as pd

# Load the Excel file
file_path_new = '/Users/karsten/Downloads/Thesis/Results/Definief!.xlsx'
df_new = pd.read_excel(file_path_new)

# Convert UNIX timestamps to datetime objects
df_new['start'] = pd.to_datetime(df_new['start'], unit='s')
df_new['end'] = pd.to_datetime(df_new['end'], unit='s')

# Calculate the duration for each row
df_new['Duration'] = df_new['end'] - df_new['start']

# Convert the duration to total seconds for easier interpretation
df_new['Duration_seconds'] = df_new['Duration'].dt.total_seconds()

# Save the updated DataFrame to a new Excel file
output_path = '/Users/karsten/Downloads/Thesis/Results/unixresults.xlsx'
df_new.to_excel(output_path, index=False)

# Display the updated DataFrame
import ace_tools as tools
tools.display_dataframe_to_user(name="Updated Proposals with Durations", dataframe=df_new)