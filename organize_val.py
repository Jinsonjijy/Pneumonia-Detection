"""
this python file is used to do validation in the ml model mainly the parameters

"""

import os
import shutil
from pathlib import Path
source_folder="chest_xray/val/PNEUMONIA"
Bacterial_folder="chest_xray/val/Bacterial" 
Viral_folder="chest_xray/val/Viral"
Path(Bacterial_folder).mkdir(parents=True,exist_ok=True) 
Path(Viral_folder).mkdir(parents=True,exist_ok=True) # this is we are making the folders that we are making the two folders bacterial and viral
for filename in os.listdir(source_folder):
    src_path=os.path.join(source_folder,filename)
    if "bacteria" in filename:
        shutil.copy(src_path,os.path.join(Bacterial_folder,filename))
    elif "virus" in filename:
        shutil.copy(src_path,os.path.join(Viral_folder,filename))
if os.path.exists("chest_xray/val/PNEUMONIA"):
    shutil.rmtree("chest_xray/val/PNEUMONIA")
    print("deleted the PNEUMONIA folder from the validation")
