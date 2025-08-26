import google.generativeai as genai

# 🔑 Gemini Setup
GEMINI_API_KEY = "AIzaSyCHsfibtq7lh9uqt_2O9wzNx7Ttc6HOihU"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_caption(topic: str) -> str:
    prompt = f"Write an engaging social media caption for '{topic}'."
    response = model.generate_content(prompt)
    return response.text.strip()
