# 🚀 Deployment Guide - Render Free Tier

## Prerequisites
- GitHub account
- Render account (free at https://render.com)
- Pinecone account with API key
- Git initialized in your project

## Step-by-Step Deployment

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Deploy FastAPI Backend on Render

1. Go to https://render.com and sign in
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `rag-api` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free
   
5. Click **Create Web Service**

6. Go to **Environment** tab and add these variables:
   ```
   PINECONE_API_KEY=<your_pinecone_key>
   PINECONE_INDEX_NAME=<your_index_name>
   GEMINI_API_KEY=<your_gemini_api_key>
   ```

### 3. Deploy Streamlit Frontend on Streamlit Cloud (Free)

1. Go to https://streamlit.io/cloud
2. Sign in with GitHub
3. Click **New app**
4. Select repository, branch, and main file: `app.py`
5. Click **Deploy**

6. In Streamlit Cloud app settings, update `app.py` to use your Render backend URL:
   ```python
   API_URL = "https://your-rag-api.onrender.com/query"  # Replace with your Render URL
   ```

### 4. Get Your Render API URL

After deployment, your FastAPI backend will be live at:
```
https://rag-api.onrender.com
```

Update `app.py` to use this URL in production:
```python
# Use environment variable for flexibility
import os
API_URL = os.getenv("API_URL", "http://localhost:8000/query")
```

### 5. Get a Gemini API Key (IMPORTANT)

Since we transitioned from local Ollama to the Google Gemini API:
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click **Create API Key**.
4. Copy the API key and set it as `GEMINI_API_KEY` in your environment or Render environment variables.

## Environment Variables Required

Set these in Render dashboard:
- `PINECONE_API_KEY` - Your Pinecone API key
- `PINECONE_INDEX_NAME` - Your Pinecone index name
- `GEMINI_API_KEY` - Your Google Gemini API key

## Free Tier Limitations ⚠️

- **Render**: 
  - Free tier apps spin down after 15 minutes of inactivity
  - Limited to 0.5GB RAM
  - Cold starts may be slow
  
- **Streamlit Cloud**: 
  - Free tier available
  - App may sleep after inactivity

## Troubleshooting

### "Module not found" errors
- Ensure all imports in your code match `requirements.txt`
- Check Python version compatibility

### API connection errors
- Verify environment variables are set correctly
- Check that Render URLs are accessible

### Slow responses
- Free tier has limited resources; consider upgrading for production
- Check Ollama performance; it may be the bottleneck

## Next Steps

For production, consider:
- Upgrading Render to paid tier for better performance
- Using a managed LLM service (OpenAI API, Anthropic, etc.)
- Adding a PostgreSQL database if needed
- Setting up monitoring and logging

---

Questions? Check Render docs: https://render.com/docs
