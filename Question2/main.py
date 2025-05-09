import os  # Import the os module for file path operations

# Define the main function to read and validate salary files
def main():
    # Start an infinite loop to keep the program running until valid input is received
    while True:
        # Begin try-except block to handle potential errors
        try:
            # Asking the user to enter the filename
            filename = input("Please enter the name of the file to be read: ")
            
            # Construct the full file path by joining the current directory with the filename
            filepath = os.path.join(os.path.dirname(__file__), filename)
            
            # Attempt to open and read the file
            with open(filepath, 'r') as file:
                # Read file content and remove any leading/trailing whitespace
                content = file.read().strip()
                
                # Try to convert content to an integer (salary validation)
                try:
                    salary = int(content)
                    # If successful, print the salary and break out of the loop
                    print(f"Salary: ${salary}")
                    print("Thank you for using our program")
                    break # Force the program to jump out of the loop
                # Handle case where content is not a valid integer
                except ValueError:
                    print(f"File {filename} contains an invalid selary.")
                    print("Try Again")
                    
        # Handle case where file doesn't exist
        except FileNotFoundError:
            print(f"File {filename} not found.")
            print("Try Again")
        # Handle case where program doesn't have permission to access file
        except PermissionError:
            print(f"Permission denied to file {filename}.")
            print("Try Again")
        # Catch any other unexpected errors
        except Exception as e:
            print(f"unexpected error occurred on: {filename}.")
            print("Try Again")

# Call the function to start the program
main()