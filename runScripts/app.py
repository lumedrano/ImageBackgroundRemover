import streamlit as st
from PIL import Image, ImageOps, ImageColor
from rembg import remove
import io

st.set_page_config(page_title="Background Remover", layout="centered")
st.title("🖼️ Background Remover")

st.write("Upload an image and customize the background or size before downloading.")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    with st.spinner("Processing image..."):
        #read and remove background
        input_image = Image.open(uploaded_file).convert("RGBA")
        result = remove(input_image)

    st.subheader("Advanced Options")

    #color picker for background color options
    bg_color = st.color_picker("Pick a background color", "#FFFFFF")

    #format download
    download_format = st.selectbox("Download format", ["PNG", "JPG"])

    # padding
    add_padding = st.checkbox("Add padding around the image")
    padding_size = 0
    if add_padding:
        padding_size = st.slider("Padding size (px)", 0, 200, 20)

    # resize option
    resize = st.checkbox("Resize image")
    resized_width, resized_height = result.size
    if resize:
        resized_width = st.number_input("Width", min_value=1, value=result.width)
        resized_height = st.number_input("Height", min_value=1, value=result.height)

    # preview
    show_checkerboard = st.checkbox("Show transparency (checkerboard preview)")

    # create the background of chosen color
    bg = Image.new("RGBA", result.size, ImageColor.getrgb(bg_color) + (255,))
    final_image = Image.alpha_composite(bg, result).convert("RGB")

    # add padding if selected
    if add_padding:
        final_image = ImageOps.expand(final_image, border=padding_size, fill=bg_color)

    # resize if selected
    if resize:
        final_image = final_image.resize((int(resized_width), int(resized_height)))

    # display before and after
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(input_image, use_container_width=True)

    with col2:
        st.subheader("Processed Image")
        st.image(final_image, use_container_width=True)

    
    if show_checkerboard:
        st.subheader("Transparency Preview")
        st.image(result, caption="Without background color", use_container_width=True)

    # prepare download
    img_bytes = io.BytesIO()
    if download_format == "PNG":
        final_image.save(img_bytes, format="PNG")
        mime = "image/png"
        filename = "no_bg_image.png"
    else:
        final_image.save(img_bytes, format="JPEG")
        mime = "image/jpeg"
        filename = "no_bg_image.jpg"

    st.download_button("Download Image", img_bytes.getvalue(), filename, mime)
