import streamlit as st
from my_module import generate_image

st.header("Image Generator")

prompt = st.text_input("Enter your prompt", "A cat sitting on a table")

if prompt:
    with st.spinner("Generating image..."):
        image_url = generate_image(prompt)
    if image_url:
        st.success("Generated image!")
        st.image(image_url, caption=prompt)
    else:
        st.warning("Failed to generate image with DALL-E API.", icon="⚠️")
