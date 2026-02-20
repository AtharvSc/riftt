# 🧬 PharmaGuard VCF Authenticator

**Advanced Pharmacogenomic Analysis & Real-Time Risk Assessment Platform**

PharmaGuard is a state-of-the-art pharmacogenomics (PGx) platform designed to bridge the gap between complex genetic data and actionable clinical insights. By analyzing patient VCF files, it predicts drug-gene interactions using a robust **Dual-Engine Approach** that combines established clinical guidelines (CPIC) with cutting-edge Machine Learning models.

---

## 🚀 Key Features

### 1. 🔬 Advanced Genetic Analysis
-   **VCF Parsing**: Validates and parses standard VCF v4.2 files, checking for essential pharmacogenomic tags (`GENE`, `RS`, `STAR`).
-   **Automated Profiling**: Instantly extracts variants and builds diplotypes for critical pharmacogenes:
    -   `CYP2D6` (Metabolizer of Codeine, Tamoxifen)
    -   `CYP2C19` (Clopidogrel, Omeprazole)
    -   `CYP2C9` (Warfarin, Phenytoin)
    -   `SLCO1B1` (Statin Transporter)
    -   `TPMT` & `DPYD` (Chemotherapy Toxicity)

### 2. 🧠 Dual-Engine Risk Assessment
-   **Rule-Based Clinical Engine**: Implements **CPIC (Clinical Pharmacogenetics Implementation Consortium)** guidelines for deterministic, evidence-based risk profiling.
-   **ML Ensemble Predictor**: A powerful Machine Learning module (using **XGBoost** and **Scikit-Learn**) that analyzes variant density, impact, and pathogenicity to predict risks even when specific guidelines are ambiguous.

### 3. 📊 Interactive Dashboard & Reports
-   **Dynamic UI**: Built with **React 19** and **Tailwind CSS** for a premium, responsive experience.
-   **Visual Risk Gauges**: "Traffic Light" system (Green/Yellow/Red) for immediate risk comprehension.
-   **Downloadable Reports**: Generate professional **PDF Metadata Reports** summarizing the analysis for clinical records.

### 4. 💬 Real-Time Consultation
-   **Live Chat**: Integrated WebSocket-based chat allows seamless communication between Patients and Doctors.
-   **Secure History**: Chat history is persisted securely in **Supabase**.

### 5. 🎙️ Voice-Activated Drug Consultant (ElevenLabs)
-   **Voice Interface**: Patients can consult an AI agent via voice.
-   **Context-Aware**: The agent accesses the patient's genetic profile to give personalized advice on specific drugs.

### 6. 🤖 AI-Powered Explanations
-   **Groq LLM Integration**: Generates human-readable, patient-friendly explanations for complex genetic interactions.
-   **Alternative Suggestions**: Automatically suggests safer medication alternatives for high-risk drugs.

---

## 🛠️ Tech Stack

### Backend
-   **Framework**: FastAPI (Python 3.10+)
-   **ML/Data**: Pandas, NumPy, Scikit-Learn, XGBoost, Joblib
-   **Real-time**: WebSockets (Starlette)
-   **PDF Generation**: ReportLab

### Frontend
-   **Framework**: React 19 (Vite)
-   **Language**: TypeScript
-   **Styling**: Tailwind CSS
-   **State/Data**: Axios, Lucide React

### Infrastructure
-   **Database**: Supabase (PostgreSQL + RLS)
-   **Deployment**: Render (Docker Containerization)
-   **LLM**: Groq Cloud API

---

## 📂 Project Structure

```bash
vcf-authenticator/
├── Dockerfile                 # Production Docker configuration
├── vcf_authenticator.py       # Main FastAPI Backend Application
├── drug_risk_engine.py        # Rule-based CPIC risk logic
├── diplotype_builder.py       # Star allele construction
├── vcf_feature_extractor/     # ML Module
│   ├── extractor.py           # Feature engineering
│   └── models/                # Pre-trained XGBoost/Ensemble models
├── frontend/                  # React Application
│   ├── src/
│   │   ├── components/        # Dashboards, Charts, Chat UI
│   │   └── ...
└── requirements.txt           # Python dependencies
```

---

## ⚡ Getting Started (Local Development)

### 1. Backend Setup
```bash
# Clone the repository
git clone https://github.com/AtharvSc/riftt.git
cd riftt

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure Environment Variables
# Create a .env file and add:
# SUPABASE_URL=...
# SUPABASE_SERVICE_KEY=...
# GROQ_API_KEY=...
```

**Run the Backend:**
```bash
uvicorn vcf_authenticator:app --reload
```
*API will run at `http://localhost:8000`*

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
*UI will run at `http://localhost:5173`*

---

## 🚀 Deployment (Render)

The project is configured for **Single-Service Docker Deployment** on Render.

1.  **Push to GitHub**.
2.  Create a **New Web Service** on [Render](https://render.com).
3.  Connect your repository.
4.  **Runtime**: Select **Docker** (Critical Step).
5.  **Environment Variables**: Add your API keys (`GROQ_API_KEY`, `SUPABASE_URL`, etc.).
6.  **Deploy**.

*The Dockerfile handles building both the React Frontend and Python Backend into a single efficient image.*

---

## 📖 API Documentation

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/analyze` | Main pipeline: VCF Upload -> Validation -> ML/Rule Analysis -> JSON Result |
| `GET` | `/api/report/download` | Generate and download PDF report of analysis |
| `WS` | `/ws/chat/{id}` | Real-time WebSocket connection for chat |
| `POST` | `/api/chat/send` | Send message (persisted to DB) |
| `GET` | `/legacy-ui` | Access old HTML-only interface |

---

*Project developed for the **DeepMind Advanced Coding Assistant Demo**.*
