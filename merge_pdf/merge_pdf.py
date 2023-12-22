import os
import argparse
from PyPDF2 import PdfMerger

def merge_pdfs(input_folder, output_file="merged.pdf"):
    # Get a list of all PDF files in the specified folder
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]

    # Sort the PDF files to ensure a specific order, if needed
    pdf_files.sort()

    # Initialize a PdfMerger object
    pdf_merger = PdfMerger()

    # Add all PDF files to the merger
    for pdf_file in pdf_files:
        pdf_file_path = os.path.join(input_folder, pdf_file)
        pdf_merger.append(pdf_file_path)

    # Output merged PDF to the specified file
    pdf_merger.write(output_file)
    pdf_merger.close()

    print(f"Merged {len(pdf_files)} PDF files into {output_file}")

if __name__ == "__main__":
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description="Merge PDF files in a specified folder.")
    parser.add_argument("input_folder", help="Path to the folder containing PDF files to be merged.")
    parser.add_argument("-o", "--output", default="merged.pdf", help="Output file name for the merged PDF (default: merged.pdf)")

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the merge_pdfs function with the specified arguments
    merge_pdfs(args.input_folder, args.output)
