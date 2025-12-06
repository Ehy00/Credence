# Credence - AI News Verification Dashboard

A full-stack AI-assisted news verification dashboard built with **FastAPI**, **Next.js**, **PostgreSQL/SQLite**, **OpenAI GPT**, **GDELT**, and **Google Fact Checking API**. The system ingests articles, extracts claims, retrieves evidence, generates fact-checking verdicts, and visualizes results on a dark-themed dashboard.

## Features

- **Three Input Modes**: Accept user input as a claim, article URL, or pasted article text
- **Claim Extraction**: Uses GPT to extract check-worthy claims from articles
- **Evidence Retrieval**: Retrieves supporting/contradicting evidence from GDELT and Google Fact Check API, weighted by MBFC credibility dataset
- **Fact-Checking**: Generates verdicts (True/False/Misleading/Unverified) with confidence scoring using GPT
- **Article-Level Aggregation**: Aggregates claim-level verdicts to article-level credibility scores
- **Dark Dashboard UI**: Modern Next.js dashboard with article viewer, claims table, evidence list, and source credibility panel
- **ML Training Data**: Stores all data (documents, claims, evidence, verdicts) for future ML model retraining

## Project Structure

```
Credence/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── admin.py          # Admin endpoints for verdict overrides
│   │   │   │   ├── health.py         # Health check endpoint
│   │   │   │   ├── jobs.py           # Job retrieval endpoint
│   │   │   │   ├── sources.py        # Source listing endpoint
│   │   │   │   └── verify.py         # Main verification endpoint
│   │   │   └── deps.py               # Dependency injection (DB session)
│   │   ├── core/
│   │   │   ├── config.py             # Application settings
│   │   │   ├── logging_config.py     # Logging configuration
│   │   │   └── security.py           # API key authentication
│   │   ├── db/
│   │   │   ├── base.py               # SQLAlchemy base
│   │   │   ├── init_db.py            # Database initialization & MBFC seeding
│   │   │   └── session.py            # Database session factory
│   │   ├── integrations/
│   │   │   ├── gdelt_client.py      # GDELT API client
│   │   │   ├── google_factcheck_client.py  # Google Fact Check API client
│   │   │   ├── mbfc_client.py        # MBFC dataset client
│   │   │   └── openai_client.py      # OpenAI GPT client
│   │   ├── ml/
│   │   │   ├── classifier.py        # ML classifier for verdict prediction
│   │   │   ├── dataset_builder.py   # Build training datasets from DB
│   │   │   ├── embeddings.py        # Text embedding utilities
│   │   │   └── evaluation.py        # Model evaluation metrics
│   │   ├── models/
│   │   │   ├── claim.py              # Claim database model
│   │   │   ├── document.py           # Document database model
│   │   │   ├── evidence.py           # Evidence database model
│   │   │   ├── source.py             # Source credibility model
│   │   │   └── verdict.py            # Verdict database model
│   │   ├── schemas/
│   │   │   ├── claim.py              # Claim Pydantic schemas
│   │   │   ├── document.py           # Document Pydantic schemas
│   │   │   ├── evidence.py           # Evidence Pydantic schemas
│   │   │   ├── job.py                # Verification job schema
│   │   │   ├── source.py             # Source Pydantic schemas
│   │   │   └── verdict.py            # Verdict Pydantic schemas
│   │   ├── services/
│   │   │   ├── admin_service.py      # Admin service functions
│   │   │   ├── aggregation.py        # Article-level verdict aggregation
│   │   │   ├── claim_extraction.py   # Claim extraction service
│   │   │   ├── evidence_retrieval.py # Evidence retrieval & ranking
│   │   │   ├── fact_checking.py      # Fact-checking service
│   │   │   └── ingestion.py          # URL fetching & text normalization
│   │   ├── tests/                    # Test files
│   │   └── main.py                   # FastAPI application entry point
│   ├── Dockerfile
│   └── pyproject.toml                # Python dependencies
├── frontend/
│   ├── app/
│   │   ├── admin/                    # Admin page
│   │   ├── result/[jobId]/           # Result display page
│   │   ├── verify/                   # Verification workspace
│   │   ├── layout.tsx                # Root layout
│   │   ├── page.tsx                  # Home page
│   │   ├── globals.css               # Global styles
│   │   └── theme.css                 # Dark theme styles
│   ├── components/
│   │   ├── charts/
│   │   │   ├── TimelineChart.tsx     # Timeline visualization
│   │   │   └── VerdictPieChart.tsx   # Verdict distribution chart
│   │   ├── inputs/
│   │   │   ├── ArticleTextForm.tsx   # Paste article text form
│   │   │   ├── ClaimInputForm.tsx    # Claim input form
│   │   │   └── UrlInputForm.tsx      # URL input form
│   │   ├── layout/
│   │   │   └── Shell.tsx             # Main layout shell with nav
│   │   └── results/
│   │       ├── ArticleViewer.tsx     # Article display component
│   │       ├── ClaimTable.tsx        # Claims & verdicts table
│   │       ├── EvidenceList.tsx      # Evidence list component
│   │       └── SourceCredibilityCard.tsx  # Source credibility stats
│   ├── lib/
│   │   ├── api-client.ts             # API client utilities
│   │   └── types.ts                   # TypeScript type definitions
│   ├── Dockerfile
│   ├── next.config.mjs
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   └── tsconfig.json
├── scripts/
│   ├── init_db.sh                    # Database initialization script
│   └── run_tests.sh                  # Test runner script
├── data/                              # Data directory (MBFC CSV, SQLite DB)
├── docker-compose.yml                 # Docker Compose configuration
└── README.md                          # This file
```

