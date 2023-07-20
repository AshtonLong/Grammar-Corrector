# Grammar Correction Program

This is a Python program that uses OpenAI's GPT-3.5-turbo model to correct the grammar in a given text. The program reads a text from an input file, sends it to the GPT-3.5-turbo model for grammar correction, and writes the corrected text to an output file.

## Dependencies

This program requires the `openai` Python package. You can install it using pip:

```
pip install openai
```

## Setup

Before running the program, you need to set up your OpenAI API key. The program expects to find the key in a file named `api_key.txt` in the same directory. You can obtain an API key by creating an account on the [OpenAI website](https://www.openai.com/).

## Usage

To use the program, you need to provide a text file named `input.txt` in the same directory. This file should contain the text you want to correct. The program will read this file, correct the grammar, and write the corrected text to a file named `output.txt` in the same directory.

To run the program, simply execute the Python script:

```
python script_name.py
```

Replace `script_name.py` with the actual name of the script.

## Functions

The program contains the following functions:

- `correct_grammar(text)`: This function takes a string as input and returns the corrected text. It sends the text to the GPT-3.5-turbo model and retrieves the corrected text. If an error occurs during this process, the function prints the error message and exits the program.

- `get_text()`: This function reads the `input.txt` file and returns its content as a string. If the file is not found or an error occurs while reading the file, the function prints an error message and exits the program.

- `write_text(corrected_text)`: This function takes a string as input and writes it to the `output.txt` file. If an error occurs while writing to the file, the function prints the error message and exits the program.

- `main()`: This is the main function of the program. It calls the other functions to read the input text, correct the grammar, and write the corrected text to the output file.

## Error Handling

The program includes basic error handling. If an error occurs while reading or writing files, or while correcting the grammar, the program prints an error message and exits with a status code of 1.
