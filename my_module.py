import streamlit as st
import requests
import re


def generate_image(prompt):
    # Set OpenAI API Key
    openai_api_key = "sk-xxxx"

    # Streamlit App
    st.title("DALL-E Image Generation with OpenAI API and Tencent Cloud")

    # Prompt input
    print("prompt:", prompt)
    if prompt:
        with st.spinner("Waiting for DALL-E..."):
            prompt = re.sub(r"[^a-zA-Z,\s]+", "", prompt).strip()
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {openai_api_key}",
            }
            data = {"prompt": prompt, "n": 1, "size": "1024x1024"}
            response = requests.post(
                "https://service-xxxxw.apigw.tencentcs.com/v1/images/generations",
                headers=headers,
                json=data,
            )
            print("data:", data)
            response_json = response.json()
            print("response_json:", response.json())
            if (
                "data" in response_json
                and len(response_json["data"]) > 0
                and "url" in response_json["data"][0]
            ):
                image_url = response_json["data"][0]["url"]
                st.image(image_url, caption=prompt)
                return image_url
            else:
                st.warning("Failed to generate image with DALL-E API.", icon="⚠️")
                return None
