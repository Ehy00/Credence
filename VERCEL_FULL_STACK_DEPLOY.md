# 🚀 Deploy Everything to Vercel (Full Stack)

Yes, you can deploy both frontend and backend to Vercel! However, FastAPI needs special configuration for Vercel's serverless functions.

---

## ⚠️ Important Considerations

### Pros of Vercel for Both:
- ✅ Single platform (easier management)
- ✅ Free tier available
- ✅ Automatic deployments
- ✅ Built-in CDN and edge network
- ✅ Great Next.js integration

### Cons/Challenges:
- ⚠️ **Serverless function limits**: 10s execution on free tier, 60s on Pro
- ⚠️ **Cold starts**: First request may be slower
- ⚠️ **Database connections**: Need connection pooling (PostgreSQL)
- ⚠️ **File storage**: MBFC dataset needs external storage (S3, etc.)
- ⚠️ **More complex setup**: Requires Mangum adapter for FastAPI

### Recommendation:
- **For production**: Railway/Render for backend is easier
- **For simplicity**: Vercel for both works, but requires more setup

---

## 📋 Prerequisites

- GitHub account
- Vercel account (free tier works)
- OpenAI API key
- PostgreSQL database (Vercel Postgres, Supabase, or Railway Postgres)
- (Optional) External storage for MBFC dataset (Vercel Blob, S3, etc.)

---

## Part 1: Set Up Backend for Vercel

### Step 1.1: Install Mangum Adapter

Mangum converts FastAPI to work with Vercel's serverless functions.

```bash
cd backend
pip install mangum
```

Add to `requirements.txt`:
```
mangum>=0.17.0
```

### Step 1.2: Create Vercel Configuration

Create `backend/vercel.json`:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "api/index.py"
    }
  ],
  "env": {
    "PYTHON_VERSION": "3.11"
  }
}
```

### Step 1.3: Create Serverless Entry Point

Create `backend/api/index.py`:

```python
from mangum import Mangum
from app.main import app

# Wrap FastAPI app with Mangum for Vercel
handler = Mangum(app, lifespan="off")
```

### Step 1.4: Update Main App

Update `backend/app/main.py` to handle serverless:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging_config import configure_logging
from app.api.v1 import verify, jobs, sources, admin, health

configure_logging()

app = FastAPI(title="Credence Lite API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(verify.router, prefix="/api/v1")
app.include_router(jobs.router, prefix="/api/v1")
app.include_router(sources.router, prefix="/api/v1")
app.include_router(admin.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Credence Lite API is running"}

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Step 1.5: Update Database Connection

For serverless, you need connection pooling. Update `backend/app/db/session.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import os

# Use connection pooling for serverless
if os.getenv("VERCEL"):
    # Serverless: use connection pooling
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        pool_size=1,
        max_overflow=0,
        connect_args={"connect_timeout": 10}
    )
