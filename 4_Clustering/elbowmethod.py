import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the cleaned data
cleaned_data = pd.read_excel('/Users/karsten/Downloads/Thesis/Cleaned data/Dataset_wihtout_stopwords.xlsx')

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_data['cleaned_titles'])

# Dimensionality Reduction (optional)
pca = PCA(n_components=2, random_state=42)
X_reduced = pca.fit_transform(X.toarray())

# Elbow method to find the optimal number of clusters
def calculate_wcss(data):
    wcss = []
    for k in range(1, 16):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    return wcss

wcss = calculate_wcss(X_reduced)

# Plot the WCSS values
plt.figure(figsize=(10, 6))
plt.plot(range(1, 16), wcss, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.show()
