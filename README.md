# File Content Modifier

This Python program reads the contents of a text file, converts all the text to lowercase, and saves the modified content to a new file.

## How it Works
1. The program asks you to enter the name of an input file (e.g., `input.txt`).
2. It reads the content of that file.
3. It converts all the text to lowercase.
4. The modified content is saved to a new file named `modified_<filename>` (e.g., `modified_input.txt`).

## Example
If `input.txt` contains:
HELLO WORLD
PYTHON IS FUN

After running the program, `modified_input.txt` will contain:
hello world
python is fun

## Error Handling
- If the file does not exist, it shows an error message.
- If there are permission issues, it alerts you.
- Handles unexpected errors gracefully.