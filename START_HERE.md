# 🚀 START HERE: Deploy Your Credence App

**Your GitHub Actions deployment didn't work?** No problem! Follow these simple steps to deploy manually.

---

## ⚡ Quickest Path (20 minutes)

**Read this first**: `QUICK_START_DEPLOY.md` - Step-by-step guide to get live in 20 minutes.

---

## 📚 Full Documentation

1. **`QUICK_START_DEPLOY.md`** - Fastest way to deploy (Railway + Vercel)
2. **`DEPLOY_STEP_BY_STEP.md`** - Detailed step-by-step guide with troubleshooting
3. **`DEPLOYMENT_CHECKLIST.md`** - Checklist to ensure everything works
4. **`DEPLOYMENT.md`** - Complete deployment options (all platforms)

---

## 🎯 Recommended Approach

### Why Railway + Vercel?

- ✅ **Easiest to set up** (no complex config)
- ✅ **Free tier available** (Vercel free, Railway $5/month)
- ✅ **Auto-deploys** from GitHub
- ✅ **Built-in databases** (Railway provides PostgreSQL)
- ✅ **SSL/HTTPS included** (automatic)
- ✅ **Great documentation** and support

### What You'll Do

1. **Push code to GitHub** (2 min)
2. **Deploy backend to Railway** (8 min)
3. **Deploy frontend to Vercel** (5 min)
4. **Connect them together** (2 min)
5. **Test and verify** (3 min)

**Total time: ~20 minutes**

---

## 🔑 What You Need

Before starting:
- [ ] GitHub account
- [ ] OpenAI API key (get from https://platform.openai.com/api-keys)
- [ ] (Optional) GDELT API key
- [ ] (Optional) Google Fact Check API key

---

## 📋 Step-by-Step Summary

### 1. Push to GitHub
```bash
cd /Users/oladebs/Downloads/Credence-main
git init
git add .
git commit -m "Ready to deploy"
git remote add origin https://github.com/YOUR_USERNAME/credence.git
git push -u origin main
```

### 2. Deploy Backend (Railway)
- Go to https://railway.app
- New Project → Deploy from GitHub
- **Set Root Directory to `backend`** ⚠️ IMPORTANT
- Add PostgreSQL database
- Add environment variables (see QUICK_START_DEPLOY.md)
- Copy backend URL

### 3. Deploy Frontend (Vercel)
- Go to https://vercel.com
- Add New → Project
- **Set Root Directory to `frontend`** ⚠️ IMPORTANT
- Add environment variable: `NEXT_PUBLIC_API_BASE_URL` = your Railway URL
- Copy frontend URL

### 4. Connect Them
- Update `BACKEND_CORS_ORIGINS` in Railway to your Vercel URL
- Test your app!

---

## ⚠️ Common Mistakes to Avoid

1. **Wrong root directory** - Must be `backend` for Railway, `frontend` for Vercel
2. **Missing environment variables** - Check the checklist
3. **CORS not configured** - Must match your frontend URL exactly
4. **Database not initialized** - Run `python -m app.db.init_db` via Railway CLI
5. **Using wrong database URL** - Railway auto-sets `DATABASE_URL`, don't override it

---

## 🆘 Need Help?

### Backend Issues
- Check Railway logs: Dashboard → Service → Deploy Logs
- Test backend: `https://your-backend.railway.app/api/v1/health`
- View API docs: `https://your-backend.railway.app/docs`

### Frontend Issues
- Check Vercel build logs
- Check browser console (F12)
- Verify environment variables are set

### Integration Issues
- Check CORS settings match frontend URL
- Verify `NEXT_PUBLIC_API_BASE_URL` is correct
- Test API directly with curl/Postman

---

## 📖 Next Steps After Deployment

1. **Test all features**:
   - Submit a claim
   - Submit a URL
   - Paste article text
   - Verify results display

2. **Optional enhancements**:
   - Add custom domain
   - Set up monitoring
   - Configure backups
   - Add MBFC dataset

3. **Share your app**:
   - Your app is now live!
   - Share the Vercel URL with users

---

## 💰 Cost

- **Vercel (Frontend)**: FREE (hobby plan)
- **Railway (Backend + DB)**: $5/month (starter plan)
- **Total**: ~$5/month for small apps

---

## ✅ Success Checklist

After deployment, verify:
- [ ] Backend health check works
- [ ] Frontend loads without errors
- [ ] Can submit all input types
- [ ] Results display correctly
- [ ] No console errors
- [ ] No CORS errors

---

## 🎉 You're Ready!

**Start with**: `QUICK_START_DEPLOY.md`

This will get you live in 20 minutes. If you run into issues, check `DEPLOY_STEP_BY_STEP.md` for detailed troubleshooting.

**Good luck! 🚀**

