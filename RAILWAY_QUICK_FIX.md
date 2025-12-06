# ⚡ Railway Root Directory - Quick Fix

Railway can't find the root directory. Here's the **fastest way to fix it**:

---

## 🎯 Method 1: Find Root Directory in Settings (2 minutes)

**The option IS there, here's exactly where:**

1. **In Railway dashboard:**
   - Click on your **Project** (the container)
   - Click on the **Service** (the failed deployment)
   - Look for **"Settings"** tab (gear icon ⚙️)
   - Scroll down - you'll see **"Root Directory"** field
   - Enter: `backend`
   - Click **"Save"**

2. **Redeploy:**
   - Go to **"Deployments"** tab
   - Click **"Redeploy"** button

**That's it!** Railway will now build from the `backend` directory.

---

## 🎯 Method 2: Delete & Recreate (If Method 1 doesn't work)

1. **Delete the current service:**
   - Settings → Scroll to bottom → **"Delete Service"**

2. **Create new service:**
   - Click **"+ New"** in your project
   - Select **"GitHub Repo"**
   - Select your repository
   - **Look for "Root Directory" or "Working Directory"** in the setup form
   - Set to: `backend`
   - Click **"Deploy"**

---

## 🎯 Method 3: Use Configuration Files (Already Created!)

I've created `railway.toml` and `nixpacks.toml` at the root. Push them:

```bash
cd /Users/oladebs/Downloads/Credence-main
git add railway.toml nixpacks.toml
git commit -m "Add Railway root directory configuration"
git push
```

Then in Railway:
- Delete current service
- Create new service from GitHub
- Railway should auto-detect the config

---

## 🔍 Where is Root Directory in Railway UI?

**Step-by-step navigation:**

1. **Railway Dashboard** → Your Project
2. **Click on the Service** (the box that shows your repo name)
3. **Click "Settings" tab** (top right, gear icon)
4. **Scroll down** past Variables section
5. **You'll see "Root Directory"** field (might be empty or show `/`)
6. **Type**: `backend`
7. **Click "Save"** (bottom of page)

**Visual guide:**
```
Railway Dashboard
  └── Your Project
      └── Your Service (click this)
          └── Settings Tab (gear icon)
              └── Scroll down
                  └── Root Directory: [backend] ← Enter here
```

---

## ✅ After Setting Root Directory

**Verify it worked:**

1. **Check build logs:**
   - Should show: `Building from backend/`
   - Should detect Python
   - Should run: `pip install -e .`

2. **If still fails:**
   - Check that `backend/pyproject.toml` exists
   - Check that `backend/requirements.txt` exists
   - Verify Python files are in `backend/app/`

---

## 🆘 Still Can't Find Root Directory?

**Try these:**

1. **Use Railway CLI:**
   ```bash
   npm install -g @railway/cli
   railway login
   railway link
   railway service update --root backend
   ```

2. **Create separate backend repo:**
   - Create new GitHub repo: `credence-backend`
   - Copy only `backend/` folder contents
   - Deploy that repo (no root directory needed)

3. **Use Render instead:**
   - Render has clearer root directory option
   - See `DEPLOYMENT.md` for instructions

---

## 📋 Quick Checklist

- [ ] Found Settings tab in Railway service
- [ ] Found Root Directory field
- [ ] Set to `backend`
- [ ] Saved changes
- [ ] Redeployed
- [ ] Build logs show it's using backend directory

---

**The Root Directory option IS in Railway - it's just in Settings! Try Method 1 first! 🚀**

