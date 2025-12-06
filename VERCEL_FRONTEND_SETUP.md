# 🎯 Vercel Frontend Setup - Exact Configuration

## 📋 Vercel Project Settings

### Install Command
**Input:** `npm install`
- This is the default for Next.js
- Vercel will auto-detect this, but you can set it explicitly
- It installs all dependencies from `package.json`

### Build Command
**Input:** `npm run build`
- This is the default for Next.js
- Vercel will auto-detect this
- Builds your Next.js app for production

### Output Directory
**Input:** `.next`
- This is the default for Next.js
- Vercel will auto-detect this
- Where Next.js outputs the built files

### Development Command
**Input:** `npm run dev`
- This is the default for Next.js
- Only used for local development
- Vercel will auto-detect this

---

## 🔑 Environment Variables

### Frontend Environment Variables (Vercel)

**ONLY add this one:**

✅ **`NEXT_PUBLIC_API_BASE_URL`**
- **Value:** `https://credence-production-6240.up.railway.app`
- **Purpose:** Tells frontend where your backend API is
- **Important:** Must start with `NEXT_PUBLIC_` to be accessible in browser

### ❌ Do NOT Add These to Vercel Frontend:

- ❌ `OPENAI_API_KEY` - This is for BACKEND only
- ❌ `GOOGLE_FACTCHECK_API_KEY` - This is for BACKEND only
- ❌ `GDELT_API_KEY` - This is for BACKEND only
- ❌ `DATABASE_URL` - This is for BACKEND only
- ❌ `BACKEND_CORS_ORIGINS` - This is for BACKEND only

**Why?** 
- Frontend code runs in the browser (public)
- API keys should NEVER be in frontend code
- All API calls go through your backend
- Backend handles all API keys securely

---

## 🔐 Where to Add Google Fact Check API Key

**Add it to Railway (Backend), NOT Vercel (Frontend):**

1. Go to **Railway dashboard**
2. Click on your **backend service**
3. Go to **"Variables"** tab
4. Add environment variable:
   - **Key:** `GOOGLE_FACTCHECK_API_KEY`
   - **Value:** Your Google Fact Check API key
5. Railway will auto-redeploy

---

## 📋 Complete Vercel Configuration Summary

### Settings Tab:
- **Framework Preset:** Next.js ✅
- **Root Directory:** `frontend` ⚠️ IMPORTANT
- **Build Command:** `npm run build` (default)
- **Output Directory:** `.next` (default)
- **Install Command:** `npm install` (default)
- **Development Command:** `npm run dev` (default)

### Environment Variables Tab:
**Only add:**
- `NEXT_PUBLIC_API_BASE_URL` = `https://credence-production-6240.up.railway.app`

**That's it!** Just one environment variable for the frontend.

---

## 🔐 Complete Backend Environment Variables (Railway)

Add these in **Railway**, not Vercel:

- ✅ `DATABASE_URL` - Auto-set by Railway (if PostgreSQL added)
- ✅ `OPENAI_API_KEY` - Your OpenAI key (`sk-...`)
- ✅ `GOOGLE_FACTCHECK_API_KEY` - Your Google Fact Check key
- ✅ `BACKEND_CORS_ORIGINS` - Your Vercel frontend URL (after deployment)
- ⚠️ `GDELT_API_KEY` - Optional
- ⚠️ `MBFC_DATA_PATH` - Optional (default: `./data/mbfc.csv`)

---

## 🎯 Quick Reference

**Vercel (Frontend):**
- Install: `npm install`
- Build: `npm run build`
- Env Var: `NEXT_PUBLIC_API_BASE_URL` only

**Railway (Backend):**
- All API keys go here
- All secrets go here
- Database connection here

---

**Summary: Frontend = 1 env var, Backend = All API keys! 🚀**

