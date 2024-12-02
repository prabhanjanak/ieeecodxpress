import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load MNIST dataset
(_, _), (x_test, y_test) = mnist.load_data()
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0
y_test = to_categorical(y_test)

# Load pre-trained model
path = r"C:\Users\sammj\Desktop\model.keras"
model = load_model(path)

# Function to preprocess the image
def preprocess_img(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
    return resized.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Preprocess the image and predict the digit
    preprocessed = preprocess_img(frame)
    prediction = model.predict(preprocessed)
    digit = np.argmax(prediction)

    # Show the predicted digit in a window
    cv2.putText(frame, str(digit), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Prediction', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
