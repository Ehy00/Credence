# 🚂 Railway Deployment - Step by Step Fix

Your Railway error shows it's trying to build from the root. Here's exactly how to fix it.

---

## 🔍 Understanding the Error

**What Railway said:**
```
Railpack could not determine how to build the app.
The app contents that Railpack analyzed contains:
./backend/
./frontend/
```

**Problem**: Railway is looking at the **root directory** and sees both `backend/` and `frontend/`, so it doesn't know which one to build.

**Solution**: Tell Railway to use `backend/` as the root directory.

---

## ✅ Solution: Set Root Directory (3 Steps)

### Step 1: Navigate to Settings

1. Go to **https://railway.app**
2. Click on your **Project** (the container with your repo name)
3. Click on the **Service** (the box inside the project - it might show "Deploying" or have an error)
4. Click the **"Settings"** tab (top right, looks like a gear ⚙️)

### Step 2: Find Root Directory

1. In Settings, scroll down past:
   - Service Name
   - Healthcheck Path
   - Restart Policy
   - **You'll see "Root Directory"** (or "Working Directory")

2. **Root Directory field**:
   - Currently shows: `/` or empty
   - **Change it to**: `backend`
   - (Just type `backend`, no slash)

### Step 3: Save and Redeploy

1. Click **"Save"** (bottom of Settings page)
2. Go to **"Deployments"** tab
3. Click **"Redeploy"** (or push a new commit to trigger auto-deploy)

---

## 🎯 Visual Guide

```
Railway Dashboard
│
├── Your Project (click this)
│   │
│   └── Your Service (click this - the failed one)
│       │
│       ├── Deployments tab
│       ├── Metrics tab
│       ├── Variables tab
│       └── Settings tab ← CLICK HERE
│           │
│           └── Scroll down to find:
│               │
│               └── Root Directory: [backend] ← TYPE THIS
│
└── Click "Save" → Go to Deployments → Redeploy
```

---

## 🔄 Alternative: Delete and Recreate

**If you can't find Root Directory in Settings:**

1. **Delete current service:**
   - Settings → Scroll to very bottom
   - **"Danger Zone"** section
   - Click **"Delete Service"**

2. **Create new service:**
   - In your project, click **"+ New"**
   - Select **"GitHub Repo"**
   - Select your repository
   - **Before clicking "Deploy"**, look for:
     - "Root Directory" field, OR
     - "Advanced" or "Configure" button
   - Set Root Directory to: `backend`
   - Click **"Deploy"**

---

## 🛠️ Method 3: Use Configuration Files

I've created configuration files that Railway can auto-detect:

**Files created:**
- ✅ `railway.toml` (at root)
- ✅ `nixpacks.toml` (at root)

**To use:**

1. **Push to GitHub:**
   ```bash
   cd /Users/oladebs/Downloads/Credence-main
   git add railway.toml nixpacks.toml
   git commit -m "Add Railway configuration for root directory"
   git push
   ```

2. **In Railway:**
   - Delete current service
   - Create new service from GitHub
   - Railway should auto-detect the config and use `backend` directory

---

## 🧪 Verify It Worked

**After setting root directory and redeploying, check logs:**

✅ **Good signs:**
- Logs show: `Building from backend/`
- Python detected
- `pip install` runs successfully
- No "could not determine how to build" error

❌ **If still fails:**
- Check that `backend/pyproject.toml` exists
- Check that `backend/requirements.txt` exists
- Verify `backend/app/main.py` exists

---

## 🆘 Still Having Issues?

### Option A: Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link to your project
railway link

# Set root directory via CLI
railway variables set RAILWAY_ROOT_DIRECTORY=backend

# Or update service
railway service update --root backend
```

### Option B: Separate Backend Repo

1. Create new GitHub repo: `credence-backend`
2. Copy only contents of `backend/` folder (not the folder itself)
3. Deploy that repo to Railway (no root directory needed)

### Option C: Use Render

Render has a clearer root directory option:
- See `DEPLOYMENT.md` for Render instructions
- Root directory is clearly visible during setup

---

## 📋 Quick Checklist

- [ ] Found Settings tab in Railway service
- [ ] Found Root Directory field
- [ ] Set to `backend` (not `/backend` or `./backend`)
- [ ] Saved changes
- [ ] Redeployed
- [ ] Build logs show success
- [ ] Backend URL is accessible

---

## 💡 Pro Tip

**After setting root directory:**
- Railway will remember this setting
- Future deployments will use `backend/` automatically
- You can verify in Settings anytime

---

**The Root Directory option IS there - it's in Settings! Follow the steps above and you'll find it! 🚀**

If you still can't find it, try the Railway CLI method or create a separate backend repository.

