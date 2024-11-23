import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText

class NextWordPredictor:
    def __init__(self, suggestions_file='predictions.txt'):
        self.suggestions_dict = self.load_suggestions_from_file(suggestions_file)

    def load_suggestions_from_file(self, file_path):
        suggestions_dict = {}
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if ':' in line:
                        word, predictions = line.strip().split(':', 1)
                        suggestions_dict[word.strip()] = [prediction.strip() for prediction in predictions.split(',')]
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file '{file_path}' was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        return suggestions_dict

    def predict_next_words(self, user_input):
        words = user_input.split()
        if words:
            last_word = words[-1]
            return self.suggestions_dict.get(last_word, ["No valid prediction found."] * 2)
        return ["No valid prediction found."] * 2

    def save_history(self, user_input, predictions):
        with open('history.txt', 'a') as history_file:
            history_file.write(f"Input: {user_input}\nPredictions: {', '.join(predictions)}\n\n")

    def display_history(self):
        try:
            with open('history.txt', 'r') as history_file:
                return history_file.read() or "No history found."
        except FileNotFoundError:
            return "History file not found."

class UserAuthentication:
    def __init__(self, user_data_file='users.txt'):
        self.user_data_file = user_data_file

    def register_user(self, username, password):
        if self.check_username_exists(username):
            messagebox.showinfo("Info", "Username already exists. Choose a different username.")
            return False
        with open(self.user_data_file, 'a') as file:
            file.write(f"{username}:{password}\n")
        messagebox.showinfo("Success", "Registration successful! You can now log in.")
        return True

    def check_username_exists(self, username):
        try:
            with open(self.user_data_file, 'r') as file:
                for line in file:
                    if line.startswith(username + ":"):
                        return True
        except FileNotFoundError:
            return False
        return False

    def login(self, username, password):
        try:
            with open(self.user_data_file, 'r') as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(':')
                    if stored_username == username and stored_password == password:
                        return True
        except FileNotFoundError:
            messagebox.showerror("Error", "User data file not found.")
            return False
        return False

class PredictorApp:
    def __init__(self, root):
        self.auth = UserAuthentication()
        self.predictor = NextWordPredictor()
        self.root = root
        self.root.title("Next Word Predictor")
        self.create_login_ui()

    def create_login_ui(self):
        self.clear_window()
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        
        self.username_entry = tk.Entry(self.root)
        self.password_entry = tk.Entry(self.root, show="*")
        
        tk.Label(self.root, text="Username:").pack()
        self.username_entry.pack()
        tk.Label(self.root, text="Password:").pack()
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.handle_login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.handle_register).pack(pady=5)

    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if self.auth.login(username, password):
            messagebox.showinfo("Success", "Login successful!")
            self.create_prediction_ui()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def handle_register(self):
        username = simpledialog.askstring("Register", "Enter username:")
        password = simpledialog.askstring("Register", "Enter password:", show="*")
        if username and password:
            self.auth.register_user(username, password)

    def create_prediction_ui(self):
        self.clear_window()
        tk.Label(self.root, text="Next Word Predictor", font=("Arial", 16)).pack(pady=10)
        
        self.user_input_entry = tk.Entry(self.root, width=50)
        self.user_input_entry.pack()
        
        tk.Button(self.root, text="Predict Next Words", command=self.handle_predict).pack(pady=5)
        tk.Button(self.root, text="View History", command=self.view_history).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)  

        self.prediction_display = ScrolledText(self.root, width=40, height=10, state='disabled')
        self.prediction_display.pack(pady=10)

    def handle_predict(self):
        user_input = self.user_input_entry.get().strip()
        if not user_input:
            messagebox.showinfo("Info", "Please enter some text.")
            return

        predictions = self.predictor.predict_next_words(user_input)
        self.predictor.save_history(user_input, predictions)
        
        self.prediction_display.config(state='normal')
        self.prediction_display.insert(tk.END, f"Input: {user_input}\nPredictions: {', '.join(predictions)}\n\n")
        self.prediction_display.config(state='disabled')

    def view_history(self):
        history_content = self.predictor.display_history()
        self.prediction_display.config(state='normal')
        self.prediction_display.insert(tk.END, f"History:\n{history_content}\n\n")
        self.prediction_display.config(state='disabled')

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PredictorApp(root)
    root.mainloop()

