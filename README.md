# Automated_Social_Media_content_Curation

This project automates the process of generating captions, hashtags, and images for social media posts using Google Gemini AI and Stability AI (Stable Diffusion).
It also fetches trending topics from Hacker News so you can instantly generate content based on hot discussions or your own custom prompt.

✨ Features

📈 Fetch trending topics from Hacker News

📝 Generate AI captions with Gemini

🔖 Generate AI hashtags with Gemini

🎨 Generate AI images with Stability AI

⌨️ User can provide custom prompts to generate content

💾 Save generated images inside the outputs/ folder

🗂️ Project Structure
auto_curation (main folder)

1.  .env                         # Stores your API keys
2.   app.py                       # Main Streamlit app
3.   hackernews.py                 # Fetch Hacker News topics & trending
4.   content_gen.py                # Captions generator
5.   hashtag_generator.py          # Hashtags generator
6.   image_generator.py            # Image generator
7.   requirements.txt              # Dependencies
8.   README.md                     # Documentation

⚙️ Installation

# Clone the repo

git clone https://github.com/your-username/auto_curation.git
cd auto_curation


# Create a virtual environment (recommended)

python -m venv .cura
source .cura/bin/activate   # (Linux/Mac)
.cura\Scripts\activate      # (Windows)


# Install dependencies

pip install -r requirements.txt

# 🔑 Setup API Keys

Create a .env file in the root of your project:

GEMINI_API_KEY=your_gemini_api_key_here
STABILITY_API_KEY=your_stability_api_key_here


# Get your keys:
Google Gemini API
Stability AI (Stable Diffusion)

▶️ Run the App

Start Streamlit:

**streamlit run app.py**


The app will launch in your browser at http://localhost:8501
 🎉

📸 Example Workflow

Fetch trending topics from Hacker News.

Click Generate AI Content for a topic → get caption + hashtags + AI image.

Or enter a custom prompt → generate content from scratch.

Save and use generated content for social media posting.

📌 Requirements

Python 3.9+

Internet connection

API Keys for Gemini & Stability AI

🛠️ Future Improvements

✅ Direct posting to Twitter / LinkedIn / Instagram

✅ Support for video & audio generation

✅ Analytics on generated post performance

🔥 Built with Streamlit + Gemini AI + Stability AI
