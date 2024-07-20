import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re

# Load the data
data = pd.read_excel('/Users/karsten/Downloads/Thesis/Results/Body_clustering.xlsx')

# Specify the path to the manually downloaded NLTK data
nltk.data.path.append('/Users/karsten/Downloads/stopwords/english')

# Text preprocessing function
def preprocess_text(text):
    if not isinstance(text, str):
        text = ''
    text = re.sub(r'\W', ' ', text)  # Remove non-alphanumeric characters
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.lower()  # Convert to lowercase
    tokens = text.split()  # Split into words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords.words('english')]  # Remove stopwords and lemmatize
    return ' '.join(tokens)

# Apply the preprocessing function to the 'body' column
data['cleaned_body'] = data['body'].apply(preprocess_text)

# Save the cleaned data to a new Excel file
cleaned_file_path = '/Users/karsten/Downloads/Thesis/Cleaned data/body_without_stopwords.xlsx'
data.to_excel(cleaned_file_path, index=False)
