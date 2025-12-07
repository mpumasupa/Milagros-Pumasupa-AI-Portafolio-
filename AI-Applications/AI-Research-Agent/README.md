
# AI Research Agent

AI Research Agent is an intelligent research assistant that automatically analyzes PDF and Word documents, generates structured research plans, and produces concise summaries based on relevant content. It accelerates literature review, streamlines research workflows, and helps users extract insights efficiently.

This project is ideal for academics, students, and professionals who need a fast and reliable way to organize information from multiple documents.

---

## Problem Statement

Research often involves sifting through large volumes of documents to extract relevant information, which is time-consuming and prone to human error.  
AI Research Agent addresses this problem by:

- Automatically reading and indexing PDFs and Word documents.
- Retrieving the most relevant content for a given query.
- Generating a structured research plan and summary for rapid understanding.

---

## Value Proposition

AI Research Agent creates value by:

- Streamlining document analysis for research projects.
- Offering AI-generated plans and summaries to guide research decisions.
- Reducing manual effort and helping users extract insights faster.
- Allowing teams to focus on critical thinking rather than document review.

---

## Project Structure

```
AI-Research-Agent/
├── main.py
├── test_agent_run.py
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── agent/
│ ├── init.py
│ ├── _config.py
│ └── agent.py
├── rag/
│ ├── init.py
│ ├── index_documents.py
│ ├── openai_embed.py
│ └── retriever.py
│ ├── docs/ # Folder for PDF and Word files
│ └── store/ # Folder for FAISS vector storage
├── skills/
│ ├── init.py
│ ├── planner.py
│ └── summarize.py
└── vector_store/
├── init.py
└── vector_store.py

```

---

## Key Features

- **Document Indexing:** Converts PDFs and Word documents into vector embeddings and stores them in FAISS.
- **Smart Retrieval:** Finds the most relevant documents for any research query.
- **Research Planning:** Generates concise, structured research plans using retrieved content.
- **Summarization:** Produces clear summaries in bullet points or short paragraphs.
- **Test Mode:** Includes a script that simulates documents to validate the agent workflow.

---

## Technologies Used

- Python 3.10+
- FAISS for vector storage and similarity search
- PyPDF2 for PDF text extraction
- python-docx for Word document parsing
- Semantic Kernel for AI-driven text generation
- OpenAI GPT API (optional) for enhanced summaries and planning

---

## Installation

### 1. Clone the repository

git clone https://github.com/mpumasupa/AI-Research-Agent.git
cd AI-Research-Agent

### 2. Create a virtual environment

python -m venv venv

Activate it:

**Windows:**
venv\Scripts\activate

**Linux / macOS:**
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt
pip install PyPDF2 python-docx faiss-cpu

### 4. (Optional) Add OpenAI API Key

Create a `.env` file:

OPENAI_API_KEY=your_api_key_here

---

## Usage

### Running with Real Documents

1. Place PDF or Word files inside `rag/docs/`.
2. Run the agent:

python main.py

3. Enter a research question when prompted.
4. The console will display:
   - A research plan
   - A summary of relevant document content

---

### Running the Test Script

python test_agent_run.py

This script:

- Automatically creates sample PDF and Word documents
- Runs the full agent workflow
- Validates functionality without real data

---

## Example Output

Research question: What are the latest AI techniques for document summarization?

Searching for relevant information...
Retrieved 5 relevant documents.

Generating research plan...
Plan summary:

Review current AI summarization models

Compare extractive vs abstractive methods

Identify commonly used datasets

Highlight evaluation metrics

Suggest applications in document research

Producing final report...
Summary:

Bullet 1: ...

Bullet 2: ...

Bullet 3: ...

---

## Impact

AI Research Agent enables users to:

- Reduce time spent on literature review
- Extract insights efficiently
- Make informed decisions faster
- Automate repetitive document analysis tasks

This project demonstrates practical applications of AI in research and information management.

---

## License

This project is developed for educational purposes as part of ITAI 2277 and the AI Agents Hackathon 2025.
