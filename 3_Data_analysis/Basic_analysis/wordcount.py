import pandas as pd

def count_words(text):
    if pd.isna(text):
        return 0
    # Split the text into words
    words = text.split()
    # Return the number of words
    return len(words)

# Read the Excel file
file_path = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx'  # Update this path to your file
df = pd.read_excel(file_path)

# Assuming the text data is in a column named 'body'
df['word_count'] = df['body'].apply(count_words)

# Save the result to a new Excel file
output_file_path = '/Users/karsten/Downloads/Thesis/Results/wordcount_dataset.xlsx'  # Update this path to your desired output file
df.to_excel(output_file_path, index=False)

print("Word count has been added to the new Excel file.")
