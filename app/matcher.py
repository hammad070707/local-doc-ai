from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

class ProductMatcher:
    def __init__(self,collection_name="Products"):
        self.client = QdrantClient(path="db/")
        self.model=SentenceTransformer("all-MiniLM-L6-v2")
        self.collection_name=collection_name 

        if not self.client.collection_exists(collection_name=self.collection_name):
            print(f"Almari '{self.collection_name}' nahi mili, nayi bana rahe hain...")
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE)
            )
        else:
            print(f"Almari '{self.collection_name}' pehle se maujood hai. Purana data use karenge.")

    def index_products(self,product_list):
        points=[]
        for idx,prod in enumerate(product_list):
            vector=self.model.encode(prod).tolist()
            points.append(PointStruct(id=idx,vector=vector,payload={"name":prod}))
        self.client.upsert(collection_name=self.collection_name,points=points)
    
    def search(self,item_name,threshold=0.7):
        query_vector=self.model.encode(item_name).tolist()
        response=self.client.query_points(collection_name=self.collection_name,query=query_vector,limit=1)
        results = response.points
        
        if results and results[0].score>=threshold:
            return results[0].payload["name"] ,results[0].score
        return "no match found",0.0