"""now we are creating a simple ui that we can share chestxray and our ml model can predict the wheather it is bacterial or viral or normal"""
import tkinter as tk
from tkinter import filedialog,Label# it is used for the file selection and all the stuff
from PIL import Image,ImageTk
import numpy as np # it is a library mainly used for the mathematical calculation and it have ndarry(for mathematical calculations)
import tensorflow as tf
import threading
import time


#now wer are loading the model to do that create an instance of that model 
model = tf.keras.models.load_model("pneumonia_model.h5")
# we have to define the class names
class_names=["Bacterial","Normal","Viral"]
# now we are going to preprocess the image
def preprocess_image(img_path):
    img=Image.open(img_path).convert("RGB")
    img = img.resize((150, 150), Image.Resampling.LANCZOS)
    img_array=np.array(img)/255.0
    img_array=np.expand_dims(img_array,axis=0)
    return img_array
#now we are predicing with an animation that animation is in another thread we are implementing multithreading so that two process in different threads
def predict_img():
    file_path=filedialog.askopenfilename()
    if file_path:
        # now this is showing the image in the ui
        img=Image.open(file_path)
        img=img.resize((250,250))
        img_tk=ImageTk.PhotoImage(img)# convert it from pil img to photoimage to show it in the ui
        image_label.config(image=img_tk)
        image_label.image=img_tk
        result_label.config(text="PREDICTING.........",fg="lime")
        root.update_idletasks() #keep running the prediciting message in it
        def run_prediction():
            time.sleep(1.5)
            img_array=preprocess_image(file_path)
            prediction=model.predict(img_array)
            predicted_class=class_names[np.argmax(prediction)]
            result_label.config(text=f"PREDICTION : {predicted_class}",fg="lime")
# now we are placing the prediction in a different thread other than the main tkinter ui
    threading.Thread(target=run_prediction).start()
# we are seting up main ui for our tkinter ui
root=tk.Tk()
root.title("PNEUMONIA X-RAY CLASSIFIER")
root.geometry("400x500")
root.configure(bg="#0a0a0a")
# we are placing a title in the root window
title=tk.Label(root,text="PNEUMONIA DETECTION",font=("Helvetica",18,"bold"),fg="lime",bg="#0a0a0a")
title.pack(pady=20)
# to upload a file we have to place an upload button inside the root while clicking we can upload a file like that
upload_btn=tk.Button(root,text="Upload X-ray",command=predict_img,font=("Helvetica",14),bg="black",fg="lime",activebackground="green",activeforeground="white")
upload_btn.pack(pady=10)
#to show the image
image_label=Label(root,bg="#0a0a0a")
image_label.pack(pady=10)
# now we are showing the result
result_label=Label(root,text="",font=("Helvetica",16),bg="#0a0a0a",fg="lime")
result_label.pack(pady=20)
root.mainloop()


