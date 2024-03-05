import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Test Case Generator")

# Yüklenen dosyanın yolu
uploaded_file = ''

def upload_file():
    global uploaded_file
    uploaded_file = filedialog.askopenfilename(initialdir="/", title="Select File",
                                               filetypes=(("PowerPoint files", "*.pptx"),
                                                          ("PDF files", "*.pdf"),
                                                          ("Word files", "*.docx"),
                                                          ("all files", "*.*")))
    if uploaded_file:
        uploaded_label.config(text=f"Uploaded: {os.path.basename(uploaded_file)}")
    else:
        uploaded_label.config(text="No file selected.")

def generate_test_cases():
    if uploaded_file:
        # Dosya yüklendiyse test durumları üretme fonksiyonunu burada çağır
        pass
    else:
        # Dosya yüklenmediyse kullanıcıyı uyar
        pass

canvas = tk.Canvas(root, height=400, width=600)
canvas.pack()

upload_btn = tk.Button(root, text="Upload File", padx=10, pady=5, fg="white", bg="#263D42", command=upload_file)
upload_btn.pack()

run_btn = tk.Button(root, text="Execute", padx=10, pady=5, fg="white", bg="#263D42", command=generate_test_cases)
run_btn.pack()

uploaded_label = tk.Label(root, text="No file selected.", bg="gray")
uploaded_label.pack()

root.mainloop()
