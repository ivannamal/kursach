# import tkinter as tk
# from tkinter import filedialog, messagebox
# import subprocess
# import os
#
#
# def browse_input_file():
#     file_path = filedialog.askopenfilename(filetypes=[("Ttarch2 Files", "*.ttarch2")])
#     if file_path:
#         input_var.set(file_path)
#
#
# def browse_output_folder():
#     folder_path = filedialog.askdirectory()
#     if folder_path:
#         output_var.set(folder_path)
#
#
# def run_extraction():
#     input_path = input_var.get()
#     output_path = output_var.get()
#
#     if not input_path or not output_path:
#         messagebox.showwarning("Missing info", "Please select both input file and output folder.")
#         return
#
#     if not os.path.exists(r"ttarchext\ttarchext.exe"):
#         messagebox.showerror("Missing tool", "ttarchext.exe not found in script folder.")
#         return
#
#     try:
#         ttarchext_path = r"ttarchext\ttarchext.exe"
#         subprocess.run([ttarchext_path, "54", input_path, output_path], check=True)
#         messagebox.showinfo("Done", "Extraction completed successfully.")
#     except subprocess.CalledProcessError as e:
#         messagebox.showerror("Error", f"Extraction failed.\n{e}")
#
#
# # --- GUI ---
# root = tk.Tk()
# root.title("TTARCH Extractor GUI")
#
# input_var = tk.StringVar()
# output_var = tk.StringVar()
#
# tk.Label(root, text="Select .ttarch2 file:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
# tk.Entry(root, textvariable=input_var, width=60).grid(row=0, column=1, padx=10)
# tk.Button(root, text="Browse", command=browse_input_file).grid(row=0, column=2, padx=10)
#
# tk.Label(root, text="Select output folder:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
# tk.Entry(root, textvariable=output_var, width=60).grid(row=1, column=1, padx=10)
# tk.Button(root, text="Browse", command=browse_output_folder).grid(row=1, column=2, padx=10)
#
# tk.Button(root, text="Extract", command=run_extraction, bg="#4CAF50", fg="white", height=2).grid(row=2, column=0,
#                                                                                                  columnspan=3, pady=20)
#
# root.mainloop()
