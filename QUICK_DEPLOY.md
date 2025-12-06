# Quick Deploy Guide

## 🚀 Fastest Way: Vercel + Railway (Recommended)

### Step 1: Deploy Backend (Railway) - 5 minutes

1. **Go to [Railway.app](https://railway.app)** and sign up/login
2. **Click "New Project"** → **"Deploy from GitHub repo"**
3. **Select your repository** and choose the `backend` folder as root
4. **Add Environment Variables:**
   ```
   DATABASE_URL=postgresql://... (Railway auto-generates this)
   OPENAI_API_KEY=sk-your-key-here
   GDELT_API_KEY=your-key (optional)
   GOOGLE_FACTCHECK_API_KEY=your-key (optional)
   BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app
   MBFC_DATA_PATH=./data/mbfc.csv
   ```
5. **Click Deploy** - Railway will build and deploy automatically
6. **Copy your backend URL** (e.g., `https://credence-backend.railway.app`)

### Step 2: Deploy Frontend (Vercel) - 3 minutes

1. **Go to [Vercel.com](https://vercel.com)** and sign up/login
2. **Click "Add New"** → **"Project"**
3. **Import your GitHub repository**
4. **Configure:**
   - Framework Preset: **Next.js**
   - Root Directory: `frontend`
   - Environment Variable: `NEXT_PUBLIC_API_BASE_URL` = your Railway backend URL
5. **Click Deploy** - Vercel will build and deploy automatically
6. **Your app is live!** 🎉

### Step 3: Update CORS (1 minute)

1. Go back to Railway dashboard
2. Update `BACKEND_CORS_ORIGINS` to your Vercel URL: `https://your-app.vercel.app`
3. Railway will automatically redeploy

## 🐳 Alternative: Docker on VPS

If you prefer your own server (DigitalOcean, AWS EC2, etc.):

```bash
# 1. Clone repository
git clone <your-repo>
cd Credence

# 2. Create .env file
cat > .env << EOF
DATABASE_URL=postgresql://credence:password@db:5432/credence
OPENAI_API_KEY=sk-your-key
GDELT_API_KEY=your-key
GOOGLE_FACTCHECK_API_KEY=your-key
BACKEND_CORS_ORIGINS=https://your-domain.com
POSTGRES_USER=credence
POSTGRES_PASSWORD=your-secure-password
POSTGRES_DB=credence
EOF

# 3. Deploy
docker-compose -f docker-compose.prod.yml up -d

# 4. Set up domain (optional)
# Use Nginx + Let's Encrypt (see DEPLOYMENT.md)
```

## 📋 Environment Variables Checklist

### Backend (Railway/Render/Fly.io)
- [ ] `DATABASE_URL` (auto-set by platform or PostgreSQL connection string)
- [ ] `OPENAI_API_KEY` (required)
- [ ] `GDELT_API_KEY` (optional)
- [ ] `GOOGLE_FACTCHECK_API_KEY` (optional)
- [ ] `BACKEND_CORS_ORIGINS` (your frontend URL)
- [ ] `MBFC_DATA_PATH` (default: `./data/mbfc.csv`)

### Frontend (Vercel)
- [ ] `NEXT_PUBLIC_API_BASE_URL` (your backend URL)

## 🔗 After Deployment

1. **Test your backend:** Visit `https://your-backend.railway.app/api/v1/health`
2. **Test your frontend:** Visit `https://your-app.vercel.app`
3. **Check API docs:** Visit `https://your-backend.railway.app/docs`

## 💰 Cost Estimate

- **Vercel (Frontend):** FREE (hobby plan)
- **Railway (Backend + DB):** $5/month (starter plan)
- **Total:** ~$5/month for small apps

## 🆘 Troubleshooting

**Backend won't start?**
- Check all environment variables are set
- Check logs in Railway dashboard
- Verify database connection string

**Frontend can't connect?**
- Verify `NEXT_PUBLIC_API_BASE_URL` is correct
- Check CORS settings in backend
- Ensure backend URL is publicly accessible

**Need help?** See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions.




