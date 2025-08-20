def modify_content (content):
    """
    This function modifies the content by converting text to lowercase.
    
    """
    return content.lower()

def main():
    try:
        # Prompt user for input file name
        input_file = input("Enter the name of the input file: ").strip()
        
        # Read the content of the file
        with open(input_file, 'r') as file:
            content = file.read()
            modified_content = modify_content(content)

        # Save the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)
            
        print(f"SUCCESSFUL!! Content modified and saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read or write to the file '{input_file}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred. {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()      