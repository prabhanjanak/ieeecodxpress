import cv2
import numpy as np
import tensorflow as tf

# Load and preprocess the image
image = cv2.imread(r"C:\Users\sammj\Desktop\2.jpg", cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
resized_image = cv2.resize(image, (28, 28))  # Resize the image to 28x28

# Normalize the image
normalized_image = resized_image / 255.0  # Normalize pixel values

# Reshape the image to match the model input shape
input_image = np.reshape(normalized_image, (1, 28, 28))  # Reshape to (1, 28, 28)

# Load the trained model
model = tf.keras.models.load_model(r"C:\Users\sammj\Desktop\model_2.keras")

# Make predictions
predictions = model.predict(input_image)

# Get the predicted class
predicted_class = np.argmax(predictions)
print("Predicted class:", predicted_class)
