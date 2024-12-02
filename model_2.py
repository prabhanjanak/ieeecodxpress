import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

mnsit = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnsit.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=2)

path = r"C:\Users\sammj\Desktop\model_2.keras"
# model.save(path)

loss, acc = model.evaluate(x_test, y_test)
print(loss)
print(acc)

image = cv2.imread(r"C:\Users\sammj\Desktop\4.jpg", cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
resized_image = cv2.resize(image, (28, 28)) 

predict = model.predict(resized_image)
print(np.argmax(predict))
