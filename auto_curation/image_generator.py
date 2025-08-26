import os
import requests

def generate_image(prompt, output_file="generated.png"):
    api_key = os.getenv("STABILITY_API_KEY")
    if not api_key:
        raise Exception("Missing Stability API key. Please add STABILITY_API_KEY in your .env file")

    api_host = os.getenv("API_HOST", "https://api.stability.ai")

    # ✅ Corrected engine ID
    engine_id = "stable-diffusion-xl-1024-v1-0"

    url = f"{api_host}/v1/generation/{engine_id}/text-to-image"

    response = requests.post(
        url,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [{"text": prompt}],
            "cfg_scale": 7,
            "clip_guidance_preset": "FAST_BLUE",
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception(f"Image generation request failed: {response.text}")

    data = response.json()

    if "artifacts" not in data:
        raise Exception(f"No image artifacts found in response: {data}")

    # Save image
    import base64
    image_base64 = data["artifacts"][0]["base64"]
    image_bytes = base64.b64decode(image_base64)

    with open(output_file, "wb") as f:
        f.write(image_bytes)

    return output_file
