# WebAI Project

## a) Problem Statement Reference
**Problem Statement Chosen:** AI-powered web agent for browsing, searching, and interacting with web data.  

**Reason to Choose the Problem Statement:**  
To build an intelligent assistant that can fetch, process, and present information from the web in real-time, making research and data gathering more efficient.  

---

## b) Solution Overview
**Proposed Approach (2–3 lines):**  
We use a combination of backend APIs, a Streamlit frontend, and LLM-based reasoning to search the web, extract meaningful information, and present it in a user-friendly interface.  

**Key Features / Modules:**  
- `agent.py` → AI reasoning engine  
- `backend.py` → API for orchestrating modules  
- `console_frontend.py` → CLI interface  
- `llm_module.py` → LLM integration  
- `streamlit_frontend.py` → Web interface  

---

## c) System Architecture
**Architecture Diagram / Workflow:**  
![Architecture](SystemArchitecure.png)  

**Data Flow Explanation:**  
1. User enters a query via Streamlit frontend.  
2. Backend processes request and routes it to the agent.  
3. Agent uses LLM + scraping modules to fetch web content.  
4. Data is processed and returned to the frontend.  

---

## d) Technology Stack
- **Backend:** Python (FastAPI/Flask)  
- **Frontend:** Streamlit, Console UI  
- **Databases:** (If applicable, e.g., SQLite/Postgres)  
- **ML/AI Frameworks:** LangChain, OpenAI/Ollama integration  
- **APIs / Libraries:** BeautifulSoup, Requests, Pandas  

---

## e) Algorithms & Models
- **Algorithm(s) Chosen:** Information extraction + summarization  
- **Reason for Choice:** Enables efficient real-time processing of unstructured data.  
- **Model Training & Testing Approach:** Pre-trained LLMs + prompt engineering; no heavy training required.  

---

## f) Data Handling
- **Data Sources Used:** Web scraping, APIs  
- **Preprocessing Methods:** Cleaning HTML, extracting text, formatting JSON  
- **Storage / Pipeline Setup:** Temporary in-memory storage with Pandas DataFrames  

---

## g) Implementation Plan
1. **Initial Setup & Environment** → Install dependencies & set up repo  
2. **Core Module Development** → Build agent, backend, LLM integration  
3. **Integration & Testing** → Connect frontend with backend and agent  
4. **Final Deployment-ready Build** → Deploy Streamlit app  

---

## h) Performance & Validation
- **Evaluation Metrics:** Response accuracy, latency, user satisfaction  
- **Testing Strategy:** Unit testing (Python `unittest/pytest`), manual query validation  

---

## i) Deployment & Scalability
- **Deployment Plan:** Deploy via Streamlit Cloud / Docker  
- **Scalability Considerations:**  
  - Modular backend for microservices  
  - Can extend to multiple LLM APIs  
  - Horizontal scaling with containerization  

---
