"""this phase is the data cleaning and path mean we are provinding
 a flow then after that we will build our cnn model """

import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#now we are giving the path this  in this we are providing the flow of data in our model for train val and test
train_path="chest_xray/train"
val_path="chest_xray/val"
test_path="chest_xray/test"
# next phase is  our data image generating for that we have to do some work in our data that is we doing with the ImageDataGenerator by using that 
#in this we will change the pixel value from 255 to 0-1 range so our cnn model can understand it in better and also we will do the random rotation zoom and flip
# main object is that my model dont use any simpler pattern to make my model  
train_datagen = ImageDataGenerator(
    rescale=1./255,              # Normalize pixel values
    rotation_range=15,           # Random rotation for making my model more powerflul
    zoom_range=0.2,              # Random zoom
    horizontal_flip=True         # Random horizontal flip
)
# we also have to rescale the pixel value of test and validation input 
val_datagen=ImageDataGenerator(rescale=1./255)
test_datagen=ImageDataGenerator(rescale=1./255)
train_generator=train_datagen.flow_from_directory(
    train_path,
    target_size=(150,150),
    batch_size=32,
    class_mode="categorical"
)
val_generator=val_datagen.flow_from_directory(
    val_path,
    target_size=(150,150),
    batch_size=32,
    class_mode="categorical"
)
test_generator=test_datagen.flow_from_directory(
    test_path,
    target_size=(150,150),
    batch_size=32,
    class_mode="categorical",
    shuffle=False
)
