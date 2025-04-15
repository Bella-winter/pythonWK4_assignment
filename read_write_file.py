def modify_file():
    filename = input("Enter the name of the file to read (e.g., input.txt): ")

    try:
        # Try to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = content.upper()

        # Write to a new file
        output_filename = "modified_" + filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
modify_file()
# This code is a simple file reader and writer that modifies the content of a file.
# It reads a file, converts its content to uppercase, and writes it to a new file.