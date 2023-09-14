import pdfplumber

# Define the PDF file path
pdf_file_path = 'example.pdf'

# Create a PDFplumber PDF object
with pdfplumber.open(pdf_file_path) as pdf:
    # Initialize an empty text variable to store extracted text
    text = ''

    # Loop through each page and extract text
    for page in pdf.pages:
        text += page.extract_text()

# Define the output text file path
text_file_path = 'output.txt'

# Write the extracted text to a plain text file
with open(text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(text)

print(f'Text extracted from PDF and saved to {text_file_path}')
