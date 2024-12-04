### Muhammad Hamza - Next Word Predictor

A simple Tkinter-based Python application for predicting the next word in a sentence. The app allows users to log in, enter text, and get suggestions for the next words based on previous input.

## Features
- **Login and User Registration**: Users can register and log in with a username and password.
- **Next Word Prediction**: Based on the user's input, the app predicts the next word using pre-defined suggestions.
- **History**: Keeps track of past user inputs and their predictions.
- **GUI**: A simple and intuitive graphical user interface using Tkinter.

## Files Included
- `NextWordPredictor.exe`: Executable file for the application.
- `nwp.py`: Python source code for the application.
- `predictions.txt`: File containing word suggestions.
- `users.txt`: File storing registered user data.
- `history.txt`: File containing the history of user inputs and predictions.
- `videos.zip`: Contains video files related to the project.
- `images.zip`: Contains image files used in the project.
- `icons.zip`: Contains icon files for the application.
- `dist.zip`: Contains distribution files for the project.
- `build.zip`: Contains build files for the project.
- `README.md`: This file.
- `README.txt`: A guide for users who want to use the application.

## How to Extract ZIP Files
If you want to access the contents of the ZIP files, follow these steps:

### Download all ZIP files:
- `videos.zip`
- `images.zip`
- `icons.zip`
- `dist.zip`
- `build.zip`

### Extract the ZIP files:
1. Download each ZIP file to your local machine.
2. Extract all the files into the same directory where the `.exe` or Python script is located.
   - On Windows, right-click each ZIP file and select **Extract All...**, then choose the same directory.
   - On macOS or Linux, double-click the ZIP file to extract it, or use the command line:
     ```bash
     unzip videos.zip
     unzip images.zip
     unzip icons.zip
     unzip dist.zip
     unzip build.zip
     ```

After extraction, you will find all the necessary files ready to use in the application.

## Requirements
- **Python 3.x** (for running the Python script version)
- **Tkinter** (usually included with Python)
- A text editor for modifying `predictions.txt` and `users.txt`

## How to Use

### Running the `.exe` File
1. Download the `NextWordPredictor.exe` file from the repository.
2. Run the `.exe` file. It will open the GUI application.
3. **Login**: Enter your username and password to log in, or **Register** a new account.
4. **Predict Next Words**: Type your sentence and click **Predict Next Words** to get suggestions.
5. **View History**: You can view the history of past inputs and their predictions by clicking the **View History** button.

### Running the Python Script
If you prefer to run the app from source, you can do so by running the `nwp.py` file.
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install required dependencies:
   ```bash
   pip install tkinter
