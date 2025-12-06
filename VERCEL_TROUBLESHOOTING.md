# 🔧 Vercel Deployment Troubleshooting Guide

Common issues and solutions when deploying to Vercel.

---

## 🚨 Quick Diagnosis

**What error are you seeing?**
1. Build fails? → See "Build Errors" below
2. Function timeout? → See "Timeout Issues"
3. Import errors? → See "Import Errors"
4. 404/500 errors? → See "Runtime Errors"
5. Frontend can't connect? → See "Connection Issues"

---

## 🔴 Build Errors

### Error: "Module not found" or "Import error"

**Problem**: Python can't find your modules.

**Solution 1**: Check root directory
- In Vercel project settings → **Root Directory** must be `backend`
- Not the root of the repo!

**Solution 2**: Add `__init__.py` files
```bash
# Make sure these exist:
backend/__init__.py
backend/app/__init__.py
backend/api/__init__.py
```

**Solution 3**: Update `vercel.json` to include app directory:
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

### Error: "Mangum not found"

**Problem**: Mangum not installed.

**Solution**: 
1. Check `requirements.txt` includes `mangum>=0.17.0`
2. Make sure you're using `requirements.txt` in build command
3. Build command should be: `pip install -r requirements.txt`

### Error: "Build command failed"

**Problem**: Build command is wrong.

**Solution**: In Vercel project settings:
- **Build Command**: `pip install -r requirements.txt` (or `pip install -e .`)
- **Output Directory**: (leave empty)
- **Install Command**: `pip install -r requirements.txt`

---

## 🔴 Runtime Errors (500, 404)

### Error: 404 Not Found

**Problem**: Routes not configured correctly.

**Solution**: Update `backend/vercel.json`:
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
    },
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}
```

### Error: 500 Internal Server Error

**Problem**: Application error.

**Solution**: 
1. Check Vercel function logs:
   - Vercel dashboard → Your project → **Functions** tab
   - Click on a function → View logs
2. Common causes:
   - Missing environment variables
   - Database connection error
   - Import errors

### Error: "Handler not found"

**Problem**: `api/index.py` not exporting `handler`.

**Solution**: Make sure `backend/api/index.py` has:
```python
from mangum import Mangum
from app.main import app

handler = Mangum(app, lifespan="off")
```

**Important**: The variable must be named `handler` (not `app` or `main`).

---

## 🔴 Import Errors

### Error: "No module named 'app'"

**Problem**: Python can't find the app module.

**Solution 1**: Check file structure:
```
backend/
  ├── api/
  │   └── index.py
  ├── app/
  │   ├── __init__.py
  │   └── main.py
  └── vercel.json
```

**Solution 2**: Update `api/index.py` to use absolute imports:
```python
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from mangum import Mangum
from app.main import app

handler = Mangum(app, lifespan="off")
```

### Error: "Cannot import from app.main"

**Problem**: Path resolution issue.

**Solution**: Create `backend/api/__init__.py` (empty file):
```bash
touch backend/api/__init__.py
```

---

## 🔴 Timeout Issues

### Error: "Function execution timeout"

**Problem**: Fact-checking takes >10 seconds (free tier limit).

**Solutions**:
1. **Upgrade to Vercel Pro** ($20/month) - 60 second limit
2. **Use Railway for backend** instead (no limits)
3. **Optimize your code**:
   - Make API calls async
   - Process in background
   - Return job ID immediately, process async

### Error: "Cold start timeout"

**Problem**: First request takes too long.

**Solution**: 
- This is normal for serverless (1-2 seconds)
- Consider Pro tier for better performance
- Or use Railway (no cold starts)

---

## 🔴 Database Connection Errors

### Error: "Database connection failed"

**Problem**: Can't connect to PostgreSQL.

**Solution 1**: Check `DATABASE_URL` format:
```
postgresql://user:password@host:5432/dbname
```
Not: `postgresql+psycopg2://...` (remove +psycopg2)

**Solution 2**: Verify environment variable is set:
- Vercel dashboard → Settings → Environment Variables
- Make sure it's set for **Production**, **Preview**, and **Development**

**Solution 3**: Check database is accessible:
- If using external DB (Supabase, Neon), verify connection string
- Check if database allows connections from Vercel IPs

**Solution 4**: Update connection pooling (already done in `session.py`):
```python
# Should already be in your code
if os.getenv("VERCEL"):
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        pool_size=1,
        max_overflow=0,
        connect_args={"connect_timeout": 10}
    )
```

---

## 🔴 Frontend Build Errors

### Error: "Build failed" on frontend

**Problem**: Next.js build error.

**Solution 1**: Check root directory:
- Must be `frontend` (not root of repo)

**Solution 2**: Check `next.config.mjs`:
```javascript
const nextConfig = {
  output: 'standalone',  // Remove this for Vercel!
};
```
**Fix**: Remove `output: 'standalone'` - Vercel handles this automatically.

**Solution 3**: Check for TypeScript errors:
- Run `npm run build` locally
- Fix any TypeScript errors
- Push fixes to GitHub

