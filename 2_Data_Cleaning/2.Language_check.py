import pandas as pd
from langdetect import detect, LangDetectException

# Load the dataset (adjust the file path as needed)
file_path = '/Users/karsten/Downloads/Copy_Final_Version2.xlsx'
df = pd.read_excel(file_path)

# Function to detect if the language of the title is English
def is_english(title):
    try:
        return detect(title) == 'en'
    except LangDetectException:
        return False

# Apply the function to the dataset to identify non-English titles
df['is_non_english'] = df['title'].apply(lambda x: not is_english(x))

# Save the dataset with color highlighting to an Excel file
highlighted_file_path = '/Users/karsten/Downloads/Copy_Final_Version3.xlsx'
with pd.ExcelWriter(highlighted_file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Proposals')
    workbook = writer.book
    worksheet = writer.sheets['Proposals']
    
    # Apply conditional formatting to highlight non-English titles
    format_red = workbook.add_format({'bg_color': 'red', 'font_color': 'white'})
    for row_num, is_non_english in enumerate(df['is_non_english'], start=2):  # start=2 to account for header row
        if is_non_english:
            worksheet.write(row_num, df.columns.get_loc('title'), df.at[row_num-2, 'title'], format_red)

print(f"Initial dataset size: {len(df)}")
print(f"Number of non-English proposals: {df['is_non_english'].sum()}")
print(f"Highlighted dataset saved to: {highlighted_file_path}")
