import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class JobSearchEngine:
    def __init__(self, jobs):
        self.jobs = jobs
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.embeddings = None
        self._prepare_data()
    
    def _combine_fields(self, job):
       
        return f"{job['title']} {job['description']} {job['degree_requirements']}"

    def _prepare_data(self):
        combined_data = [self._combine_fields(job) for job in self.jobs]
        self.embeddings = self.model.encode(combined_data, convert_to_tensor=False)
        dimension = self.embeddings[0].shape[0]
        self.index = faiss.IndexFlatL2(dimension)
        faiss_embeddings = np.array(self.embeddings)
        self.index.add(faiss_embeddings)
        
    def search(self, query):
        query_embedding = self.model.encode(query, convert_to_tensor=False).reshape(1, -1)
        distances, indices = self.index.search(query_embedding, 10)
        
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if dist <= 1.5 and idx < len(self.jobs):
                job = self.jobs[idx]
                results.append({
                    "id": job["id"],
                    "title": job["title"],
                    "company": job["company"],
                    "location": job["location"],
                    "description": job["description"],
                    "degree_requirements": job["degree_requirements"]
                })
        return results
