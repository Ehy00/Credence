# 🚀 Step-by-Step Deployment Guide

This guide will walk you through deploying your Credence app **without GitHub Actions**. We'll use the easiest platforms: **Railway** (backend) + **Vercel** (frontend).

---

## 📋 Prerequisites

Before starting, make sure you have:
- ✅ A GitHub account (to push your code)
- ✅ An OpenAI API key (`sk-...`)
- ✅ (Optional) GDELT API key
- ✅ (Optional) Google Fact Check API key
- ✅ (Optional) MBFC dataset CSV file

---

## Part 1: Deploy Backend to Railway (15 minutes)

### Step 1.1: Push Code to GitHub

1. **Create a new repository on GitHub** (if you haven't already)
   - Go to https://github.com/new
   - Name it `credence` (or any name)
   - Make it **Public** (for free tier) or **Private**
   - Click "Create repository"

2. **Push your code to GitHub:**
   ```bash
   cd /Users/oladebs/Downloads/Credence-main
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/credence.git
   git push -u origin main
   ```
   Replace `YOUR_USERNAME` with your GitHub username.

### Step 1.2: Create Railway Account

1. Go to **https://railway.app**
2. Click **"Start a New Project"**
3. Sign up with GitHub (recommended) - this connects your GitHub account
4. Authorize Railway to access your repositories

### Step 1.3: Deploy Backend

1. In Railway dashboard, click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Find and select your `credence` repository
4. Railway will detect it's a Python project
5. **IMPORTANT**: Click on the service, then go to **Settings** → **Root Directory**
   - Set it to: `backend`
   - This tells Railway to deploy only the backend folder

### Step 1.4: Add PostgreSQL Database

1. In your Railway project, click **"+ New"**
2. Select **"Database"** → **"Add PostgreSQL"**
3. Railway will create a PostgreSQL database automatically
4. The `DATABASE_URL` environment variable will be auto-set

### Step 1.5: Configure Environment Variables

1. In your Railway service, go to **Variables** tab
2. Add these environment variables:

   ```
   DATABASE_URL=postgresql://... (already set by Railway)
   OPENAI_API_KEY=sk-your-actual-openai-key-here
   GDELT_API_KEY=your-gdelt-key (optional, leave empty if you don't have)
   GOOGLE_FACTCHECK_API_KEY=your-google-key (optional, leave empty if you don't have)
   MBFC_DATA_PATH=./data/mbfc.csv
   BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app
   ```

   **Note**: For `BACKEND_CORS_ORIGINS`, we'll update this after deploying the frontend. For now, you can set it to `*` temporarily (not recommended for production).

3. Click **"Deploy"** or Railway will auto-deploy

### Step 1.6: Get Your Backend URL

1. Once deployed, Railway will show your service URL
2. It will look like: `https://credence-backend-production.up.railway.app`
3. **Copy this URL** - you'll need it for the frontend
4. Test it: Visit `https://your-backend-url.railway.app/api/v1/health`
   - You should see: `{"status": "ok"}`

### Step 1.7: Initialize Database

1. Railway provides a **"Deploy Logs"** section
2. Check if the database was initialized automatically
3. If not, you can add a one-time command:
   - Go to **Settings** → **Deploy**
   - Add a **"Run Command"**: `python -m app.db.init_db`
   - Or use Railway's **CLI**:
     ```bash
     railway run python -m app.db.init_db
     ```

---

## Part 2: Deploy Frontend to Vercel (10 minutes)

### Step 2.1: Create Vercel Account

1. Go to **https://vercel.com**
2. Click **"Sign Up"**
3. Sign up with GitHub (recommended)
4. Authorize Vercel to access your repositories

### Step 2.2: Import Your Project

1. In Vercel dashboard, click **"Add New"** → **"Project"**
2. Find and select your `credence` repository
3. Click **"Import"**

### Step 2.3: Configure Frontend

1. **Framework Preset**: Should auto-detect "Next.js" ✅
2. **Root Directory**: Click "Edit" and set to: `frontend`
   - This tells Vercel to deploy only the frontend folder
3. **Build Command**: Leave as default (`npm run build`)
4. **Output Directory**: Leave as default (`.next`)
5. **Install Command**: Leave as default (`npm install`)

### Step 2.4: Add Environment Variable

1. Scroll down to **"Environment Variables"**
2. Click **"Add"**
3. Add this variable:
   - **Key**: `NEXT_PUBLIC_API_BASE_URL`
   - **Value**: Your Railway backend URL (from Step 1.6)
     - Example: `https://credence-backend-production.up.railway.app`
4. Make sure it's enabled for **Production**, **Preview**, and **Development**

### Step 2.5: Deploy

1. Click **"Deploy"**
2. Vercel will build and deploy your frontend
3. Wait 2-3 minutes for the build to complete
4. Once done, you'll get a URL like: `https://credence.vercel.app`
5. **Copy this URL** - you'll need it for the backend CORS

---

## Part 3: Connect Frontend and Backend (5 minutes)

### Step 3.1: Update Backend CORS

1. Go back to **Railway** dashboard
2. Open your backend service
3. Go to **Variables** tab
4. Find `BACKEND_CORS_ORIGINS`
5. Update it to your Vercel URL:
   ```
   BACKEND_CORS_ORIGINS=https://credence.vercel.app
   ```
   (Replace with your actual Vercel URL)
6. Railway will automatically redeploy

### Step 3.2: Test Your App

1. Visit your Vercel frontend URL: `https://credence.vercel.app`
2. You should see the Credence dashboard
3. Try submitting a claim or URL
4. Check the browser console (F12) for any errors
5. Check Railway logs if there are backend errors

---

## Part 4: Optional - Add MBFC Dataset

If you have an MBFC credibility dataset CSV file:

1. **Option A: Upload to Railway**
   - Go to Railway service → **Settings** → **Volumes**
   - Create a volume and mount it to `/app/data`
   - Upload your `mbfc.csv` file there

2. **Option B: Include in Git** (if file is small)
   - Add `data/mbfc.csv` to your repository
   - Railway will have access to it

3. **Option C: Use a URL** (if hosted elsewhere)
   - Modify the code to download from URL on startup

---

## Part 5: Troubleshooting

### Backend Issues

**Problem**: Backend won't start
- **Solution**: Check Railway logs
  - Go to Railway → Your service → **Deploy Logs**
  - Look for error messages
  - Common issues:
    - Missing environment variables
    - Database connection issues
    - Python dependency errors

**Problem**: Database connection error
- **Solution**: 
  - Verify `DATABASE_URL` is set correctly
  - Check if PostgreSQL service is running in Railway
  - Try re-initializing: `railway run python -m app.db.init_db`

**Problem**: API returns 500 errors
- **Solution**: 
  - Check Railway logs for Python errors
  - Verify all API keys are set correctly
  - Check if OpenAI API key is valid

### Frontend Issues

**Problem**: Frontend can't connect to backend
- **Solution**:
  - Verify `NEXT_PUBLIC_API_BASE_URL` is correct in Vercel
  - Check browser console for CORS errors
  - Ensure backend CORS is set correctly
  - Make sure backend URL is publicly accessible

**Problem**: Build fails on Vercel
- **Solution**:
  - Check Vercel build logs
  - Ensure `frontend` is set as root directory
  - Verify `package.json` is in the frontend folder
  - Check for TypeScript errors

**Problem**: Environment variable not working
- **Solution**:
  - Vercel environment variables must start with `NEXT_PUBLIC_` to be accessible in browser
  - Redeploy after adding environment variables
  - Clear browser cache

### General Issues

**Problem**: Changes not showing up
- **Solution**:
  - Push changes to GitHub
  - Railway/Vercel will auto-deploy
  - Wait for deployment to complete
  - Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)

