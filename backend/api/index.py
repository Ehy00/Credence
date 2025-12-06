"""
Vercel serverless function entry point for FastAPI.
Uses Mangum to convert FastAPI app to ASGI handler.
"""
import sys
from pathlib import Path

# Add parent directory to Python path for imports
backend_dir = Path(__file__).parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from mangum import Mangum
from app.main import app

# Wrap FastAPI app with Mangum for Vercel serverless functions
# The handler variable name is required by Vercel
handler = Mangum(app, lifespan="off")