else:
    # Local: standard connection
    engine = create_engine(settings.DATABASE_URL, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

---

## Part 2: Deploy Backend to Vercel

### Step 2.1: Push Code to GitHub

```bash
cd /Users/oladebs/Downloads/Credence-main
git add .
git commit -m "Add Vercel serverless support"
git push
```

### Step 2.2: Deploy Backend

1. Go to **https://vercel.com**
2. Click **"Add New"** → **"Project"**
3. Import your repository
4. **Configure**:
   - **Root Directory**: `backend`
   - **Framework Preset**: Other
   - **Build Command**: `pip install -r requirements.txt` (or `pip install -e .`)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

### Step 2.3: Add Environment Variables

In Vercel project settings → **Environment Variables**:

```
DATABASE_URL=postgresql://user:pass@host:5432/dbname
OPENAI_API_KEY=sk-your-key
GDELT_API_KEY=your-key (optional)
GOOGLE_FACTCHECK_API_KEY=your-key (optional)
MBFC_DATA_PATH=./data/mbfc.csv
BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app
VERCEL=1
```

**Note**: For `DATABASE_URL`, you'll need an external PostgreSQL:
- **Vercel Postgres** (recommended, integrates well)
- **Supabase** (free tier available)
- **Railway Postgres** (can use separately)
- **Neon** (serverless Postgres, free tier)

### Step 2.4: Deploy

1. Click **"Deploy"**
2. Wait for build to complete
3. Copy your backend URL: `https://your-backend.vercel.app`

### Step 2.5: Test Backend

Visit: `https://your-backend.vercel.app/api/v1/health`

Should return: `{"status": "ok"}`

---

## Part 3: Deploy Frontend to Vercel

### Step 3.1: Create Frontend Project

1. In Vercel dashboard, click **"Add New"** → **"Project"**
2. Import the **same repository**
3. **Configure**:
   - **Root Directory**: `frontend`
   - **Framework Preset**: Next.js (auto-detected)
   - **Build Command**: `npm run build` (default)
   - **Output Directory**: `.next` (default)

### Step 3.2: Add Environment Variable

**Environment Variable**:
- **Key**: `NEXT_PUBLIC_API_BASE_URL`
- **Value**: Your backend Vercel URL (from Step 2.4)

### Step 3.3: Deploy

1. Click **"Deploy"**
2. Wait for build
3. Copy frontend URL: `https://your-frontend.vercel.app`

---

## Part 4: Connect Frontend and Backend

### Step 4.1: Update CORS

1. Go to backend project in Vercel
2. **Settings** → **Environment Variables**
3. Update `BACKEND_CORS_ORIGINS` to your frontend URL
4. Redeploy backend

### Step 4.2: Test Integration

1. Visit your frontend URL
2. Try submitting a claim
3. Check browser console for errors

---

## Part 5: Set Up Database

### Option A: Vercel Postgres (Recommended)

1. In Vercel dashboard → **Storage** → **Create Database**
2. Select **Postgres**
3. Vercel will auto-set `DATABASE_URL`
4. Initialize database:
   - Use Vercel CLI: `vercel env pull`
   - Run: `python -m app.db.init_db`

### Option B: External PostgreSQL

Use one of these:
- **Supabase**: https://supabase.com (free tier)
- **Neon**: https://neon.tech (serverless, free tier)
- **Railway**: https://railway.app (separate service)

Then set `DATABASE_URL` in Vercel environment variables.

---

## Part 6: Handle MBFC Dataset

Since Vercel serverless functions have limited file system access:

### Option A: External Storage (Recommended)

1. Upload `mbfc.csv` to:
   - **Vercel Blob Storage**
   - **AWS S3**
   - **Cloudflare R2**
   - **GitHub Releases** (download on startup)

2. Update code to download on startup:
```python
# In app/integrations/mbfc_client.py
import httpx

def __init__(self):
    if os.getenv("VERCEL"):
        # Download from external storage
        url = os.getenv("MBFC_DATA_URL")
        response = httpx.get(url)
        self.df = pd.read_csv(StringIO(response.text))
    else:
        # Local file
        self.df = pd.read_csv(settings.MBFC_DATA_PATH)
```

### Option B: Include in Build

If file is small (< 1MB), you can include it in the build:
- Add to `backend/data/mbfc.csv`
- Commit to Git
- Vercel will include it in the build

---

## Troubleshooting

### Backend Issues

**Problem**: Function timeout
- **Solution**: Optimize long-running operations, use background jobs, or upgrade to Pro

**Problem**: Database connection errors
- **Solution**: Use connection pooling, check `DATABASE_URL` format

**Problem**: Cold start delays
- **Solution**: Use Vercel Pro (faster cold starts), or keep functions warm

**Problem**: File not found (MBFC dataset)
- **Solution**: Use external storage or include in build

### Frontend Issues

**Problem**: Can't connect to backend
- **Solution**: Verify `NEXT_PUBLIC_API_BASE_URL` matches backend URL
- **Solution**: Check CORS settings

**Problem**: API calls timeout
- **Solution**: Backend functions may be timing out, check Vercel function logs

---

## Alternative: Simpler Approach

If Vercel serverless is too complex, consider:

1. **Frontend on Vercel** (easy, recommended)
2. **Backend on Railway/Render** (easier for FastAPI)

This gives you:
- ✅ Best of both worlds
- ✅ Easier setup
- ✅ Better performance for FastAPI
- ✅ No serverless limitations

See `QUICK_START_DEPLOY.md` for this approach.

---

## Cost Comparison

### Vercel Full Stack:
- **Free Tier**: 
  - 100GB bandwidth
  - 100 serverless function invocations/day
  - 10s function execution limit
- **Pro Tier**: $20/month
  - Unlimited bandwidth
  - 60s function execution
  - Better performance

### Vercel Frontend + Railway Backend:
- **Vercel**: FREE (frontend)
- **Railway**: $5/month (backend + database)
- **Total**: $5/month

---

## Success Checklist

- [ ] Backend deployed to Vercel
- [ ] Backend health check works
- [ ] Database connected and initialized
- [ ] Frontend deployed to Vercel
- [ ] Frontend connects to backend
- [ ] Can submit claims/URLs/text
- [ ] Results display correctly
- [ ] No timeout errors
- [ ] MBFC dataset accessible (if using)

---

## Next Steps

1. **Monitor function logs** in Vercel dashboard
2. **Set up alerts** for errors
3. **Optimize cold starts** (if needed)
4. **Consider Pro tier** if hitting limits
5. **Set up custom domains** (optional)

---

**Your app is now fully deployed on Vercel! 🎉**

If you run into issues with serverless limitations, consider the hybrid approach (Vercel frontend + Railway backend) for better reliability.

