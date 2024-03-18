# Importing libraries
import numpy as np
import pickle
from PIL import Image
import io
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Load the pre-trained model
def loadModel():
    model = pickle.load(open(r"D:\8th-sem-project\leukocyte_model", 'rb'))
    print("Model Loaded . ")
    return model

# For path image
def preprocess_image_path(img_path , img_height , img_width):
    img = image.load_img(img_path, target_size=(img_height , img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    print("Image Processed . ")
    return img_array

def predict_image_class_path(model, img_path , img_height , img_width):
    img_array = preprocess_image_path(img_path , img_height , img_width)
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    return class_index

# For Bytes images
def preprocess_image_bytes(image_bytes, img_height, img_width):
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((img_height, img_width))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    print("Image Processed.")
    return img_array

def predict_image_class_bytes(model, image_bytes, img_height, img_width):
    img_array = preprocess_image_bytes(image_bytes, img_height, img_width)
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    return class_index

# Main function
def main():
    
    # Class Names
    class_name = ['basophil', 'eosinophil', 'erythroblast', 'ig', 'lymphocyte', 'monocyte', 'neutrophil', 'platelet'] 
    
    # Test image path
    image_path = r'D:\8th-sem-project\bloodcells_dataset\neutrophil\BNE_229500.jpg'
    
    # Image parameters
    img_height = 300 
    img_width = 300
    
    # prediction Process
    model = loadModel()
    predicted_class = predict_image_class_path(model, image_path , img_height , img_width)
    
    # Out-Put
    print(f'The predicted class is: {class_name[predicted_class]}')

if __name__ == "__main__":
    main()
