def file_read_write():
    try:
        
        filename = input("Enter the name of the file to read: ")

        
        with open(filename, "r") as file:
            content = file.read()

       
        modified_content = content.upper()

        
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified file has been saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")



file_read_write()
