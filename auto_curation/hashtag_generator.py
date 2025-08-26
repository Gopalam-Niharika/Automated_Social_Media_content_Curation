import google.generativeai as genai

# 🔑 Gemini Setup
GEMINI_API_KEY = "AIzaSyCHsfibtq7lh9uqt_2O9wzNx7Ttc6HOihU"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_hashtags(topic: str) -> str:
    prompt = f"Generate 5 trending hashtags for a social media post about '{topic}'."
    response = model.generate_content(prompt)
    return response.text.strip()
