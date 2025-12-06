#!/usr/bin/env bash
set -euo pipefail

echo "🚀 Credence Deployment Helper"
echo "=============================="
echo ""
echo "Choose deployment option:"
echo "1) Vercel (Frontend) + Railway (Backend) - Recommended"
echo "2) Vercel (Frontend) + Render (Backend)"
echo "3) Docker Compose (Full Stack)"
echo "4) Fly.io (Full Stack)"
echo ""
read -p "Enter choice [1-4]: " choice

case $choice in
  1)
    echo ""
    echo "📦 Deploying to Vercel + Railway"
    echo ""
    echo "Frontend (Vercel):"
    echo "1. Push code to GitHub"
    echo "2. Go to https://vercel.com and import repository"
    echo "3. Set environment: NEXT_PUBLIC_API_BASE_URL = your Railway backend URL"
    echo ""
    echo "Backend (Railway):"
    echo "1. Go to https://railway.app and create project"
    echo "2. Connect GitHub repo, select 'backend' folder"
    echo "3. Add environment variables (see DEPLOYMENT.md)"
    echo "4. Deploy"
    ;;
  2)
    echo ""
    echo "📦 Deploying to Vercel + Render"
    echo ""
    echo "See DEPLOYMENT.md for detailed instructions"
    ;;
  3)
    echo ""
    echo "🐳 Deploying with Docker Compose"
    echo ""
    if [ ! -f .env ]; then
      echo "⚠️  .env file not found. Creating from template..."
      cp .env.example .env
      echo "✅ Please edit .env with your production values"
    fi
    echo "Starting services..."
    docker-compose -f docker-compose.prod.yml up -d
    echo "✅ Services started. Check logs with: docker-compose -f docker-compose.prod.yml logs -f"
    ;;
  4)
    echo ""
    echo "✈️  Deploying to Fly.io"
    echo ""
    echo "Backend:"
    echo "cd backend && fly launch"
    echo ""
    echo "Frontend:"
    echo "cd frontend && fly launch"
    echo ""
    echo "See DEPLOYMENT.md for detailed instructions"
    ;;
  *)
    echo "Invalid choice"
    exit 1
    ;;
esac




