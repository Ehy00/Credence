# ✅ Backend is Live! Next Steps

Your Railway backend is successfully deployed! 🎉

## ✅ What's Working

- ✅ Backend deployed to Railway
- ✅ Public domain generated
- ✅ Port 8000 configured correctly
- ✅ API responding: `{"message":"Credence Lite API is running"}`

## 🧪 Test Your Backend

Try these endpoints to verify everything works:

1. **Health Check:**
   ```
   https://your-service.railway.app/api/v1/health
   ```
   Should return: `{"status": "ok"}`

2. **API Documentation:**
   ```
   https://your-service.railway.app/docs
   ```
   Should show FastAPI interactive docs

3. **Root endpoint:**
   ```
   https://your-service.railway.app/
   ```
   Should return: `{"message":"Credence Lite API is running"}`

## 📋 Next Steps: Deploy Frontend

### Step 1: Deploy Frontend to Vercel

1. Go to **https://vercel.com**
2. **Add New** → **Project**
3. Import your GitHub repository
4. **Configure:**
   - **Root Directory**: `frontend` ⚠️ IMPORTANT
   - **Framework Preset**: Next.js (auto-detected)
5. **Environment Variable:**
   - **Key**: `NEXT_PUBLIC_API_BASE_URL`
   - **Value**: Your Railway backend URL
     - Example: `https://your-service.railway.app`
6. **Deploy**

### Step 2: Update CORS in Railway

1. Go back to **Railway dashboard**
2. Your backend service → **Variables** tab
3. Find or add `BACKEND_CORS_ORIGINS`
4. Set it to your Vercel frontend URL:
   ```
   BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app
   ```
5. Railway will auto-redeploy

### Step 3: Initialize Database

You need to initialize the database:

**Option A: Using Railway CLI**
```bash
npm install -g @railway/cli
railway login
railway link  # Link to your backend project
cd backend
railway run python -m app.db.init_db
```

**Option B: Add as Deploy Command (Temporary)**
1. Railway → Settings → Deploy
2. Add one-time command: `python -m app.db.init_db`
3. Redeploy

### Step 4: Add Environment Variables

Make sure these are set in Railway:

- ✅ `DATABASE_URL` (auto-set by Railway if you added PostgreSQL)
- ✅ `OPENAI_API_KEY` (your OpenAI key)
- ✅ `BACKEND_CORS_ORIGINS` (your Vercel frontend URL)
- ⚠️ `GDELT_API_KEY` (optional)
- ⚠️ `GOOGLE_FACTCHECK_API_KEY` (optional)
- ⚠️ `MBFC_DATA_PATH` (optional, default: `./data/mbfc.csv`)

## 🎯 Test Your Full Stack

Once frontend is deployed:

1. Visit your Vercel frontend URL
2. Try submitting a claim
3. Check browser console (F12) for errors
4. Verify API calls are working

## 🆘 Troubleshooting

**Backend not responding?**
- Check Railway logs
- Verify port 8000 is correct
- Check environment variables

**Frontend can't connect?**
- Verify `NEXT_PUBLIC_API_BASE_URL` is set correctly
- Check CORS settings in Railway
- Ensure backend URL is publicly accessible

**Database errors?**
- Initialize database (see Step 3 above)
- Verify `DATABASE_URL` is set
- Check PostgreSQL service is running in Railway

---

**Your backend is live! Now deploy the frontend and connect them! 🚀**

