# Python File Handling Assignment

# Step 1: Creating and writing to a file
try:
    # Open a file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", 'w') as file:
        # Write three lines of text to the file
        file.write("Hello, this is the first line.\n")
        file.write("Here's the second line with a number: 123.\n")
        file.write("And finally, the third line, number: 456.\n")

    print("File has been created and written to successfully.")

    # Step 2: Reading and displaying the file contents
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\n--- Current File Contents ---")
        print(content)

    # Step 3: Appending more content to the file
    with open("my_file.txt", 'a') as file:
        file.write("This is an additional line (line 4).\n")
        file.write("Adding another line (line 5) with a number: 789.\n")
        file.write("And one more line (line 6) to wrap it up!\n")

    print("\nAdditional lines appended to the file successfully.")

    # Displaying the updated file contents
    with open("my_file.txt", 'r') as file:
        updated_content = file.read()
        print("\n--- Updated File Contents ---")
        print(updated_content)

# Step 4: Error handling
except FileNotFoundError:
    print("Error: The file you're trying to access doesn't exist.")
except PermissionError:
    print("Error: You don't have permission to modify this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling operation completed.")
