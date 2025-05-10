import os  # Import the os module for file path operations

# Define the my_file_reader function to read and validate age files
def my_file_reader():
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
                
                # Try to convert content to an integer (age validation)
                try:
                    age = int(content)
                    # If successful, print the age and break out of the loop
                    print(f"Age: {age}")
                    break # Force the program to jump out of the loop
                # Handle case where content is not a valid integer
                except ValueError:
                    print(f"File {filename} contains an invalid age.")
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
my_file_reader()