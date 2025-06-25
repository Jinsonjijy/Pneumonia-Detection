from load_data import train_generator, val_generator, test_generator
from keras.models import Sequential 
from keras.layers import Conv2D,MaxPooling2D,Dropout,Dense,Flatten
# we are building the cnn model 
model=Sequential([
    Conv2D(32,(3,3),activation="relu",input_shape=(150,150,3)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64,(3,3),activation="relu"),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(128,(3,3),activation="relu"),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128,activation='relu'),
    Dropout(0.5),
    Dense(3,activation="softmax"),
])
# we made the model
#next we we compiling the model
model.compile(
    optimizer="adam",# we use an optimizer adam it is very it is very powerful
    loss="categorical_crossentropy",# it make how to measure error
    metrics=["accuracy"],


)
model.summary()# just for see the structure of the model
#next we are training the mode
history=model.fit(
    train_generator,
    epochs=10,
    validation_data=val_generator

)
test_loss, test_accuracy = model.evaluate(test_generator)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
print(f"Test Loss: {test_loss:.4f}")

# (Optional) Save the trained model
model.save("pneumonia_model.h5")
print("Model saved successfully.")