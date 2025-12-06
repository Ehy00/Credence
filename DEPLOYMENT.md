# Deployment Guide

This guide covers deploying Credence to various cloud platforms.

## Quick Deploy Options

### Option 1: Vercel (Frontend) + Railway (Backend) - Recommended

**Frontend (Vercel):**
1. Push code to GitHub
2. Go to [Vercel](https://vercel.com) and import your repository
3. Set environment variable: `NEXT_PUBLIC_API_BASE_URL` = your backend URL
4. Deploy

**Backend (Railway):**
1. Go to [Railway](https://railway.app) and create new project
2. Connect GitHub repository
3. Select `backend` folder as root
4. Add environment variables:
   - `DATABASE_URL` (Railway provides PostgreSQL)
   - `OPENAI_API_KEY`
   - `GDELT_API_KEY`
   - `GOOGLE_FACTCHECK_API_KEY`
   - `BACKEND_CORS_ORIGINS` = your Vercel frontend URL
5. Deploy

### Option 2: Vercel (Frontend) + Render (Backend)

**Frontend:** Same as Option 1

**Backend (Render):**
1. Go to [Render](https://render.com) and create new Web Service
2. Connect GitHub repository
3. Set root directory to `backend`
4. Build command: `pip install -e .`
5. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables (same as Railway)
7. Deploy

### Option 3: Fly.io (Full Stack)

**Deploy Backend:**
```bash
cd backend
fly launch
# Follow prompts, then:
fly secrets set OPENAI_API_KEY=your-key
fly secrets set GDELT_API_KEY=your-key
fly secrets set GOOGLE_FACTCHECK_API_KEY=your-key
fly deploy
```

**Deploy Frontend:**
```bash
cd frontend
fly launch
# Set environment variable:
fly secrets set NEXT_PUBLIC_API_BASE_URL=https://your-backend.fly.dev
fly deploy
```

### Option 4: Docker Compose (VPS/Cloud Server)

**On your VPS (DigitalOcean, AWS EC2, etc.):**

1. **Install Docker & Docker Compose:**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo apt-get install docker-compose-plugin
```

2. **Clone repository:**
```bash
git clone <your-repo-url>
cd Credence
```

3. **Create `.env` file:**
```bash
cp .env.example .env
# Edit .env with your production values
```

4. **Deploy:**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

5. **Set up reverse proxy (Nginx):**
```nginx
# /etc/nginx/sites-available/credence
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

6. **Enable SSL with Let's Encrypt:**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Environment Variables for Production

### Backend
```bash
DATABASE_URL=postgresql://user:pass@host:5432/dbname
OPENAI_API_KEY=sk-...
GDELT_API_KEY=your-key
GOOGLE_FACTCHECK_API_KEY=your-key
MBFC_DATA_PATH=./data/mbfc.csv
BACKEND_CORS_ORIGINS=https://your-frontend-domain.com
```

### Frontend
```bash
NEXT_PUBLIC_API_BASE_URL=https://your-backend-domain.com
```

## Database Setup

### PostgreSQL (Production)

Most cloud platforms provide managed PostgreSQL. For manual setup:

```bash
# Create database
createdb credence

# Run migrations (if using Alembic)
alembic upgrade head

# Or initialize directly
python -m app.db.init_db
```

### SQLite (Development Only)

SQLite works for development but use PostgreSQL for production.

## File Storage

For MBFC dataset:
- Upload `mbfc.csv` to your server/data directory
- Or use object storage (S3, Cloudflare R2) and download on startup
- Or include in Docker image (not recommended for large files)

## Monitoring & Logs

### Railway
- Logs available in dashboard
- Set up alerts for errors

### Render
- Logs in dashboard
- Can set up webhooks for monitoring

### Fly.io
```bash
fly logs
fly status
```

### Docker
```bash
docker-compose -f docker-compose.prod.yml logs -f
```

## Scaling

### Backend
- Railway/Render: Auto-scaling based on traffic
- Fly.io: Set `min_machines_running` in `fly.toml`
- Docker: Use Docker Swarm or Kubernetes

### Frontend
- Vercel: Automatic edge caching
- Other platforms: Use CDN (Cloudflare)

## Security Checklist

- [ ] Use HTTPS everywhere
- [ ] Set secure CORS origins
- [ ] Use environment variables (never commit secrets)
- [ ] Enable database backups
- [ ] Set up rate limiting (consider Cloudflare)
- [ ] Use API keys for admin endpoints
- [ ] Regular security updates

## Troubleshooting

### Backend won't start
- Check database connection string
- Verify all environment variables are set
- Check logs: `docker logs <container-name>`

### Frontend can't connect to backend
- Verify `NEXT_PUBLIC_API_BASE_URL` is correct
- Check CORS settings in backend
- Ensure backend is publicly accessible

### Database connection errors
- Verify `DATABASE_URL` format
- Check database is accessible from backend
- Ensure database exists and migrations are run

## Cost Estimates

- **Vercel (Frontend)**: Free tier available, Pro starts at $20/mo
- **Railway (Backend)**: $5/mo starter, scales with usage
- **Render (Backend)**: Free tier available, paid starts at $7/mo
- **Fly.io**: Pay-as-you-go, ~$5-10/mo for small apps
- **VPS (DigitalOcean)**: $6-12/mo for basic droplet

## Recommended Setup

For production, we recommend:
- **Frontend**: Vercel (free tier, excellent Next.js support)
- **Backend**: Railway or Render (easy PostgreSQL setup)
- **Database**: Managed PostgreSQL (Railway/Render provide this)

Total cost: **$0-15/month** for small to medium traffic.




