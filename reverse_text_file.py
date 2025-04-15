def reverse_file_text():
    filename = input("Enter the name of the file to read (e.g., input.txt): ")

    try:
        # Try to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Reverse the entire text
        modified_content = content[::-1]

        # Save the result to a new file
        output_filename = "reversed_" + filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"The reversed text has been saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
reverse_file_text()