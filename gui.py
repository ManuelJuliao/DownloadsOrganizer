import tkinter as tk
from tkinter import filedialog
from files_org import organizeDir

def browse_folder():
    folder_path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, folder_path)

def organize():
    folder_path = entry_path.get()
    organizeDir(folder_path)

def close_app():
    root.destroy()    

root = tk.Tk()
root.title("File Organizer")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_path = tk.Label(frame, text="Folder Path:")
label_path.grid(row=0, column=0)

entry_path = tk.Entry(frame, width=50)
entry_path.grid(row=0, column=1)

button_browse = tk.Button(frame, text="Browse", command=browse_folder)
button_browse.grid(row=0, column=2)

button_organize = tk.Button(frame, text="Organize Files", command=organize)
button_organize.grid(row=1, columnspan=3, pady=10)

button_close = tk.Button(frame, text="Close", command=close_app)
button_close.grid(row=2, columnspan=3, pady=10)

root.mainloop()
