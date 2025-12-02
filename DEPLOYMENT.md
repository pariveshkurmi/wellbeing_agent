# Deployment Guide for Hugging Face Spaces

This guide will help you deploy the Wellbeing Agent to Hugging Face Spaces.

## Prerequisites

1. A Hugging Face account (sign up at https://huggingface.co)
2. A Google API key for Gemini models (get one at https://makersuite.google.com/app/apikey)

## Step-by-Step Deployment

### 1. Create a New Space

1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. Fill in the details:
   - **Space name**: `wellbeing-agent` (or your preferred name)
   - **SDK**: Select **Gradio**
   - **Hardware**: Choose **CPU basic** (free tier) or upgrade if needed
   - **Visibility**: Public or Private
4. Click "Create Space"

### 2. Upload Your Files

You can upload files using one of these methods:

#### Option A: Using Git (Recommended)

```bash
# Clone your repository if you haven't already
git clone https://github.com/pariveshkurmi/wellbeing_agent.git
cd wellbeing_agent

# Add Hugging Face remote
git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/wellbeing-agent
# Replace YOUR_USERNAME with your Hugging Face username

# Push to Hugging Face
git push hf main
```

#### Option B: Using Web Interface

1. Go to your Space page
2. Click "Files and versions" tab
3. Click "Add file" → "Upload files"
4. Upload these files:
   - `app.py` (root level)
   - `requirements.txt`
   - `README.md` (or use README_HF.md and rename it)
   - `src/` directory (entire folder with all subdirectories)
   - `knowledge/` directory (if needed)

### 3. Set Environment Variables

1. Go to your Space settings
2. Navigate to "Variables and secrets" tab
3. Add a new secret:
   - **Key**: `GOOGLE_API_KEY`
   - **Value**: Your Google API key
4. Click "Add secret"

### 4. Wait for Build

Hugging Face will automatically:
- Install dependencies from `requirements.txt`
- Build your Space
- Deploy your app

You can monitor the build logs in the "Logs" tab.

### 5. Access Your App

Once the build completes, your app will be available at:
`https://huggingface.co/spaces/YOUR_USERNAME/wellbeing-agent`

## File Structure for HF Spaces

Your Space should have this structure:

```
wellbeing-agent/
├── app.py                 # Main entry point (required)
├── requirements.txt       # Python dependencies (required)
├── README.md             # Space description (optional but recommended)
├── src/
│   └── wellbeing_agent/
│       ├── __init__.py
│       ├── app.py
│       ├── crew.py
│       ├── main.py
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py
└── knowledge/
    └── user_preference.txt
```

## Troubleshooting

### Build Fails

- Check the logs in the "Logs" tab
- Verify `requirements.txt` has all dependencies
- Ensure Python version compatibility (3.10-3.13)

### App Doesn't Work

- Verify `GOOGLE_API_KEY` is set correctly
- Check that all files are uploaded
- Review error messages in the app logs

### Import Errors

- Make sure `src/` directory is uploaded
- Verify `app.py` has correct import paths
- Check that all `__init__.py` files are present

## Updating Your Space

After making changes:

```bash
git add .
git commit -m "Update app"
git push hf main
```

Or upload new files through the web interface.

## Resources

- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Gradio Documentation](https://www.gradio.app/docs/)
- [CrewAI Documentation](https://docs.crewai.com/)

