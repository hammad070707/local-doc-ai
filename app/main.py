from fastapi import FastAPI , UploadFile, File, BackgroundTasks, background
import shutil
import os
from ocr_engine import DocumentProcessor
from extractor import InvoiceExtractor
from matcher import ProductMatcher

app=FastAPI()
doc_processor=DocumentProcessor()
extractor=InvoiceExtractor()
matcher=ProductMatcher()

catalog = ["Laptop Dell XPS", "Wireless Mouse", "Mechanical Keyboard", "Monitor 24 inch"]
matcher.index_products(catalog)
def cleanup_file(file_path: str):
    """
    Processing khatam hone ke baad file delete karne ke liye
    """
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"✅ Temporary file {file_path} delete ho gayi.")
        except Exception as e:
            print(f"⚠️ Cleanup failed: {e}")

@app.post("/process_invoice")
async def process_invoice(background_tasks:BackgroundTasks,file:UploadFile=File(...)):
    HOME=os.path.expanduser("~")
    UPLOAD_PATH=os.path.join(HOME,"n8n-file","data","uploads")
    os.makedirs(UPLOAD_PATH,exist_ok=True)
    temp_file=os.path.join(UPLOAD_PATH,f"{file.filename}")  

    with open(temp_file,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    raw_text=doc_processor.process_document(temp_file)
    structured_data=extractor.extract(raw_text)

    for item in structured_data.get("items",[]):
        matched_name,score=matcher.search(item['description'])
        item["matched_catalog_item"]=matched_name
        item["match_score"]=score

    need_review=any(item["match_score"]<0.6 for item in structured_data.get("items",[]) )
    structured_data["need_review"]=need_review
    background_tasks.add_task(cleanup_file,temp_file)
    return structured_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
    