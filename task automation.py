import os

def automate_task():
    try:
        # Prompt the user for the directory path
        directory_path = input("Enter the directory path: ")

        # Change to the specified directory
        os.chdir(directory_path)

        # List all files in the directory
        files = os.listdir()

        # Print the list of files
        print("Files in the directory:")
        for file in files:
            print(file)

        # Add your automation logic here

    except Exception as e:
        print(f"Error: {e}")

# Call the function to start the automation
automate_task()