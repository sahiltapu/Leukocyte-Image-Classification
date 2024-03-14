import streamlit as st
import os
from CNN_Predict import loadModel , predict_image_class_bytes
from PIL import Image


def is_image(uploaded_file):
    return uploaded_file.type.startswith("image/") if uploaded_file else False

def is_size_within_limit(uploaded_file, max_size_mb=2):
    max_size_bytes = max_size_mb * 1024 * 1024
    return uploaded_file.size <= max_size_bytes if uploaded_file else False

def read_image_bytes(uploaded_file):
    return uploaded_file.read() if uploaded_file else None

def display_image(bytes_data):
    st.image(bytes_data, caption="Uploaded Image", use_column_width=False)


def upload_image(max_size_mb=2):
    uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "png"] , accept_multiple_files= False)

    if uploaded_file:
        if is_image(uploaded_file):
            if is_size_within_limit(uploaded_file, max_size_mb):
                bytes_data = read_image_bytes(uploaded_file)
                display_image(bytes_data)
                return bytes_data
            else:
                st.warning(f"Please upload an image file with a size less than or equal to {max_size_mb}MB.")
        else:
            st.warning("Please upload only image files (jpg, jpeg, or png).")

    else:
        st.text("No file uploaded.")
        return False
 

@st.cache_data(persist = True)   
def Load_leukocyte_model():
    return loadModel()
    
def cnn_model():
    st.markdown("""<h1 style='text-align: center; color: #67C6E3;'>Welcome to Leukocyte Image Prediction System.</h1>""", unsafe_allow_html=True)
    model = Load_leukocyte_model()
    image_path = upload_image()
    if image_path:
        if st.button("Predict", type="primary"):
            predicted_class = predict_image_class_bytes(model,image_path,300,300)
            class_name = ['basophil', 'eosinophil', 'erythroblast', 'ig', 'lymphocyte', 'monocyte', 'neutrophil', 'platelet'] 
            st.subheader(f'The predicted class is: {class_name[predicted_class]}')
            
def display_images_from_assets_folder(folder_path, cols, images_per_row):
    row_count = 0
    tcount = 0
    for root, dirs, files in os.walk(folder_path):
        tcount = 0
        
        for file in files:
            if tcount == 0:
                st.markdown(os.path.basename(root))
                
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                tcount = 1
                image_path = os.path.join(root, file)
                with Image.open(image_path) as img:
                    img.thumbnail((150, 150))
                    cols[row_count % images_per_row].image(img, use_column_width=True)
                row_count += 1
                if row_count % images_per_row == 0:
                    cols = st.columns(8)

def main():
    st.set_page_config(layout="wide", page_title="Leukocyte Image Prediction")
    cnn_model()
   # Display images from folders inside the assets folder
    st.markdown("## Some suggestions from different types.")
    asset_folder = "assets"
    cols = st.columns(8)
    images_per_row = 5
    display_images_from_assets_folder(asset_folder , cols , images_per_row)

if __name__ == "__main__":
    main()