---

## Part 6: Custom Domain (Optional)

### Vercel Custom Domain

1. Go to Vercel project → **Settings** → **Domains**
2. Add your domain (e.g., `credence.yourdomain.com`)
3. Follow DNS instructions
4. Vercel will provide SSL automatically

### Railway Custom Domain

1. Go to Railway service → **Settings** → **Networking**
2. Add your custom domain
3. Update DNS records as instructed
4. Railway will provide SSL automatically

---

## Part 7: Monitoring & Updates

### View Logs

- **Railway**: Dashboard → Service → **Deploy Logs**
- **Vercel**: Dashboard → Project → **Deployments** → Click deployment → **Logs**

### Update Your App

1. Make changes to your code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update feature"
   git push
   ```
3. Railway and Vercel will automatically redeploy

### Check Status

- **Railway**: Dashboard shows service status
- **Vercel**: Dashboard shows deployment status
- **Health Check**: Visit `https://your-backend.railway.app/api/v1/health`

---

## 🎉 Success Checklist

- [ ] Backend deployed to Railway
- [ ] Backend URL is accessible (health check works)
- [ ] Frontend deployed to Vercel
- [ ] Frontend URL is accessible
- [ ] Environment variables set correctly
- [ ] CORS configured properly
- [ ] Database initialized
- [ ] Can submit a claim/URL/text
- [ ] Results display correctly
- [ ] No console errors

---

## 💰 Cost Estimate

- **Vercel (Frontend)**: **FREE** (Hobby plan)
  - Unlimited deployments
  - 100GB bandwidth/month
  - Perfect for most projects

- **Railway (Backend + Database)**: **$5/month** (Starter plan)
  - Includes PostgreSQL database
  - 512MB RAM
  - $5 credit included (can run small apps for free initially)

**Total: ~$0-5/month** for small to medium traffic

---

## 🆘 Need Help?

If you encounter issues:

1. **Check the logs** (Railway and Vercel dashboards)
2. **Verify environment variables** are set correctly
3. **Test backend directly**: Visit `https://your-backend.railway.app/docs` (FastAPI docs)
4. **Check browser console** for frontend errors
5. **Verify CORS settings** match your frontend URL

---

## Alternative: Deploy Everything to One Platform

If you prefer a simpler setup, you can also deploy both frontend and backend to:

- **Render.com** (free tier available)
- **Fly.io** (pay-as-you-go)
- **DigitalOcean App Platform** (starts at $5/month)

See `DEPLOYMENT.md` for details on these options.

---

**Your app should now be live and accessible to users! 🚀**

