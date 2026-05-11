from docling.document_converter import DocumentConverter

class DocumentProcessor:
    def __init__(self):
        self.converter=DocumentConverter()

    def process_document(self,source_path:str):
        """
        PDF/Image ko text (Markdown) mein convert karta hai
        """
        try:
            result=self.converter.convert(source_path)
            markdown_output=result.document.export_to_markdown()
            return markdown_output
        except Exception as e:
            print(e)
            return "Error"

if __name__ == "__main__":
    processor = DocumentProcessor()

