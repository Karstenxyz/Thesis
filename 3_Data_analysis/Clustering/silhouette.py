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

# Dimensionality Reduction
pca = PCA(n_components=2, random_state=42)
X_reduced = pca.fit_transform(X.toarray())

# Function to calculate silhouette scores for a range of clusters
def find_optimal_clusters(data, max_k):
    iters = range(2, max_k+1, 1)
    s_scores = []
    for k in iters:
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(data)
        s_score = silhouette_score(data, labels)
        s_scores.append(s_score)
        print(f'Number of clusters: {k}, Silhouette Score: {s_score}')
    
    return iters, s_scores

# Find the optimal number of clusters
max_k = 10  
iters, s_scores = find_optimal_clusters(X_reduced, max_k)

# Plot the silhouette scores
plt.figure(figsize=(10, 6))
plt.plot(iters, s_scores, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Scores for Different Numbers of Clusters')
plt.show()

# Optimal number of clusters
optimal_k = iters[s_scores.index(max(s_scores))]
print(f'Optimal number of clusters: {optimal_k}')

