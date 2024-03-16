import tkinter as tk
from tkinter import messagebox

def greet():
    n = int(name_entry.get())
    if n < 3:
        messagebox.showinfo("Error", "Jumlah kontrol poin harus >= 3")
    else:
        show_entries(n)

def show_entries(n):
    for i in range(n):
        labels[i].grid(row=i, column=0)
        entry_x[i].grid(row=i, column=1)
        entry_y[i].grid(row=i, column=2)

# Create the main window
root = tk.Tk()
root.title("Tkinter with Matplotlib Graph")

# Create a frame to hold widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

frameAngka = tk.Frame(root, padx=20, pady=20)
frameAngka.pack(padx=20, pady=20)

# Create label and entry for number of points
label = tk.Label(frame, text="Masukkan jumlah kontrol poin:")
label.grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)
greet_button = tk.Button(frame, text="Calculate", command=greet)
greet_button.grid(row=0, column=2)

# Create labels and entry widgets for points
labels = []
entry_x = []
entry_y = []
for i in range(6):
    labelx = tk.Label(frameAngka, text=f"Poin {i+1}")
    labels.append(labelx)
    entry_x.append(tk.Entry(frameAngka))
    entry_y.append(tk.Entry(frameAngka))

# Run the main event loop
root.mainloop()
