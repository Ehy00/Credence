# ✅ Deployment Checklist

Use this checklist to ensure everything is set up correctly.

---

## Pre-Deployment

- [ ] Code is pushed to GitHub
- [ ] All environment variables are ready (OpenAI API key, etc.)
- [ ] You have accounts on Railway and Vercel (or chosen platforms)

---

## Backend Deployment (Railway)

### Initial Setup
- [ ] Created Railway account
- [ ] Created new project from GitHub repo
- [ ] Set **Root Directory** to `backend`
- [ ] Added PostgreSQL database service

### Environment Variables
- [ ] `DATABASE_URL` (auto-set by Railway) ✅
- [ ] `OPENAI_API_KEY` = `sk-...`
- [ ] `GDELT_API_KEY` = (optional, can be empty)
- [ ] `GOOGLE_FACTCHECK_API_KEY` = (optional, can be empty)
- [ ] `MBFC_DATA_PATH` = `./data/mbfc.csv`
- [ ] `BACKEND_CORS_ORIGINS` = `*` (temporary, update after frontend deploy)

### Database
- [ ] Database service is running
- [ ] Database initialized (run `python -m app.db.init_db` via Railway CLI or add as startup command)

### Testing
- [ ] Backend URL is accessible
- [ ] Health check works: `https://your-backend.railway.app/api/v1/health`
- [ ] API docs accessible: `https://your-backend.railway.app/docs`
- [ ] No errors in Railway logs

---

## Frontend Deployment (Vercel)

### Initial Setup
- [ ] Created Vercel account
- [ ] Imported GitHub repository
- [ ] Set **Root Directory** to `frontend`
- [ ] Framework preset is Next.js

### Environment Variables
- [ ] `NEXT_PUBLIC_API_BASE_URL` = Your Railway backend URL

### Testing
- [ ] Frontend URL is accessible
- [ ] Build completed successfully
- [ ] No build errors in Vercel logs

---

## Connection & Configuration

### CORS Setup
- [ ] Updated `BACKEND_CORS_ORIGINS` in Railway to your Vercel URL
- [ ] Railway redeployed after CORS update

### Integration Testing
- [ ] Frontend loads without errors
- [ ] Can submit a claim
- [ ] Can submit a URL
- [ ] Can paste article text
- [ ] Results display correctly
- [ ] No CORS errors in browser console
- [ ] No 404/500 errors

---

## Post-Deployment

### Optional Enhancements
- [ ] Added custom domain (Vercel)
- [ ] Added custom domain (Railway)
- [ ] Set up monitoring/alerts
- [ ] Configured database backups
- [ ] Added MBFC dataset (if available)
- [ ] Set up error tracking (Sentry, etc.)

### Documentation
- [ ] Updated README with production URLs
- [ ] Documented any custom configurations
- [ ] Shared deployment guide with team

---

## Troubleshooting Checklist

If something isn't working:

### Backend Issues
- [ ] Check Railway logs for errors
- [ ] Verify all environment variables are set
- [ ] Test backend directly: `/api/v1/health` and `/docs`
- [ ] Verify database connection
- [ ] Check if database was initialized
- [ ] Verify OpenAI API key is valid

### Frontend Issues
- [ ] Check Vercel build logs
- [ ] Verify `NEXT_PUBLIC_API_BASE_URL` is correct
- [ ] Check browser console for errors
- [ ] Verify CORS settings match frontend URL
- [ ] Hard refresh browser (Ctrl+Shift+R)
- [ ] Check network tab for API calls

### Integration Issues
- [ ] Verify backend URL is publicly accessible
- [ ] Check CORS headers in network requests
- [ ] Verify environment variables are set for production
- [ ] Check both Railway and Vercel logs
- [ ] Test API endpoint directly with curl/Postman

---

## Quick Test Commands

### Test Backend
```bash
# Health check
curl https://your-backend.railway.app/api/v1/health

# API docs
open https://your-backend.railway.app/docs
```

### Test Frontend
```bash
# Open in browser
open https://your-app.vercel.app
```

### Test Integration
1. Open frontend in browser
2. Open browser DevTools (F12)
3. Go to Network tab
4. Submit a claim
5. Check if API calls succeed (status 200)

---

## Success Criteria

Your deployment is successful when:
- ✅ Backend health check returns `{"status": "ok"}`
- ✅ Frontend loads without errors
- ✅ Can submit all three input types (claim/URL/text)
- ✅ Results display correctly
- ✅ No console errors
- ✅ No CORS errors
- ✅ API calls return 200 status

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Backend won't start | Check Railway logs, verify env vars |
| Database connection error | Verify DATABASE_URL, check PostgreSQL is running |
| Frontend build fails | Check Vercel logs, verify root directory is `frontend` |
| CORS errors | Update BACKEND_CORS_ORIGINS with exact frontend URL |
| API returns 500 | Check Railway logs, verify OpenAI API key |
| Environment variable not working | Redeploy after adding env vars, verify naming |

---

**Once all items are checked, your app is fully deployed! 🎉**

