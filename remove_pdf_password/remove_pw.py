import fitz  # PyMuPDF
import os
import itertools
import argparse

def remove_password(input_pdf, output_pdf, password="101010"):
    pdf_document = fitz.open(input_pdf)
    
    if pdf_document.needs_pass:
        if pdf_document.authenticate(password):
            pdf_document.save(output_pdf)
            pdf_document.close()
            print(f"Password {password} removed from {input_pdf}. Saved as {output_pdf}")
            return True  # Return True if successful
        else:
            return False  # Return False if authentication fails
    else:
        print(f"{input_pdf} is not password-protected, no password removal needed.")
        return True  # Return True if no password needed

def brute_force_password(input_pdf, output_folder):
    # Generate all possible 6-digit passwords
    possible_passwords = [f"{i:06}" for i in range(10**6)]

    for password in possible_passwords:
        output_file = input_pdf.replace("encrypted_", "").replace(".pdf", f"_pw_removed_{password}.pdf")
        if remove_password(input_pdf, output_file, password):
            break  # Break the loop if successful password removal

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove password from PDF files.")
    parser.add_argument("--input", required=True, help="Path to the PDF file or folder containing PDF files.")
    parser.add_argument("--output", default ='no_pw.pdf', help="Path to the folder where processed PDFs will be saved.")
    parser.add_argument("--password", default="101010", help="Password to be removed. If not provided, it will iterate through all 6-digit passwords.")

    args = parser.parse_args()

    if os.path.isdir(args.input):
        # If the input is a directory, iterate through all PDF files in the directory
        for pdf_file in os.listdir(args.input):
            if pdf_file.endswith(".pdf"):
                input_path = os.path.join(args.input, pdf_file)
                brute_force_password(input_path, args.output)
    else:
        # If the input is a single PDF file
        brute_force_password(args.input, args.output)
