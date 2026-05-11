import json
from extractor import InvoiceExtractor
from ocr_engine import DocumentProcessor

def run_test(pdf_path):
    doc_processor=DocumentProcessor()
    markdown_test=doc_processor.process_document(pdf_path)
    extractor=InvoiceExtractor()
    structured_data=extractor.extract(markdown_test)
    print(json.dumps(structured_data,indent=4))
    
if __name__ == "__main__":
    run_test("data/uploads/sample_invoice.jpg")



