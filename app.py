from taipy.gui import Gui
import tensorflow as tf
import numpy as np
from PIL import Image

# Load pretrained model
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# Class labels
decode_predictions = tf.keras.applications.mobilenet_v2.decode_predictions
preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input

# State variables
image_path = None
prediction = ""

def classify_image(state):
    if state.image_path is None:
        state.prediction = "Please upload an image."
        return

    img = Image.open(state.image_path).resize((224, 224))
    img_array = np.array(img)

    if img_array.shape[-1] == 4:  # RGBA → RGB
        img_array = img_array[..., :3]

    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded = decode_predictions(preds, top=1)[0][0]

    state.prediction = f"{decoded[1]} ({decoded[2]*100:.2f}%)"

# UI layout
page = """
# 🖼️ Image Classification App

Upload an image and get its predicted class.

<|{image_path}|file_selector|extensions=.jpg,.png|label=Upload Image|>

<|Classify Image|button|on_action=classify_image|>

### Prediction
**{prediction}**
"""

Gui(page).run()
