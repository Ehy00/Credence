# 🔧 Railway Root Directory Fix

Railway is trying to build from the root directory instead of `backend`. Here are **3 ways to fix this**:

---

## ✅ Solution 1: Set Root Directory in Railway UI (Easiest)

**The UI option exists, but it's in a specific place:**

1. **After Railway creates the service** (even if it fails):
   - Click on your **service** (the failed one)
   - Go to **Settings** tab (gear icon)
   - Scroll down to **"Root Directory"**
   - Enter: `backend`
   - Click **Save**

2. **Redeploy**:
   - Go to **Deployments** tab
   - Click **"Redeploy"** or push a new commit

**If you can't find "Root Directory" in Settings:**
- Make sure you're clicking on the **service** (not the project)
- It's in the **Settings** tab, not Variables
- Sometimes it's labeled as **"Working Directory"**

---

## ✅ Solution 2: Use Railway Configuration File (I've Created This!)

I've created `railway.toml` at the root of your project. This tells Railway to:
- Build from the `backend` directory
- Use the correct commands

**What to do:**
1. The file is already created ✅
2. Push to GitHub:
   ```bash
   git add railway.toml nixpacks.toml
   git commit -m "Add Railway configuration"
   git push
   ```
3. In Railway:
   - Delete the current service (if it exists)
   - Create a new service from GitHub
   - Railway should now detect the configuration

---

## ✅ Solution 3: Create Service Manually with CLI

Use Railway CLI to set root directory:

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link to your project
railway link

# Set root directory
railway variables set RAILWAY_ROOT_DIRECTORY=backend

# Or use the service command
railway service create --name credence-backend --root backend
```

---

## 🎯 Recommended: Solution 1 (UI Method)

**Step-by-step with screenshots description:**

1. **Go to Railway dashboard**
2. **Click on your project**
3. **Click on the service** (the one that failed)
4. **Click "Settings"** (gear icon on the right)
5. **Scroll down** to find **"Root Directory"** or **"Working Directory"**
6. **Enter**: `backend`
7. **Click "Save"**
8. **Go to "Deployments"** tab
9. **Click "Redeploy"** (or push a new commit)

---

## 🔍 If Root Directory Option is Missing

**Try this:**

1. **Delete the current service**:
   - Settings → Danger Zone → Delete Service

2. **Create new service**:
   - Click "+ New" in your project
   - Select "GitHub Repo"
   - Select your repository
   - **Before clicking Deploy**, look for "Root Directory" option
   - Set it to `backend`
   - Then deploy

3. **Or use Railway's new UI**:
   - Some Railway interfaces show root directory during initial setup
   - Look for "Advanced" or "Configure" options

---

## 🛠️ Alternative: Use Nixpacks Configuration

I've also created `nixpacks.toml` which Railway's buildpack will detect automatically.

**What it does:**
- Tells Railway to use Python
- Sets build commands to work from backend directory
- Configures start command

**To use:**
1. Files are already created ✅
2. Push to GitHub
3. Railway should auto-detect and use it

---

## 📋 Quick Fix Checklist

- [ ] Try Solution 1: Find Root Directory in Settings
- [ ] If not found, try Solution 2: Use railway.toml (already created)
- [ ] Push railway.toml and nixpacks.toml to GitHub
- [ ] Delete and recreate service if needed
- [ ] Verify build logs show it's using backend directory

---

## 🆘 Still Not Working?

**Option A: Create a separate backend repository**
1. Create a new GitHub repo just for backend
2. Copy only the `backend/` folder contents
3. Deploy that to Railway (no root directory needed)

**Option B: Use Render instead**
- Render has a clearer "Root Directory" option
- See `DEPLOYMENT.md` for Render instructions

**Option C: Use Railway CLI**
```bash
railway service create --root backend
```

---

## ✅ Verification

After fixing, check the build logs. You should see:
- ✅ Building from `backend/` directory
- ✅ Python detected
- ✅ `pip install` running
- ✅ No "could not determine how to build" error

---

**Try Solution 1 first** - the Root Directory option is there, just need to find it in Settings! 🚀

