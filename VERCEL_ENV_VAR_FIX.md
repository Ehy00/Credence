# 🔧 Fix Vercel Environment Variable Error

## ❌ The Error

```
Environment Variable "NEXT_PUBLIC_API_BASE_URL" references Secret "api_base_url", which does not exist.
```

## 🔍 What Happened

Vercel is trying to reference a secret instead of using a plain value. This happens if:
- You used `@api_base_url` syntax (Vercel secret reference)
- Or there's a `vercel.json` file with secret references

## ✅ The Fix

### Step 1: Add Environment Variable Correctly

In Vercel project settings:

1. Go to **Settings** → **Environment Variables**
2. Click **"Add New"**
3. **Key:** `NEXT_PUBLIC_API_BASE_URL`
4. **Value:** `https://credence-production-6240.up.railway.app`
   - ⚠️ **Important:** Type the URL directly, don't use `@` or secret syntax
   - Just paste: `https://credence-production-6240.up.railway.app`
5. Select environments: **Production**, **Preview**, **Development**
6. Click **"Save"**

### Step 2: Check vercel.json (if it exists)

If you have a `vercel.json` file, make sure it doesn't reference secrets:

**❌ Wrong (references secret):**
```json
{
  "env": {
    "NEXT_PUBLIC_API_BASE_URL": "@api_base_url"
  }
}
```

**✅ Correct (or remove env section):**
```json
{
  "buildCommand": "npm run build",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs"
}
```

Or just delete the `env` section from `vercel.json` - you'll set it in Vercel UI instead.

---

## 📋 Correct Vercel Configuration

### Environment Variables (in Vercel UI):
- **Key:** `NEXT_PUBLIC_API_BASE_URL`
- **Value:** `https://credence-production-6240.up.railway.app` (plain text, no `@`)

### vercel.json (optional, can be minimal):
```json
{
  "framework": "nextjs"
}
```

Or just delete `vercel.json` - Vercel will auto-detect Next.js.

---

## 🎯 Quick Fix Steps

1. **In Vercel UI:**
   - Settings → Environment Variables
   - Add: `NEXT_PUBLIC_API_BASE_URL` = `https://credence-production-6240.up.railway.app`
   - Make sure value is plain text (no `@` symbol)

2. **If vercel.json has secret reference:**
   - Remove the `env` section
   - Or update to not use `@` syntax

3. **Redeploy:**
   - Vercel will pick up the new environment variable

---

**The key is: Use plain URL value, not a secret reference! 🚀**

