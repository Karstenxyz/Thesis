import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load the cleaned data
cleaned_data = pd.read_excel('/Users/karsten/Downloads/Thesis/Cleaned data/Dataset_wihtout_stopwords.xlsx')

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_data['cleaned_titles'])

# Dimensionality Reduction (optional)
pca = PCA(n_components=2, random_state=42)
X_reduced = pca.fit_transform(X.toarray())

# Clustering
num_clusters = 6 
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
labels = kmeans.fit_predict(X_reduced)

# Add cluster labels to the DataFrame
cleaned_data['cluster'] = labels

# Save the updated data with cluster labels to a new Excel file
clustered_file_path = '/Users/karsten/Downloads/Thesis/Cleaned data/Dataset_clustered.xlsx'
cleaned_data.to_excel(clustered_file_path, index=False)