## Database Schema

### Documents Table
- `id`: Primary key
- `url`: Article URL (optional)
- `title`: Article title (optional)
- `source_domain`: Extracted domain from URL
- `raw_text`: Full article text
- `created_at`: Timestamp

### Claims Table
- `id`: Primary key
- `document_id`: Foreign key to documents
- `text`: Claim text
- `topic`: Claim topic (optional)
- `confidence`: Extraction confidence (0-1)

### Evidence Table
- `id`: Primary key
- `claim_id`: Foreign key to claims
- `source_domain`: Source domain
- `url`: Evidence URL
- `snippet`: Evidence text snippet
- `credibility`: MBFC credibility score (0-1)
- `relevance`: Relevance score

### Verdicts Table
- `id`: Primary key
- `claim_id`: Foreign key to claims
- `label`: Verdict label (True/False/Misleading/Unverified)
- `confidence`: Confidence score (0-1)
- `rationale`: GPT-generated rationale
- `model_version`: Model version used
- `created_at`: Timestamp

### Sources Table
- `id`: Primary key
- `domain`: Unique domain identifier
- `name`: Source name
- `bias`: Political bias classification
- `credibility`: Credibility score (0-1)
- `url`: Source URL

## Data Flow

1. **Input Reception**: User submits input via one of three modes:
   - **Claim**: Direct claim text
   - **URL**: Article URL (fetched and parsed)
   - **Text**: Pasted article text

2. **Ingestion**:
   - If URL mode: Fetch HTML, extract text using BeautifulSoup
   - Normalize text (remove extra whitespace)
   - Store document in database

3. **Claim Extraction**:
   - If claim mode: Use input directly as single claim
   - If URL/text mode: Send text to GPT-4o-mini with extraction prompt
   - GPT returns JSON with up to 5 claims (text, topic, confidence)
   - Store claims in database

4. **Evidence Retrieval** (per claim):
   - Query GDELT API with claim text
   - Query Google Fact Check API with claim text
   - Combine results from both sources
   - Look up source credibility in MBFC dataset
   - Rank evidence by: `relevance_score + credibility_score`
   - Store top 20 evidence items per claim

5. **Fact-Checking** (per claim):
   - Send claim + evidence snippets to GPT-4o-mini
   - GPT returns JSON with:
     - `label`: True/False/Misleading/Unverified
     - `confidence`: 0-1 score
     - `rationale`: Explanation
   - Store verdict in database

6. **Aggregation**:
   - Aggregate claim-level verdicts to article-level:
     - Weighted scoring: True=+1.0, False=-1.0, Misleading=-0.5, Unverified=0.0
     - Average confidence across all claims
     - Final article verdict based on weighted sum

