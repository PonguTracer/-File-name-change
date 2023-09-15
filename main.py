# Input file name
input_file = input("Enter the name of the input text file: ")

# Initialize a list to store the modified file names
modified_file_names = []

try:
    # Open the input text file and read photo file names
    with open(input_file, 'r') as file:
        photo_file_names = file.readlines()

    for photo_name in photo_file_names:
        # Remove leading/trailing whitespace and newline characters
        photo_name = photo_name.strip()

        # Check if the file name ends with "_photo.jpg"
        if photo_name.endswith("_photo.jpg"):
            # Replace "_photo.jpg" with "_info.txt"
            modified_name = photo_name.replace("_photo.jpg", "_info.txt")

            # Append the modified file name to the list
            modified_file_names.append(modified_name)

    # Print the modified file names to the console
    for modified_name in modified_file_names:
        print(modified_name)

    print("Modified file names have been printed to the console.")

except FileNotFoundError:
    print(f"File '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
