
import numpy as np
from sklearn.cluster import KMeans

def cluster_student(daily_hours, weak_count):

    data = [
        [2, 4],  
        [5, 2],   
        [8, 1]    
    ]

    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(data)

    label = kmeans.predict([[daily_hours, weak_count]])[0]

    return ["Beginner", "Intermediate", "Advanced"][label]