### Error: "Environment variable not found"

**Problem**: `NEXT_PUBLIC_API_BASE_URL` not accessible.

**Solution**:
1. Must start with `NEXT_PUBLIC_` to be accessible in browser
2. Set in Vercel → Settings → Environment Variables
3. Redeploy after adding variables
4. Clear browser cache

---

## 🔴 Connection Issues (Frontend ↔ Backend)

### Error: "Failed to fetch" or CORS error

**Problem**: Frontend can't connect to backend.

**Solution 1**: Check `NEXT_PUBLIC_API_BASE_URL`:
- Must be your backend Vercel URL
- Example: `https://credence-backend.vercel.app`
- Not: `http://localhost:8000`

**Solution 2**: Check CORS settings:
- In backend, `BACKEND_CORS_ORIGINS` must include frontend URL
- Example: `https://credence-frontend.vercel.app`
- Or use `*` for development (not recommended for production)

**Solution 3**: Verify backend is deployed:
- Visit backend URL directly: `https://your-backend.vercel.app/api/v1/health`
- Should return: `{"status": "ok"}`

---

## 🔴 Common Configuration Mistakes

### Mistake 1: Wrong Root Directory

**Backend**: Must be `backend`
**Frontend**: Must be `frontend`

**How to fix**: 
- Vercel project → Settings → General → Root Directory

### Mistake 2: Missing Environment Variables

**Required for backend**:
- `DATABASE_URL`
- `OPENAI_API_KEY`
- `BACKEND_CORS_ORIGINS`
- `VERCEL=1` (optional, but helps)

**Required for frontend**:
- `NEXT_PUBLIC_API_BASE_URL`

### Mistake 3: Wrong Build Command

**Backend**:
- ❌ Wrong: `npm install`
- ✅ Correct: `pip install -r requirements.txt`

**Frontend**:
- ✅ Correct: `npm run build` (default)

### Mistake 4: Using Dockerfile

**Problem**: Vercel doesn't use Dockerfile by default.

**Solution**: Remove or ignore Dockerfile, use `vercel.json` instead.

---

## 🛠️ Step-by-Step Fix Process

### If Build Fails:

1. **Check logs**:
   - Vercel dashboard → Deployments → Click failed deployment → View logs

2. **Verify structure**:
   ```bash
   # Should look like this:
   backend/
     ├── api/
     │   └── index.py
     ├── app/
     │   └── main.py
     ├── requirements.txt
     └── vercel.json
   ```

3. **Test locally** (if possible):
   ```bash
   cd backend
   pip install -r requirements.txt
   python -c "from app.main import app; print('OK')"
   ```

4. **Check requirements.txt**:
   - Must include `mangum>=0.17.0`
   - All dependencies listed

5. **Verify vercel.json**:
   - Points to `api/index.py`
   - Routes configured correctly

### If Runtime Fails:

1. **Check function logs**:
   - Vercel → Functions tab → Click function → Logs

2. **Test endpoint directly**:
   ```bash
   curl https://your-backend.vercel.app/api/v1/health
   ```

3. **Check environment variables**:
   - All required vars set?
   - Correct format?

4. **Verify database**:
   - Can you connect from local machine?
   - Connection string correct?

---

## 📋 Quick Checklist

Before deploying, verify:

- [ ] Root directory set correctly (`backend` or `frontend`)
- [ ] `vercel.json` exists in backend folder
- [ ] `api/index.py` exists and exports `handler`
- [ ] `requirements.txt` includes `mangum`
- [ ] Environment variables set in Vercel
- [ ] Database connection string correct
- [ ] `next.config.mjs` doesn't have `output: 'standalone'`
- [ ] Code pushed to GitHub
- [ ] Build command correct

---

## 🆘 Still Stuck?

### Get More Help:

1. **Check Vercel logs**:
   - Dashboard → Your project → Functions/Deployments → Logs

2. **Test locally first**:
   ```bash
   # Backend
   cd backend
   pip install -r requirements.txt
   python -m app.main
   
   # Frontend
   cd frontend
   npm install
   npm run build
   ```

3. **Simplify and test**:
   - Create minimal `api/index.py`:
   ```python
   def handler(request):
       return {"status": "ok"}
   ```
   - Deploy this first
   - Then add complexity

4. **Consider alternative**:
   - If Vercel keeps failing, use **Railway for backend**
   - Much easier for FastAPI
   - See `QUICK_START_DEPLOY.md`

---

## 💡 Pro Tips

1. **Deploy backend first**, test it, then deploy frontend
2. **Use Vercel CLI** for better debugging:
   ```bash
   npm i -g vercel
   vercel login
   vercel dev  # Test locally
   ```
3. **Check function logs** in real-time during testing
4. **Start simple**: Deploy minimal version first, add features gradually
5. **Use Railway for backend** if Vercel is too complex - it's much easier!

---

**Need specific help?** Share the exact error message and I can help debug! 🚀

