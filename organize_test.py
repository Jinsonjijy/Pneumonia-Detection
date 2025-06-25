import os 
import shutil
from pathlib import Path
source_folder="chest_xray/test/PNEUMONIA" # this is the source folder right
Bacterial_folder="chest_xray/test/Bacterial"
Viral_folder="chest_xray/test/Viral"
Path(Bacterial_folder).mkdir(parents=True,exist_ok=True)
Path(Viral_folder).mkdir(parents=True,exist_ok=True)
for filename in os.listdir(source_folder):
    src_path=os.path.join(source_folder,filename)
    if "bacteria" in filename:
        shutil.copy(src_path,os.path.join(Bacterial_folder,filename))
    elif "virus" in filename:
        shutil.copy(src_path,os.path.join(Viral_folder,filename))
if os.path.exists("chest_xray/test/PNEUMONIA"):
    shutil.rmtree("chest_xray/test/PNEUMONIA")
    print("deleted the old pnuemonia folder in the test")