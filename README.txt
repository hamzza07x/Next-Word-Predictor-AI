===================================================
NEXT WORD PREDICTOR
===================================================

A simple Tkinter-based Python application for predicting the next word in a sentence, now available as an executable (.exe) file. No Python installation is required to run the program.

---------------------------------------------------
FEATURES
---------------------------------------------------
1. **User Authentication**
   - Register and log in with a username and password.

2. **Next Word Prediction**
   - Predicts the next two words based on the last word entered.

3. **History Tracking**
   - Saves and displays past inputs and predictions.

4. **Graphical User Interface (GUI)**
   - Built using Python's Tkinter library.

5. **Standalone Executable**
   - Run the program directly via the `.exe` file.

---------------------------------------------------
REQUIREMENTS
---------------------------------------------------
No Python installation is required. Simply double-click the `.exe` file to run the application.

---------------------------------------------------
HOW TO USE
---------------------------------------------------
1. **Download the Executable**:
   - Ensure all required files (`predictions.txt`, `users.txt`, etc.) are in the same directory as the `.exe` file.

2. **Run the Application**:
   - Double-click the `.exe` file to launch the program.

3. **Log In or Register**:
   - Log in with your existing credentials or register a new account.

4. **Predict Next Words**:
   - Enter a sentence or word, and the app will suggest the next possible words.

5. **View History**:
   - Access your past inputs and predictions through the "View History" button.

---------------------------------------------------
FILE STRUCTURE
---------------------------------------------------
- `NextWordPredictor.exe`:
   The standalone executable file.

- `predictions.txt`:
   Stores word-prediction data in the format:



- `users.txt`:
Stores user credentials in the format:



- `history.txt`:
Stores prediction history for later viewing.

---------------------------------------------------
NOTES
---------------------------------------------------
- Ensure the `predictions.txt` file exists in the same directory as the `.exe` file.
- The application will create `users.txt` and `history.txt` automatically if they do not exist.

---------------------------------------------------
CREATING THE .EXE FILE (For Developers)
---------------------------------------------------
To generate the `.exe` file from the Python script, use PyInstaller:
1. Install PyInstaller:



2. Run the following command:


3. The `.exe` file will be created in the `dist` folder.

---------------------------------------------------
LICENSE
---------------------------------------------------
This project is licensed under the MIT License.

---------------------------------------------------
AUTHOR
---------------------------------------------------
Developed by Muhammad Hamza