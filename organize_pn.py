"""this is doing to seperate the bacterial and the viral data in different folder so i can access each one in a seperate mode """
import os
import shutil
from pathlib import Path
source_folder="chest_xray/train/PNEUMONIA"# this is defining the source folder so we can just access by calling the variable
bacterial_folder="chest_xray/train/Bacterial" #this is for making the path of that in a variable and we can access it 
viral_folder="chest_xray/train/Viral"#this is for making the path of that in a variable and we can access it 
Path(bacterial_folder).mkdir(parents=True,exist_ok=True)
Path(viral_folder).mkdir(parents=True,exist_ok=True) #this is for doing the Path will point to the lacation and also the mkdir create a folder in the location if it is not present that is why we use the paraent and exit_ok paramenter in the mkdir paramenters
for filename in os.listdir(source_folder):
    src_path=os.path.join(source_folder,filename)
    if "bacteria" in filename:
        shutil.copy(src_path,os.path.join(bacterial_folder,filename))
    elif "virus" in filename:
        shutil.copy(src_path,os.path.join(viral_folder,filename))