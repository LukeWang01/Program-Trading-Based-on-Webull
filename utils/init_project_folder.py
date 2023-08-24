import os


# Test only
def create_secrete_file():
    folder_name = "env"
    file_name = "_secrete.py"
    # Check if the folder exists
    if not os.path.exists(folder_name):
        # Create the folder if it doesn't exist
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")

    # Create the Python file inside the folder
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as file:
        # Write some content to the file
        file.write("# My Python file")

    print(f"File '{file_name}' created under folder '{folder_name}' successfully.")
