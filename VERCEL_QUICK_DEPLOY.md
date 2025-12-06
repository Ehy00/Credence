# ⚡ Quick Deploy: Both on Vercel

**Simplified guide for deploying frontend AND backend to Vercel.**

---

## ✅ What I've Set Up For You

I've already created the necessary files:
- ✅ `backend/vercel.json` - Vercel configuration
- ✅ `backend/api/index.py` - Serverless function entry point
- ✅ Updated `requirements.txt` with Mangum
- ✅ Updated database connection for serverless

**You're ready to deploy!**

---

## 🚀 Quick Steps (15 minutes)

### Step 1: Push to GitHub

```bash
cd /Users/oladebs/Downloads/Credence-main
git add .
git commit -m "Add Vercel serverless support"
git push
```

### Step 2: Deploy Backend to Vercel

1. Go to **https://vercel.com** → Sign up/login
2. **Add New** → **Project** → Import your repo
3. **Configure Backend**:
   - **Root Directory**: `backend` ⚠️ IMPORTANT
   - **Framework**: Other
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: (leave empty)

4. **Environment Variables**:
   ```
   DATABASE_URL=postgresql://... (from Vercel Postgres or external)
   OPENAI_API_KEY=sk-your-key
   BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app
   VERCEL=1
   ```

5. **Deploy** → Copy backend URL

### Step 3: Set Up Database

**Option A: Vercel Postgres** (Easiest)
1. Vercel dashboard → **Storage** → **Create Database** → **Postgres**
2. Vercel auto-sets `DATABASE_URL`
3. Initialize: Use Vercel CLI or add init command

**Option B: External PostgreSQL**
- Use Supabase (free): https://supabase.com
- Use Neon (free): https://neon.tech
- Use Railway Postgres (separate service)

### Step 4: Deploy Frontend to Vercel

1. **Add New** → **Project** → Import **same repo**
2. **Configure Frontend**:
   - **Root Directory**: `frontend` ⚠️ IMPORTANT
   - **Framework**: Next.js (auto-detected)

3. **Environment Variable**:
   - `NEXT_PUBLIC_API_BASE_URL` = your backend Vercel URL

4. **Deploy** → Copy frontend URL

### Step 5: Connect Them

1. Go to **backend project** → **Settings** → **Environment Variables**
2. Update `BACKEND_CORS_ORIGINS` to your frontend URL
3. Redeploy backend

### Step 6: Initialize Database

Use Vercel CLI:
```bash
npm i -g vercel
vercel login
vercel link  # Link to your backend project
vercel env pull  # Get environment variables
cd backend
python -m app.db.init_db
```

Or add as a one-time deploy command in Vercel.

---

## 🎯 Test Your App

1. Visit frontend URL: `https://your-app.vercel.app`
2. Test backend: `https://your-backend.vercel.app/api/v1/health`
3. Submit a claim and verify it works!

---

## ⚠️ Important Notes

### Serverless Limitations:
- **Free tier**: 10-second function execution limit
- **Cold starts**: First request may be slow (~1-2 seconds)
- **File storage**: MBFC dataset needs external storage (see full guide)

### If You Hit Limits:
- Upgrade to Vercel Pro ($20/month) for 60s execution
- Or use hybrid: Vercel frontend + Railway backend (easier)

---

## 🆘 Troubleshooting

**Backend timeout?**
- Your fact-checking might take >10 seconds
- Solution: Upgrade to Pro or use Railway for backend

**Database connection error?**
- Verify `DATABASE_URL` is set correctly
- Check if database is accessible from Vercel

**Cold start too slow?**
- Normal for serverless (1-2 seconds first request)
- Consider Pro tier for better performance

**MBFC dataset not found?**
- Upload to external storage (S3, Vercel Blob)
- Or include in Git if <1MB

---

## 💰 Cost

- **Vercel Free**: 100GB bandwidth, 10s function limit
- **Vercel Pro**: $20/month (60s functions, better performance)
- **Database**: Vercel Postgres or free external (Supabase/Neon)

**Total**: $0-20/month depending on tier

---

## 📖 Full Guide

For detailed instructions, see: `VERCEL_FULL_STACK_DEPLOY.md`

---

## ✅ Success Checklist

- [ ] Backend deployed to Vercel
- [ ] Database connected
- [ ] Frontend deployed to Vercel
- [ ] CORS configured
- [ ] Health check works
- [ ] Can submit claims
- [ ] Results display

---

**You're all set! 🎉**

If serverless limitations become an issue, the hybrid approach (Vercel frontend + Railway backend) is often easier and more reliable for FastAPI apps.

