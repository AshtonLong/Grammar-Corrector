import openai
import sys

openai.api_key = open("api_key.txt", "r").read()

def correct_grammar(text):
    try:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {
            "role": "system",
            "content": "You will correct the grammar in any text given to you."
            },
            {
            "role": "user",
            "content": f"{text}"
            }
        ],
        temperature=0,
        max_tokens=2048
        )
        
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error occurred while correcting grammar: {e}")
        sys.exit(1)

def get_text():
    try:
        with open("input.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        print("input.txt file not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")
        sys.exit(1)

def write_text(corrected_text):
    try:
        with open("output.txt", "w") as file:
            file.write(corrected_text)
    except Exception as e:
        print(f"Error occurred while writing to the file: {e}")
        sys.exit(1)

def main():
    text = get_text()
    corrected_text = correct_grammar(text)
    write_text(corrected_text)

if __name__ == "__main__":
    main()
