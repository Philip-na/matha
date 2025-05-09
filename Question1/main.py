import os
import tkinter as tk
from tkinter import messagebox, simpledialog

def my_file_reader_gui():
    root = tk.Tk()
    root.withdraw()  # Hide the main window (we only need popups)

    while True:
        try:
            # Ask for filename using a GUI dialog instead of console input
            filename = simpledialog.askstring(
                "File Input",
                "Please enter the name of the file to be read:",
                parent=root
            )
            
            if filename is None:  # User pressed "Cancel"
                break  # Exit the loop
            
            filepath = os.path.join(os.path.dirname(__file__), filename)
            
            with open(filepath, 'r') as file:
                content = file.read().strip()
                
                try:
                    age = int(content)
                    messagebox.showinfo("Success", f"Age: {age}")
                    break  # Exit on success
                except ValueError:
                    messagebox.showerror(
                        "Error",
                        f"File '{filename}' contains an invalid age.\nTry Again."
                    )
                    
        except FileNotFoundError:
            messagebox.showerror(
                "Error",
                f"File '{filename}' not found.\nTry Again."
            )
        except PermissionError:
            messagebox.showerror(
                "Error",
                f"Permission denied to file '{filename}'.\nTry Again."
            )
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An unexpected error occurred with '{filename}'.\nTry Again."
            )

    root.destroy()  # Close the hidden Tkinter window

if __name__ == "__main__":
    my_file_reader_gui()