import sys
import os
from pypdf_reader import process_pdf
from openai_to_process_txt import format_text


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <pdf_file_path>")
        sys.exit(1)

    # Get the PDF file path from the command line argument
    pdf_file_path = sys.argv[1]

    # Check if the provided file exists
    if not os.path.isfile(pdf_file_path):
        print(f"Error: File '{pdf_file_path}' not found.")
        sys.exit(1)

    # Process the PDF using pypdf_reader.py
    output_text = process_pdf(pdf_file_path)

    # Format the output text
    formatted_output = format_text(output_text)

    # Print the formatted text
    print(formatted_output)

    # Determine the output file path (in the same folder with a .txt extension)
    output_file_path = os.path.splitext(pdf_file_path)[0] + ".txt"

    # Save the processed text to the output file
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(formatted_output)

    print(f"Text extracted and saved to '{output_file_path}'")


if __name__ == "__main__":
    main()
