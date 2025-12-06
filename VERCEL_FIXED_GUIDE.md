# ✅ Vercel Deployment - Fixed & Ready

I've fixed common issues. Here's what changed and how to deploy successfully.

---

## 🔧 What I Fixed

1. ✅ **Fixed `next.config.mjs`** - Removed `output: 'standalone'` (causes Vercel build issues)
2. ✅ **Improved `api/index.py`** - Added path resolution for better imports
3. ✅ **Added `api/__init__.py`** - Helps Python find modules
4. ✅ **Created troubleshooting guide** - `VERCEL_TROUBLESHOOTING.md`

---

## 🚀 Deploy Now (Step-by-Step)

### Step 1: Push Fixed Code

```bash
cd /Users/oladebs/Downloads/Credence-main
git add .
git commit -m "Fix Vercel deployment configuration"
git push
```

### Step 2: Deploy Backend

1. Go to **https://vercel.com** → Login
2. **Add New** → **Project**
3. Import your GitHub repository
4. **Configure**:
   - **Project Name**: `credence-backend` (or any name)
   - **Root Directory**: `backend` ⚠️ **CRITICAL**
   - **Framework Preset**: **Other** (not Next.js!)
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: (leave empty)
   - **Install Command**: `pip install -r requirements.txt`

5. **Environment Variables** (click "Add"):
   ```
   DATABASE_URL=postgresql://user:pass@host:5432/dbname
   OPENAI_API_KEY=sk-your-key-here
   BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app
   VERCEL=1
   ```
   
   **Note**: For `DATABASE_URL`, you need a PostgreSQL database:
   - **Option A**: Vercel Postgres (Storage → Create Database)
   - **Option B**: Supabase (free): https://supabase.com
   - **Option C**: Neon (free): https://neon.tech

6. Click **"Deploy"**

7. **Wait for build** (2-3 minutes)

8. **Copy your backend URL**: `https://credence-backend.vercel.app`

### Step 3: Test Backend

Visit: `https://your-backend-url.vercel.app/api/v1/health`

Should return: `{"status": "ok"}`

If you get an error, check:
- Vercel dashboard → Functions → Click function → View logs
- See `VERCEL_TROUBLESHOOTING.md` for specific errors

### Step 4: Deploy Frontend

1. In Vercel dashboard, click **"Add New"** → **"Project"**
2. Import the **same repository** (yes, same repo!)
3. **Configure**:
   - **Project Name**: `credence-frontend` (or any name)
   - **Root Directory**: `frontend` ⚠️ **CRITICAL**
   - **Framework Preset**: **Next.js** (auto-detected)
   - **Build Command**: `npm run build` (default)
   - **Output Directory**: `.next` (default)

4. **Environment Variable**:
   - **Key**: `NEXT_PUBLIC_API_BASE_URL`
   - **Value**: Your backend URL from Step 2.8
   - Example: `https://credence-backend.vercel.app`

5. Click **"Deploy"**

6. **Copy your frontend URL**: `https://credence-frontend.vercel.app`

### Step 5: Connect Frontend & Backend

1. Go to **backend project** in Vercel
2. **Settings** → **Environment Variables**
3. Find `BACKEND_CORS_ORIGINS`
4. Update to your frontend URL: `https://credence-frontend.vercel.app`
5. Save (Vercel will auto-redeploy)

### Step 6: Initialize Database

You need to run the database initialization:

**Option A: Using Vercel CLI** (Recommended)
```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Link to your backend project
cd backend
vercel link

# Pull environment variables
vercel env pull

# Initialize database
python -m app.db.init_db
```

**Option B: Add as Deploy Command** (Temporary)
1. Backend project → Settings → Deploy
2. Add one-time command: `python -m app.db.init_db`
3. Redeploy

**Option C: Use External Tool**
- Connect to your database directly
- Run the SQL schema creation

### Step 7: Test Everything

1. Visit your frontend: `https://credence-frontend.vercel.app`
2. Try submitting a claim
3. Check browser console (F12) for errors
4. Check Vercel function logs if there are issues

---

## ⚠️ Common Issues & Quick Fixes

### Issue: "Build failed" on backend

**Check**:
- [ ] Root directory is `backend` (not root)
- [ ] Framework is "Other" (not Next.js)
- [ ] Build command is `pip install -r requirements.txt`
- [ ] `requirements.txt` includes `mangum>=0.17.0`

**Fix**: See `VERCEL_TROUBLESHOOTING.md` → "Build Errors"

### Issue: "404 Not Found"

**Check**:
- [ ] `vercel.json` exists in `backend/` folder
- [ ] Routes are configured correctly
- [ ] `api/index.py` exists

**Fix**: See `VERCEL_TROUBLESHOOTING.md` → "Runtime Errors"

### Issue: "Function timeout"

**Problem**: Fact-checking takes >10 seconds

**Solutions**:
1. Upgrade to Vercel Pro ($20/month) for 60s limit
2. Use Railway for backend instead (no limits)
3. Optimize code to be faster

### Issue: Frontend build fails

**Check**:
- [ ] Root directory is `frontend`
- [ ] `next.config.mjs` doesn't have `output: 'standalone'` (I fixed this!)
- [ ] No TypeScript errors

**Fix**: Run `npm run build` locally first to catch errors

### Issue: "Cannot connect to backend"

**Check**:
- [ ] `NEXT_PUBLIC_API_BASE_URL` is set correctly
- [ ] Backend URL is accessible (test in browser)
- [ ] CORS is configured (`BACKEND_CORS_ORIGINS`)

---

## 📋 Pre-Deployment Checklist

Before deploying, make sure:

- [ ] Code is pushed to GitHub
- [ ] `backend/vercel.json` exists
- [ ] `backend/api/index.py` exists
- [ ] `requirements.txt` includes `mangum`
- [ ] `next.config.mjs` doesn't have `output: 'standalone'` ✅ (fixed)
- [ ] You have a PostgreSQL database URL
- [ ] You have OpenAI API key
- [ ] Root directories will be set correctly (`backend` and `frontend`)

---

## 🆘 Still Having Issues?

1. **Check the troubleshooting guide**: `VERCEL_TROUBLESHOOTING.md`
2. **Check Vercel logs**: Dashboard → Your project → Functions/Deployments
3. **Test locally first**:
   ```bash
   # Backend
   cd backend
   pip install -r requirements.txt
   python -c "from app.main import app; print('OK')"
   
   # Frontend
   cd frontend
   npm install
   npm run build
   ```

4. **Share the specific error** and I can help debug!

---

## 💡 Alternative: Easier Option

If Vercel keeps giving you trouble, consider:

**Vercel Frontend + Railway Backend**

This is often **easier and more reliable**:
- ✅ No serverless complexity
- ✅ No execution time limits
- ✅ Built-in database
- ✅ Better for FastAPI

See: `QUICK_START_DEPLOY.md` (20 minutes, much easier!)

---

## ✅ Success Indicators

You'll know it's working when:

- ✅ Backend health check returns: `{"status": "ok"}`
- ✅ Frontend loads without errors
- ✅ Can submit claims/URLs/text
- ✅ Results display correctly
- ✅ No console errors
- ✅ No timeout errors

---

**Ready to deploy?** Follow the steps above, and if you hit any issues, check `VERCEL_TROUBLESHOOTING.md`! 🚀

