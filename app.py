import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog as fd

def create_messagebox():
    messagebox_window = tk.Toplevel(root)
    messagebox_window.title("Create a custom messagebox")
    messagebox_window.iconbitmap("bad-system-messages.ico")
    messagebox_window.resizable(False, False)

    title_label = ttk.Label(messagebox_window, text="Title:")
    title_label.grid(column=0, row=0, padx=5, pady=5)

    title_entry = ttk.Entry(messagebox_window, width=30)
    title_entry.grid(column=1, row=0, padx=5, pady=5)

    description_label = ttk.Label(messagebox_window, text="Description:")
    description_label.grid(column=0, row=1, padx=5, pady=5)

    description_text = tk.Text(messagebox_window, width=30, height=5)
    description_text.grid(column=1, row=1, padx=5, pady=5)

    button_type_label = ttk.Label(messagebox_window, text="Button Type:")
    button_type_label.grid(column=0, row=2, padx=5, pady=5)

    button_type_var = tk.StringVar(value="ok")
    button_type_dropdown = ttk.Combobox(messagebox_window, textvariable=button_type_var, values=("ok", "okcancel", "yesno", "retrycancel", "yesnocancel", "abortretryignore"))
    button_type_dropdown.grid(column=1, row=2, padx=5, pady=5)

    messagebox_type_label = ttk.Label(messagebox_window, text="Messagebox Type:")
    messagebox_type_label.grid(column=0, row=3, padx=5, pady=5)          
           
    messagebox_type_dropdown = ttk.Combobox(messagebox_window, values=("info", "warning", "error", "question"))
    messagebox_type_dropdown.set = "info"
    messagebox_type_dropdown.grid(column=1, row=3, padx=5, pady=5)

    messagebox_icon_label = ttk.Label(messagebox_window, text="Messagebox Icon:")
    messagebox_icon_label.grid(column=0, row=4, padx=5, pady=5)
           
    messagebox_icon_entry = ttk.Entry(messagebox_window, width=30)
    messagebox_icon_entry.grid(column=1, row=4, padx=5, pady=5)

    def browse_directory():
        # clear the icon entry
        messagebox_icon_entry.delete(0, tk.END)
        
        # open a file browser to select an icon file in .ico format
        messagebox_icon_entry.insert(0, fd.askopenfilename(initialdir="d:\\", title="Select an icon file", filetypes=(("ico files", "*.ico"), ("all files", "*.*"))))

    messagebox_icon_browse = ttk.Button(messagebox_window, text="Browse", command=browse_directory)
    messagebox_icon_browse.grid(column=2, row=4, padx=5, pady=5)

    def create_messagebox_action():
        if messagebox_icon_entry.get() != "":
            try:
                messagebox_window.iconbitmap(messagebox_icon_entry.get())
                root.iconbitmap(messagebox_icon_entry.get())
            except FileNotFoundError:
                messagebox_window.iconbitmap("bad-system-messages.ico")
                root.iconbitmap("bad-system-messages.ico")
                messagebox.showerror("Messagebox icon not found! Reverting to default (empty)")
        title = title_entry.get()
        description = description_text.get("1.0", tk.END).strip()
        button_type = button_type_var.get()

        if messagebox_type_dropdown.get() == "info":
            messagebox.showinfo(title, description, type=button_type)
        elif messagebox_type_dropdown.get() == "warning":
            messagebox.showwarning(title, description, type=button_type)            
        elif messagebox_type_dropdown.get() == "error":
            messagebox.showerror(title, description, type=button_type)            
        elif messagebox_type_dropdown.get() == "question":
            messagebox.askquestion(title, description, type=button_type)

    create_button = ttk.Button(messagebox_window, text="Create", command=create_messagebox_action)
    create_button.grid(column=0, row=5, padx=5, pady=5, columnspan=2)

root = tk.Tk()
root.title("Welcome!")
root.geometry("250x50")
root.resizable(False, False)
root.iconbitmap("bad-system-messages.ico")

create_messagebox_button = ttk.Button(root, text="Create a custom messagebox", command=create_messagebox)
create_messagebox_button.pack(padx=10, pady=10)

root.mainloop()
