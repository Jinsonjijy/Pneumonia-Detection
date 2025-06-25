import cv2
import matplotlib.pyplot as plt
import os
base_path="chest_xray/train" # this is the base folder location path that we are doing in it in the train folder we are implementing it
normal_path=os.path.join(base_path,"NORMAL")
bacterial_path=os.path.join(base_path,"Bacterial")
viral_path=os.path.join(base_path,"Viral")#so we made the path for the normal and bacterila and viral we just made and stored it in a variables
# next we are going to make this bgr picture into the rgb and then plot it using the matplotlib and we will undertand the  diff of normal bacterial and viral
def load_image(folder):
    file=os.listdir(folder)[0] #get the first file from each folder that is normal bacterial viral
    img=cv2.imread(os.path.join(folder,file))#this read the file from the folder
    return cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
normal_img=load_image(normal_path)
bacterial_img=load_image(bacterial_path)
viral_img=load_image(viral_path)
#no we get normal img bacterial image and viral image in the rgb format and we are going to form a grahph plot it in using matplotlib
plt.figure(figsize=(12,4))
#this is for the normal plot
plt.subplot(1,3,1)
plt.imshow(normal_img)
plt.title("normal_image")
plt.axis('off')
#this is for the bacterial plto
plt.subplot(1,3,2)
plt.imshow(bacterial_img)
plt.title("bacterial_img")
plt.axis('off')
#this is for the viral subplot
plt.subplot(1,3,3)
plt.imshow(viral_img)
plt.title("viral_img")
plt.axis('off')
plt.tight_layout()
plt.show()