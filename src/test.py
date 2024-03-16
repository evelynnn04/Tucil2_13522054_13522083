import tkinter as tk

def toggle_visibility():
    if hidden.get():
        widget.pack_forget()
        toggle_button.config(text="Show Widget")
    else:
        widget.pack()
        toggle_button.config(text="Hide Widget")
    hidden.set(not hidden.get())

# Create the main window
root = tk.Tk()
root.title("Toggle Widget Visibility")

# Create a frame to hold widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Create a widget to hide/unhide
widget = tk.Label(frame, text="This is a hidden widget")
widget.pack()

# Create a button to toggle visibility
hidden = tk.BooleanVar()
toggle_button = tk.Button(frame, text="Hide Widget", command=toggle_visibility)
toggle_button.pack(pady=10)

# Run the main event loop
root.mainloop()
