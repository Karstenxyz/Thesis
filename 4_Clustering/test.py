import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA

# Load the cleaned data
cleaned_data = pd.read_excel('/Users/karsten/Downloads/Thesis/Cleaned data/Dataset_wihtout_stopwords.xlsx')

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_data['cleaned_titles'])

# Dimensionality Reduction (optional)
pca = PCA(n_components=2, random_state=42)
X_reduced = pca.fit_transform(X.toarray())

# Adding the PCA components to the data
cleaned_data['PCA_Component_1'] = X_reduced[:, 0]
cleaned_data['PCA_Component_2'] = X_reduced[:, 1]

# Save the updated data with PCA components to a new Excel file
pca_file_path = '/Users/karsten/Downloads/Thesis/Results/DATA/Copy_Final_Version5.xlsx'
cleaned_data.to_excel(pca_file_path, index=False)
