import PyPDF2


def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store extracted text
        extracted_text = ""

        # Loop through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the page object
            page = pdf_reader.pages[page_num]

            # Extract text from the page
            page_text = page.extract_text()

            # Append extracted text to the result string
            extracted_text += page_text

    return extracted_text


# Example usage:
pdf_path = '/Users/Richard/Library/Mobile Documents/com~apple~CloudDocs/_Studium/_LFU/5.Semester/Psychologie/Praxis/3_Praxisbestaetigung.pdf'  # Replace 'example.pdf' with the path to your PDF file
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)
