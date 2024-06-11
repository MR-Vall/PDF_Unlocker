import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def check_password(input_pdf_path, password):
    try:
        with open(input_pdf_path, 'rb') as input_file:
            reader = PyPDF2.PdfReader(input_file)
            if reader.is_encrypted:
                reader.decrypt(password)
            # If we can read the first page, the password is correct
            reader.pages[0]
        return True
    except Exception as e:
        return False

def unlock_pdf(input_pdf_paths, output_dir, password, append_suffix):
    success_files = []
    for input_pdf_path in input_pdf_paths:
        try:
            with open(input_pdf_path, 'rb') as input_file:
                reader = PyPDF2.PdfReader(input_file)
                if reader.is_encrypted:
                    reader.decrypt(password)
                writer = PyPDF2.PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)

                base_name = os.path.basename(input_pdf_path)
                if append_suffix:
                    base_name = os.path.splitext(base_name)[0] + "_oplåst.pdf"
                output_pdf_path = os.path.join(output_dir, base_name)
                with open(output_pdf_path, 'wb') as output_file:
                    writer.write(output_file)

                success_files.append(base_name)
        except Exception as e:
            messagebox.showerror("Fejl", f"Kunne ikke låse {input_pdf_path} op. Fejl: {e}")
    
    if success_files:
        success_message = "Låste op og gemte følgende filer:\n" + "\n".join(success_files)
        messagebox.showinfo("Succes", success_message)

def browse_input_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF-filer", "*.pdf")])
    if file_paths:
        file_names = [os.path.basename(path) for path in file_paths]
        input_entry.delete(0, tk.END)
        input_entry.insert(0, "; ".join(file_names))
        input_entry_paths.set("; ".join(file_paths))

def browse_output_directory():
    directory = filedialog.askdirectory()
    if directory:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, directory)

def unlock_pdf_action():
    input_pdf_paths = input_entry_paths.get().split("; ")
    output_dir = output_entry.get()
    password = password_entry.get()
    append_suffix = append_suffix_var.get()
    if input_pdf_paths and output_dir and password:
        if check_password(input_pdf_paths[0], password):
            unlock_pdf(input_pdf_paths, output_dir, password, append_suffix)
        else:
            messagebox.showerror("Fejl", "Adgangskoden er forkert.")
    else:
        messagebox.showwarning("Input Fejl", "Angiv alle nødvendige input")

# Setting up the main application window
app = tk.Tk()
app.title("PDF Oplåser")
app.configure(bg='#f0f0f0')  # Light gray background

# Styling
style = ttk.Style()
style.configure("TCheckbutton", font=('Arial', 12), background='#f0f0f0', foreground='#333333')

label_font = ('Arial', 12)
entry_font = ('Arial', 12)
button_font = ('Arial', 12, 'bold')
button_bg = '#007acc'  # Light blue
button_fg = '#ffffff'  # White text
entry_bg = '#ffffff'  # White entry fields
entry_fg = '#000000'  # Black text

# Variable to store full paths of selected input files
input_entry_paths = tk.StringVar()
append_suffix_var = tk.BooleanVar()

# Input PDF file selection
tk.Label(app, text="Input PDF-filer:", bg='#f0f0f0', fg='#333333', font=label_font).grid(row=0, column=0, padx=10, pady=10, sticky='e')
input_entry = tk.Entry(app, width=50, bg=entry_bg, fg=entry_fg, font=entry_font)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Gennemse", command=browse_input_files, bg=button_bg, fg=button_fg, font=button_font).grid(row=0, column=2, padx=10, pady=10)

# Output directory selection
tk.Label(app, text="Gem mappe:", bg='#f0f0f0', fg='#333333', font=label_font).grid(row=1, column=0, padx=10, pady=10, sticky='e')
output_entry = tk.Entry(app, width=50, bg=entry_bg, fg=entry_fg, font=entry_font)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Gennemse", command=browse_output_directory, bg=button_bg, fg=button_fg, font=button_font).grid(row=1, column=2, padx=10, pady=10)

# Password entry
tk.Label(app, text="Adgangskode:", bg='#f0f0f0', fg='#333333', font=label_font).grid(row=2, column=0, padx=10, pady=10, sticky='e')
password_entry = tk.Entry(app, show="*", width=50, bg=entry_bg, fg=entry_fg, font=entry_font)
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Checkbox for appending "oplåst" suffix
append_suffix_checkbox = ttk.Checkbutton(app, text="Tilføj 'oplåst' til filnavnet", variable=append_suffix_var, style="TCheckbutton")
append_suffix_checkbox.grid(row=3, column=0, columnspan=3, pady=10)

# Unlock PDF button
tk.Button(app, text="Lås PDF op", command=unlock_pdf_action, bg=button_bg, fg=button_fg, font=button_font).grid(row=4, column=0, columnspan=3, pady=20)

app.mainloop()
