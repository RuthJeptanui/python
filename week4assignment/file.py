
def read_write_file():
    try:
        #ask user to input file name
        file_name = input("Enter the name of the file to read:")

        #open file for reading
        with open (file_name, 'r') as myfile:
            content = myfile.read()

        #modifying content of the file
        modified_content = content.upper()

        #creating a file whre modified content wil  be stored
        modified_file = "modified_" + file_name
        with open (modified_file, 'w') as myfile:
            myfile.write(modified_content)
        print(f"Modified content written to {modified_file}")

        #error handling
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")  
    except PermissionError:
        print("You dont have the permission to access this file.")
    except Exception as e:
        print("An error occurred:", e)


#call the function
read_write_file()
