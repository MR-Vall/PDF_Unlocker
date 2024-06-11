### Script Branch README

```markdown
# PDF Decrypt - Script Branch

This branch contains the raw Python script to decrypt PDF files.

**Note:** This program is made for Danish users and does not have an English version.

## Functions

- **unlock_pdf(input_pdf_paths, output_dir, password, append_suffix)**: Unlocks and saves PDF files without password protection.
  - `input_pdf_paths`: List of paths to the input PDF files.
  - `output_dir`: Directory where the unlocked PDFs will be saved.
  - `password`: Password for the PDF files.
  - `append_suffix`: Boolean to determine if "_oplåst" should be appended to the file names.

- **browse_input_files()**: Opens a file dialog to select input PDF files.

- **browse_output_directory()**: Opens a file dialog to select the output directory.

- **unlock_pdf_action()**: Main function that validates inputs, checks the password, and calls `unlock_pdf`.

## How to Use

1. **Clone or Download the Repository**:
   - Go to the [Script branch](https://github.com/MR-Vall/PDF_Unlocker/tree/Script).
   - Click the "Code" button and download the ZIP file or clone the repository using:
     ```bash
     git clone https://github.com/MR-Vall/PDF_Decrypt.git
     cd PDF_Decrypt
     git checkout Script
     ```

2. **Install Requirements**:
   - Make sure you have Python 3.10 or later installed.
   - Install the required library:
     ```bash
     pip install PyPDF2
     ```

3. **Run the Script**:
   - Execute the script using the command:
     ```bash
     python Script.py
     ```

## Creating an Executable (Optional)

If you want to create a standalone executable:

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
