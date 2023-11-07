import os
import nbformat
from nbconvert import PDFExporter
from nbconvert.writers import FilesWriter

# Define the relative path to the input Jupyter Notebook file
relative_path = 'ML/1_linear_reg/ML in python vs R.ipynb'

# Get the absolute path to the file based on the current working directory
script_directory = os.getcwd()
input_notebook = os.path.join(script_directory, relative_path)

# Define the output PDF file path
output_pdf = 'ML in python vs R.pdf'

# Load the Jupyter Notebook file
with open(input_notebook, 'r', encoding='utf-8') as notebook_file:
    notebook_content = nbformat.read(notebook_file, as_version=4)

# Initialize the PDF exporter
pdf_exporter = PDFExporter()

# Convert the notebook to a PDF
pdf_output, resources = pdf_exporter.from_notebook_node(notebook_content)

# Write the PDF output to a file
with open(output_pdf, 'wb') as pdf_file:
    pdf_file.write(pdf_output)

print(f'Notebook converted to PDF: {output_pdf}')
