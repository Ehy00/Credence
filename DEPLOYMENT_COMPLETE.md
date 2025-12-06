# 🚀 Deployment Guide - Your Specific URLs

## ✅ Backend Status

**Your Railway Backend URL:**
```
https://credence-production-6240.up.railway.app
```

**Status:** ✅ LIVE and Working!

---

## 🧪 Test Your Backend

Try these URLs in your browser:

1. **Root Endpoint:**
   ```
   https://credence-production-6240.up.railway.app/
   ```
   ✅ Should show: `{"message":"Credence Lite API is running"}`

2. **Health Check:**
   ```
   https://credence-production-6240.up.railway.app/api/v1/health
   ```
   ✅ Should show: `{"status": "ok"}`

3. **API Documentation:**
   ```
   https://credence-production-6240.up.railway.app/docs
   ```
   ✅ Should show FastAPI interactive documentation

---

## 📋 Step 1: Deploy Frontend to Vercel

### 1.1 Go to Vercel
- Visit: **https://vercel.com**
- Sign up/Login with GitHub

### 1.2 Create New Project
1. Click **"Add New"** → **"Project"**
2. Import your GitHub repository (`Credence`)
3. Click **"Import"**

### 1.3 Configure Project
**IMPORTANT Settings:**
- **Root Directory**: Click **"Edit"** → Set to: `frontend`
- **Framework Preset**: Next.js (auto-detected)
- **Build Command**: `npm run build` (default)
- **Output Directory**: `.next` (default)

### 1.4 Add Environment Variable
**Environment Variables** section:
- **Key**: `NEXT_PUBLIC_API_BASE_URL`
- **Value**: `https://credence-production-6240.up.railway.app`
- Make sure it's enabled for: **Production**, **Preview**, and **Development**

### 1.5 Deploy
1. Click **"Deploy"**
2. Wait 2-3 minutes for build
3. **Copy your Vercel URL** (will look like: `https://credence.vercel.app`)

---

## 📋 Step 2: Update CORS in Railway

After you get your Vercel frontend URL:

1. Go to **Railway dashboard**
2. Click on your **backend service**
3. Go to **"Variables"** tab
4. Find or add: `BACKEND_CORS_ORIGINS`
5. Set value to your Vercel URL:
   ```
   https://your-frontend.vercel.app
   ```
   (Replace with your actual Vercel URL)
6. Railway will automatically redeploy

---

## 📋 Step 3: Initialize Database

You need to initialize the PostgreSQL database:

### Option A: Railway CLI (Recommended)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link to your project
railway link

# Navigate to backend
cd backend

# Initialize database
railway run python -m app.db.init_db
```

### Option B: One-Time Deploy Command

1. Railway → Your service → **Settings** → **Deploy**
2. Add **"Run Command"**: `python -m app.db.init_db`
3. Save and redeploy (one-time)

---

## 📋 Step 4: Verify Environment Variables

Make sure these are set in Railway (Variables tab):

- ✅ `DATABASE_URL` - Auto-set by Railway (if PostgreSQL is added)
- ✅ `OPENAI_API_KEY` - Your OpenAI API key (`sk-...`)
- ✅ `BACKEND_CORS_ORIGINS` - Your Vercel frontend URL
- ⚠️ `GDELT_API_KEY` - Optional
- ⚠️ `GOOGLE_FACTCHECK_API_KEY` - Optional
- ⚠️ `MBFC_DATA_PATH` - Optional (default: `./data/mbfc.csv`)

**To add PostgreSQL database in Railway:**
1. In your Railway project, click **"+ New"**
2. Select **"Database"** → **"Add PostgreSQL"**
3. Railway will auto-set `DATABASE_URL`

---

## 🎯 Step 5: Test Your Full Stack

Once frontend is deployed:

1. **Visit your Vercel URL**
2. **Try submitting:**
   - A claim (e.g., "The sky is blue")
   - An article URL
   - Pasted article text
3. **Check browser console** (F12) for any errors
4. **Verify results display correctly**

---

## 🔗 Your URLs

**Backend:**
- URL: `https://credence-production-6240.up.railway.app`
- Health: `https://credence-production-6240.up.railway.app/api/v1/health`
- Docs: `https://credence-production-6240.up.railway.app/docs`

**Frontend:**
- URL: `https://your-frontend.vercel.app` (you'll get this after Vercel deployment)

---

## 🆘 Troubleshooting

### Backend Issues

**Health check fails?**
- Check Railway logs
- Verify environment variables are set
- Check if database is initialized

**API returns 500 errors?**
- Check Railway logs for Python errors
- Verify `OPENAI_API_KEY` is set correctly
- Check database connection

### Frontend Issues

**Can't connect to backend?**
- Verify `NEXT_PUBLIC_API_BASE_URL` in Vercel matches backend URL
- Check CORS settings in Railway
- Ensure backend URL is accessible

**Build fails on Vercel?**
- Check Vercel build logs
- Verify root directory is `frontend`
- Check for TypeScript errors

---

## ✅ Success Checklist

- [ ] Backend deployed to Railway ✅
- [ ] Backend URL accessible ✅
- [ ] Health check works
- [ ] Frontend deployed to Vercel
- [ ] CORS configured correctly
- [ ] Database initialized
- [ ] Environment variables set
- [ ] Can submit claims/URLs/text
- [ ] Results display correctly

---

**You're almost there! Deploy the frontend and connect them! 🚀**

