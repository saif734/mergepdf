from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()

if __name__ == "__main__":
    print("Enter PDF file paths separated by comma:")
    files = input().split(",")

    files = [f.strip() for f in files]

    output = input("Enter output PDF file name: ")

    merge_pdfs(files, output)

    print("PDFs merged successfully!")
