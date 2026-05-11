from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from schemas import InvoiceData

class InvoiceExtractor:
    def __init__(self,model_name="qwen2.5:1.5b"):
        self.llm=ChatOllama(model=model_name,temperature=0)
        self.parser=JsonOutputParser(pydantic_object=InvoiceData)

    def extract(self,text:str):      
        prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are an expert invoice parser. Extract the following information from the provided text and return it strictly in JSON format matching the schema."
            ),
            ("user", "schema: {format_instructions}\n\nText: {text}")
        ])
        chain=prompt|self.llm|self.parser
        try: 
            format_instructions = self.parser.get_format_instructions()
            response=chain.invoke({
                "format_instructions":format_instructions,
                "text":text
            })
            return response
        except Exception as e:
            return {"error": f"Failed to extract data: {str(e)}"}

if __name__ == "__main__":
    extractor = InvoiceExtractor()
    sample_text = "Invoice #INV-101, Date: 2023-10-01, Vendor: Dell, Total: $500"
