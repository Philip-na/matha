import os
import tkinter as tk

class FileAgeReader:
    def __init__(self, root):
        self.root = root
        self.root.title("File Age Reader")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Main container
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(expand=True, fill='both', padx=50, pady=50)
        
        # Title
        self.title = tk.Label(
            self.main_frame,
            text="Please enter the name of the file to be read:",
            bg="#f0f0f0",
            font=('Arial', 18),
            pady=20
        )
        self.title.pack()
        
        # File entry
        self.entry = tk.Entry(
            self.main_frame,
            font=('Arial', 16),
            width=40,
            bd=2,
            relief='groove'
        )
        self.entry.pack(pady=20)
        
        # Buttons
        self.btn_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.btn_frame.pack(pady=20)
        
        self.submit_btn = tk.Button(
            self.btn_frame,
            text="Submit",
            command=self.process_file,
            font=('Arial', 14),
            width=10,
            bg="#4CAF50",
            fg="white"
        )
        self.submit_btn.pack(side='left', padx=10)
        
        self.quit_btn = tk.Button(
            self.btn_frame,
            text="Quit",
            command=root.quit,
            font=('Arial', 14),
            width=10,
            bg="#f44336",
            fg="white"
        )
        self.quit_btn.pack(side='left', padx=10)
        
        # Status display
        self.status = tk.Label(
            self.main_frame,
            text="",
            bg="#f0f0f0",
            font=('Arial', 14),
            fg="#333333"
        )
        self.status.pack(pady=10)
        
        # Result display
        self.result = tk.Label(
            self.main_frame,
            text="",
            bg="#f0f0f0",
            font=('Arial', 16),
            fg="#333333",
            wraplength=600
        )
        self.result.pack(pady=20)
    
    def process_file(self):
        filename = self.entry.get()
        if not filename:
            self.show_message("Please enter a filename first!", "red")
            return
            
        try:
            filepath = os.path.join(os.path.dirname(__file__), filename)
            
            with open(filepath, 'r') as file:
                content = file.read().strip()
                
                try:
                    age = int(content)
                    self.show_message("File read successfully!", "green")
                    self.show_result(f"Age: {age}")
                except ValueError:
                    self.show_message(f"File {filename} contains an invalid age. Try Again.", "red")
                    self.show_result("")
                    
        except FileNotFoundError:
            self.show_message(f"File {filename} not found. Try Again.", "red")
            self.show_result("")
        except PermissionError:
            self.show_message(f"Permission denied to file {filename}. Try Again.", "red")
            self.show_result("")
        except Exception as e:
            self.show_message(f"An unexpected error occurred with {filename}. Try Again.", "red")
            self.show_result("")
    
    def show_message(self, message, color):
        self.status.config(text=message, fg=color)
    
    def show_result(self, message):
        self.result.config(text=message, fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileAgeReader(root)
    root.mainloop()