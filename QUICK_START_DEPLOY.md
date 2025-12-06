# ⚡ Quick Start: Deploy in 20 Minutes

Follow these steps to get your app live **right now**.

---

## 🎯 The Simplest Path: Railway + Vercel

### Prerequisites
- GitHub account
- OpenAI API key (get from https://platform.openai.com/api-keys)

---

## Step 1: Push to GitHub (2 minutes)

```bash
cd /Users/oladebs/Downloads/Credence-main

# Initialize git if not already done
git init
git add .
git commit -m "Ready to deploy"

# Create repo on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/credence.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy Backend to Railway (8 minutes)

1. **Go to https://railway.app** → Sign up with GitHub

2. **New Project** → **Deploy from GitHub repo** → Select your repo

3. **IMPORTANT**: Click the service → **Settings** → **Root Directory** → Set to: `backend`

4. **Add PostgreSQL**: Click **"+ New"** → **Database** → **Add PostgreSQL**

5. **Add Environment Variables** (Variables tab):
   ```
   OPENAI_API_KEY=sk-your-key-here
   BACKEND_CORS_ORIGINS=*
   MBFC_DATA_PATH=./data/mbfc.csv
   ```
   (DATABASE_URL is auto-set by Railway)

6. **Wait for deployment** (2-3 minutes)

7. **Copy your backend URL** (looks like: `https://credence-production.up.railway.app`)

8. **Test it**: Visit `https://your-backend-url.railway.app/api/v1/health`
   - Should show: `{"status": "ok"}`

---

## Step 3: Deploy Frontend to Vercel (5 minutes)

1. **Go to https://vercel.com** → Sign up with GitHub

2. **Add New** → **Project** → Import your repo

3. **Configure**:
   - **Root Directory**: `frontend` (click "Edit" to change)
   - **Framework Preset**: Next.js (auto-detected)

4. **Environment Variable**:
   - Key: `NEXT_PUBLIC_API_BASE_URL`
   - Value: Your Railway backend URL (from Step 2.7)

5. **Deploy** → Wait 2 minutes

6. **Copy your Vercel URL** (looks like: `https://credence.vercel.app`)

---

## Step 4: Connect Them (2 minutes)

1. **Go back to Railway** → Your service → **Variables**

2. **Update** `BACKEND_CORS_ORIGINS`:
   ```
   BACKEND_CORS_ORIGINS=https://credence.vercel.app
   ```
   (Use your actual Vercel URL)

3. Railway will auto-redeploy (wait 1 minute)

---

## Step 5: Test Your App (3 minutes)

1. **Visit your Vercel URL**: `https://credence.vercel.app`

2. **Try it out**:
   - Enter a claim like: "The sky is blue"
   - Or paste an article URL
   - Submit and see results!

3. **If it works**: 🎉 **You're live!**

4. **If there are errors**:
   - Check browser console (F12)
   - Check Railway logs
   - See troubleshooting below

---

## 🔧 Quick Troubleshooting

### Backend not working?
- Check Railway logs: Dashboard → Service → Deploy Logs
- Verify `OPENAI_API_KEY` is set correctly
- Test backend directly: `https://your-backend.railway.app/docs`

### Frontend can't connect?
- Verify `NEXT_PUBLIC_API_BASE_URL` in Vercel matches your Railway URL
- Check CORS: Make sure `BACKEND_CORS_ORIGINS` in Railway includes your Vercel URL
- Hard refresh browser (Ctrl+Shift+R)

### Database errors?
- Railway auto-creates PostgreSQL, but you may need to initialize:
  - Railway → Service → **Deploy** → Add command: `python -m app.db.init_db`
  - Or use Railway CLI: `railway run python -m app.db.init_db`

---

## ✅ You're Done!

Your app is now:
- ✅ Live on the internet
- ✅ Accessible to users
- ✅ Fully functional
- ✅ Auto-deploys on git push

**Cost**: ~$0-5/month (Vercel free, Railway $5/month)

---

## 📝 Next Steps (Optional)

1. **Add custom domain** (Vercel → Settings → Domains)
2. **Set up monitoring** (Railway and Vercel dashboards)
3. **Add MBFC dataset** (upload to Railway volumes)
4. **Configure backups** (Railway → Database → Backups)

---

## 🆘 Still Stuck?

See the detailed guide: `DEPLOY_STEP_BY_STEP.md`

Or check:
- Railway docs: https://docs.railway.app
- Vercel docs: https://vercel.com/docs

