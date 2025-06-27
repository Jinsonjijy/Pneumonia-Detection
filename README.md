✅ 1. Clone the Repository
Download or clone this GitHub repository to your local machine.

✅ 2. Set Up Virtual Environment (Optional but Recommended)
Create a virtual environment to keep your project dependencies organized.

On Windows:
Open your terminal and run:

nginx
Copy
Edit
python -m venv venv
venv\Scripts\activate
On Mac/Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
✅ 3. Install Required Libraries
Make sure you have the following Python libraries installed:

tensorflow

pillow

numpy
You can install them by running:

bash
Copy
Edit
pip install tensorflow pillow numpy
✅ 4. Download and Prepare Dataset
Go to the Kaggle Chest X-ray Pneumonia dataset.

Download and extract the dataset.

Place the extracted folder in the root project directory like this:

bash
Copy
Edit
📁 pneumonia-detection/
   └── chest_xray/
       ├── train/
       ├── val/
       └── test/
✅ 5. Organize the Dataset (Optional but Recommended)
To structure or preprocess the data more cleanly (if needed), run the following Python scripts:

organize_train.py → organizes training images

organize_val.py → organizes validation images

organize_test.py → organizes test images

These scripts can help ensure the dataset is in proper format.

✨ If your dataset from Kaggle is already structured properly, this step can be skipped.

✅ 6. Load Dataset
The load_data.py script handles the loading of train, validation, and test sets using ImageDataGenerator.

Ensure this file is imported inside train_model.py like this:

python
Copy
Edit
from load_data import train_generator, val_generator, test_generator
✅ 7. Train the CNN Model
Once the dataset is ready, run:

bash
Copy
Edit
python train_model.py
This will:

Build a Convolutional Neural Network (CNN)

Train the model using your dataset

Save the model as pneumonia_model.h5

✅ 8. Launch the GUI to Predict X-rays
To interactively predict whether an uploaded chest X-ray shows signs of bacterial, viral, or normal status:

bash
Copy
Edit
python gui_predict.py
Click "Upload X-ray"

Choose an image from your system

It will briefly show "PREDICTING..."

Then display the result like:
✅ PREDICTION: Viral (or Bacterial / Normal)

📂 Project Structure
bash
Copy
Edit
📁 pneumonia-detection/
│
├── chest_xray/              # Dataset (downloaded from Kaggle)
├── gui_predict.py           # GUI using Tkinter for predictions
├── train_model.py           # Script to build and train the CNN
├── load_data.py             # Loads and preprocesses the dataset
├── organize_train.py        # Optional data structuring (train)
├── organize_val.py          # Optional data structuring (val)
├── organize_test.py         # Optional data structuring (test)
├── pneumonia_model.h5       # Trained model (output of training)
├── venv/                    # Virtual environment
