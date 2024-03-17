import tkinter as tk
from tkinter import *
from tkinter import messagebox
def validasi():
    if(int(n_entry.get()) < 3):
        messagebox.showerror("Error", "Titik kontrol harus >= 3!")
    else:
        entry_vars_x.clear()
        entry_vars_y.clear()
        for i in range(int(n_entry.get())):
            add_entry()

def show_entries():
    print("x:")
    for entry_var in entry_vars_x:
        print(entry_var.get())
    print("y:")
    for entry_var in entry_vars_y:
        print(entry_var.get())

def add_entry():
    tx = "Point " + str(len(entry_vars_x)+1)
    point_label = Label(root, text=tx)
    point_label.pack()

    new_entry_var_x = tk.StringVar()
    entry_vars_x.append(new_entry_var_x)
    entry_x = tk.Entry(root, textvariable=new_entry_var_x)
    entry_x.insert(0, "x")
    entry_x.pack()
    
    new_entry_var_y = tk.StringVar()
    entry_vars_y.append(new_entry_var_y)
    entry_y = tk.Entry(root, textvariable=new_entry_var_y)
    entry_y.insert(0, "y")
    entry_y.pack()

def makeList():
    for i in range(len(entry_vars_x)):
        listPoin.append([int(entry_vars_x[i].get()),int(entry_vars_y[i].get())])

def printList():
    print(listPoin)

# program
root = tk.Tk()
root.title("Bezier")
n_label = Label(root, text="Masukkan jumlah titik kontrol :")
n_label.pack()
n = 0
n_entry = Entry(root, textvariable=n)
n_entry.pack()

check_titik_button = Button(root, text="Buat titik", command=validasi)
check_titik_button.pack()

buat_titik_button = Button(root, text="Buat list", command=makeList)
buat_titik_button.pack()

buat_titik_button = Button(root, text="tampilkan list", command=printList)
buat_titik_button.pack()


entry_vars_x = []
entry_vars_y = []

listPoin = []

# Button to trigger the action
# add_button = tk.Button(root, text="Add Entry", command=add_entry)
# add_button.pack()

# Button to show the content of all entries
show_button = tk.Button(root, text="Check titik", command=show_entries)
show_button.pack()

root.mainloop()
