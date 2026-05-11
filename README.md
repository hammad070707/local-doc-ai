📑 LocalDoc-AI: End-to-End Automated Invoice Processing

📌 Project Overview
LocalDoc-AI is a production-grade, privacy-first automated pipeline designed to extract, structure, and route data from sensitive financial documents. By combining Local LLMs (Ollama) with Workflow Automation (n8n), this system transforms unstructured PDFs into structured assets (CSV, Databases) without any cloud dependency.

The project demonstrates a complete Agentic Workflow: from layout-aware OCR and semantic data normalization to fully automated document routing and human-in-the-loop validation.


🏗️ System Architecture
The pipeline follows a closed-loop automation workflow:
Ingestion & Trigger (n8n): Automated folder monitoring. As soon as a file is dropped, the workflow triggers.
Layout-Aware OCR (Docling): Converts complex PDFs/Images into structured Markdown, preserving table integrity.
LLM Extraction (FastAPI + Ollama): Uses Qwen2.5 / Llama3 to extract vendor details, dates, and line items into validated JSON.
Semantic Normalization (Qdrant): Matches extracted items against a master product catalog using Vector Search (Cosine Similarity).
Automated Export (n8n): Final structured data is automatically appended to a Centralized CSV or pushed to an ERP via Webhooks.


🚀 Tech Stack
Language: Python 3.10+
Orchestration: n8n (Self-hosted Workflow Automation)
OCR Engine: Docling (IBM’s Layout-aware parser)
Local LLM Engine: Ollama (Qwen2.5 / Mistral)
Vector Database: Qdrant (Semantic Product Matching)
API Framework: FastAPI & Uvicorn


🤖 Full Automation with n8n
This project leverages n8n to bridge the gap between AI and Business Logic:
Watchdog: Monitors local directories for new supplier invoices.
Data Routing: Automatically filters high-confidence extractions to the Final CSV Report.
Human-in-the-loop: If the LLM confidence or Qdrant match score is low (<0.7), n8n flags the record for manual review before exporting.
Scalability: Handles batch processing of hundreds of documents asynchronously.


📊 Business Benefits
100% Data Privacy: Local execution ensures no sensitive financial data is leaked to 3rd party AI providers.
Zero Operating Costs: No per-page OCR fees or LLM token costs.
Error Reduction: Semantic matching eliminates manual data entry errors and naming inconsistencies.
Time Efficiency: Reduces invoice processing time from minutes to seconds per document.


🛠️ Installation & Setup
1. Setup Local AI & API

git clone https://github.com/YOUR_USERNAME/local-doc-ai.git
cd local-doc-ai
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
ollama pull qwen2.5:7b
uvicorn main:app --reload

2. Setup n8n Workflow
Open your local n8n instance.
Import the provided workflow.json from the /n8n folder.
Configure the Local File Trigger to point to your data/uploads directory.


📂 Output Format
The system generates a standardized CSV output for every processed batch:
| Vendor Name | Invoice Date | Item Description | Matched Catalog Item | Total Amount | Status |
|-------------|--------------|------------------|----------------------|--------------|--------|
| Dell Inc. | 2023-10-12 | Lptp XPS 13 | Dell XPS 13 Laptop | $1200.00 | Success|

👨‍💻 Author
Hammad Ahmed

https://www.linkedin.com/in/hammad-ahmed-ai/
https://github.com/hammad070707

This project was built to demonstrate that high-performance AI Document Processing can be achieved locally, ensuring total data privacy and cost-efficiency.
