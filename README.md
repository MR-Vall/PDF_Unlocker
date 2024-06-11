# PDF Decrypt

Welcome to the PDF Decrypt repository! This repository contains a script to decrypt PDF files and is organized into two branches:

1. **Script**: Contains the raw Python script.
2. **Zip_Version**: Contains the Python script packaged into a ZIP file with a batch file for easy execution.

**Note:** This program is made for Danish users and does not have an English version.

## Branches

### Script Branch

The `Script` branch contains the raw Python script (`Script.py`).

#### How to Use

1. **Clone or Download the Repository**:
   - Go to the [Script branch](https://github.com/MR-Vall/PDF_Unlocker/tree/Script).
   - Click the "Code" button and download the ZIP file or clone the repository using:
     ```bash
     git clone https://github.com/your-username/PDF_Decrypt.git
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

### Zip_Version Branch

The `Zip_Version` branch contains the script packaged in a ZIP file along with a batch file for easy execution.

#### How to Use

1. **Download the ZIP File**:
   - Go to the [Zip_Version branch](https://github.com/MR-Vall/PDF_Unlocker/tree/Zip_Version).
   - Click the "Code" button and download the ZIP file.

2. **Extract the ZIP File**:
   - Extract the downloaded ZIP file to a convenient location on your computer.

3. **Run the Script**:
   - Open the extracted folder.
   - Double-click on `run_script.bat` to run the script.

## Creating an Executable (Optional)

If you want to create a standalone executable from the `Script` branch:

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
