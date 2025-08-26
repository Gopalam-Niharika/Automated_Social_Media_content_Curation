import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from hackernews import fetch_trending_topics
from content_gen import generate_caption
from hashtag_generator import generate_hashtags
from image_generator import generate_image

st.set_page_config(page_title="Automated Social Media Content Curation", layout="centered")

st.title("✨ Automated Social Media Content Curation")

# Sidebar settings
limit = st.sidebar.slider("Number of topics", 5, 50, 5)
min_score = st.sidebar.slider("Minimum score for trending", 50, 1000, 150)

# Initialize session state
if "topics" not in st.session_state:
    st.session_state.topics = []

if "user_content" not in st.session_state:
    st.session_state.user_content = []


# ---------------------------
# 📈 Hacker News Trending Topics
# ---------------------------
st.header("📈 Hacker News Trending Topics")

if st.button("Fetch Trending Topics"):
    st.session_state.topics = fetch_trending_topics(limit=limit, min_score=min_score)

# Display topics (persist after rerun)
if st.session_state.topics:
    for idx, t in enumerate(st.session_state.topics):
        with st.expander(f"{t['title']} (⭐ {t['score']})"):
            st.markdown(f"[Read more]({t['url']})")

            # Button for generating AI content per topic
            if st.button(f"Generate AI Content for Topic {idx}"):
                caption = generate_caption(t)
                hashtags = generate_hashtags(t)

                st.write("**Caption:**", caption)
                st.write("**Hashtags:**", hashtags)

                try:
                    with st.spinner("🎨 Generating AI Image..."):
                        img_path = generate_image(t["title"], output_file=f"generated_topic_{idx}.png")
                        st.image(img_path, caption="AI Generated Image", use_column_width=True)
                except Exception as e:
                    st.error(f"Image generation failed: {e}")


# ---------------------------
# 📝 User Custom Prompt
# ---------------------------
st.header("📝 Generate Content from Your Own Prompt")

user_prompt = st.text_input("Enter your custom topic or prompt:")

if st.button("Generate Content from Prompt"):
    if user_prompt.strip():
        caption = generate_caption({"title": user_prompt})
        hashtags = generate_hashtags({"title": user_prompt})

        content = {
            "prompt": user_prompt,
            "caption": caption,
            "hashtags": hashtags,
            "image": None
        }

        try:
            with st.spinner("🎨 Generating AI Image..."):
                img_path = generate_image(user_prompt, output_file=f"user_generated_{len(st.session_state.user_content)}.png")
                content["image"] = img_path
        except Exception as e:
            st.error(f"Image generation failed: {e}")

        # Save to session state
        st.session_state.user_content.append(content)


# ---------------------------
# 📂 Display User-Generated Content (persistent)
# ---------------------------
if st.session_state.user_content:
    st.subheader("📂 Your Generated Content")
    for idx, c in enumerate(st.session_state.user_content):
        with st.expander(f"📝 {c['prompt']}"):
            st.write("**Caption:**", c["caption"])
            st.write("**Hashtags:**", c["hashtags"])
            if c["image"]:
                st.image(c["image"], caption="AI Generated Image", use_container_width=True)
