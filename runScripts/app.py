import streamlit as st
from PIL import Image, ImageOps
from rembg import remove
import io

st.set_page_config(page_title="Background Remover", layout="centered")
st.title("🖼️ Background Remover")

st.write("Upload an image and get it with a **white** background.")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    with st.spinner("Processing image..."):
        # read and remove image background
        input_image = Image.open(uploaded_file).convert("RGBA")
        result = remove(input_image)

        #create the white background
        white_bg = Image.new("RGBA", result.size, (255, 255, 255, 255))
        final_image = Image.alpha_composite(white_bg, result).convert("RGB")

        #display a before and after preview
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(input_image, use_container_width=True)

        with col2:
            st.subheader("Processed Image")
            st.image(final_image, use_container_width=True)

        #create the download button
        img_bytes = io.BytesIO()
        final_image.save(img_bytes, format="PNG")
        st.download_button("Download Image", img_bytes.getvalue(), "no_bg_image.png", "image/png")