7. **Storage**:
   - All data persisted in SQLite/PostgreSQL:
     - Documents (for future analysis)
     - Claims (for ML training)
     - Evidence (for source analysis)
     - Verdicts (for model evaluation)

8. **Dashboard Display**:
   - Frontend fetches job by ID
   - Displays article, claims, evidence, and aggregated verdicts
   - Visualizations: pie charts, credibility scores

## Deployment

For detailed deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md).

**Quick Deploy:**
- **Frontend**: Deploy to [Vercel](https://vercel.com) (free, optimized for Next.js)
- **Backend**: Deploy to [Railway](https://railway.app) or [Render](https://render.com) (includes PostgreSQL)
- **Full Stack**: Use Docker Compose on any VPS (see DEPLOYMENT.md)

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL (optional, SQLite used by default)
- API Keys:
  - OpenAI API key
  - GDELT API key (optional)
  - Google Fact Check API key (optional)
  - MBFC dataset CSV file

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -e .
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root (copy from `.env.example`):
   ```bash
   DATABASE_URL=sqlite+aiosqlite:///./data/credence.db
   OPENAI_API_KEY=sk-your-openai-key
   GDELT_API_KEY=your-gdelt-key
   GOOGLE_FACTCHECK_API_KEY=your-google-factcheck-key
   MBFC_DATA_PATH=./data/mbfc.csv
   BACKEND_CORS_ORIGINS=http://localhost:3000
   ```

5. **Initialize database**:
   ```bash
   python -m app.db.init_db
   ```
   This creates the database schema and seeds MBFC data if available.

6. **Run the backend**:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`
   API docs at `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure environment**:
   Create a `.env.local` file:
   ```bash
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   ```

4. **Run the frontend**:
   ```bash
   npm run dev
   ```

   The app will be available at `http://localhost:3000`

### Using Docker Compose

1. **Create `.env` file** in project root (see `.env.example`)

2. **Run with Docker Compose**:
   ```bash
   docker-compose up
   ```

   This starts:
   - PostgreSQL database on port 5432
   - Backend API on port 8000
   - Frontend on port 3000

### MBFC Dataset

The MBFC (Media Bias/Fact Check) dataset should be a CSV file with columns:
- `domain`: Source domain
- `name`: Source name
- `bias`: Political bias classification
- `credibility`: Credibility score (0-1)
- `url`: Source URL

Place the file at `./data/mbfc.csv` (or update `MBFC_DATA_PATH` in `.env`).

## API Endpoints

### POST `/api/v1/verify`
Submit a verification request.

**Request Body**:
```json
{
  "mode": "claim|url|text",
  "claim": "Optional claim text (if mode=claim)",
  "url": "Optional URL (if mode=url)",
  "text": "Optional article text (if mode=text)"
}
```

**Response**: `VerificationJob` object with job_id, status, document, claims, verdicts, evidences, and aggregated article verdict.

### GET `/api/v1/jobs/{job_id}`
Retrieve a verification job by ID.

**Response**: `VerificationJob` object.

### GET `/api/v1/sources`
List all sources from MBFC dataset.

**Response**: Array of `Source` objects.

### POST `/api/v1/admin/verdicts/{verdict_id}`
Override a verdict (requires API key).

**Request Body**:
```json
{
  "label": "True|False|Misleading|Unverified",
  "confidence": 0.0-1.0
}
```

### GET `/api/v1/health`
Health check endpoint.

## ML Training Data

All verification data is stored in the database for future ML model training:

- **Documents**: Raw article text for feature extraction
- **Claims**: Extracted claims with topics and confidence
- **Evidence**: Evidence snippets with credibility scores
- **Verdicts**: Human/GPT labels with confidence scores

Use `app.ml.dataset_builder.build_dataset()` to extract training data from the database.

## Technology Stack

- **Backend**: FastAPI, SQLAlchemy, Pydantic, OpenAI, httpx, BeautifulSoup
- **Frontend**: Next.js 14, React 18, TypeScript, Tailwind CSS, Recharts
- **Database**: SQLite (default) or PostgreSQL
- **APIs**: OpenAI GPT-4o-mini, GDELT, Google Fact Check API
- **ML**: scikit-learn (for future model training)

## License

See LICENSE file for details.
