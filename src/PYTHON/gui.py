import tkinter as tk
from tkinter import messagebox
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_graph(points, iterations):
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def animate(i):
        ax.clear()
        ax.axhline(0, color='black')
        ax.axvline(0, color='black')
        
        for point in points:
            ax.plot(point[0], point[1], 'ro')
        
        for i in range(iterations):
            ax.plot([0, i], [0, i], 'b-')

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    root.mainloop()

def submit_inputs():
    # Validate number of points and iterations
    try:
        num_points = int(num_points_entry.get())
        num_iterations = int(num_iterations_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Number of points and iterations must be integers.")
        return
    
    # Validate points format
    points_str = list_of_points_entry.get()
    points_list = re.findall(r'(\d+(\.\d+)?),(\d+(\.\d+)?)', points_str)
    if len(points_list) != num_points:
        messagebox.showerror("Error", "Number of points in the list does not match the specified number of points.")
        return
    
    points = [(float(x), float(y)) for x, _, y, _ in points_list]
    draw_graph(points, num_iterations)

root = tk.Tk()
root.title("Cartesian Graph")

# Number of points input
num_points_label = tk.Label(root, text="Enter the number of points: ")
num_points_label.grid(row=0, column=0, padx=10, pady=5)
num_points_entry = tk.Entry(root)
num_points_entry.grid(row=0, column=1, padx=10, pady=5)

# Number of iterations input
num_iterations_label = tk.Label(root, text="Enter the number of iterations: ")
num_iterations_label.grid(row=1, column=0, padx=10, pady=5)
num_iterations_entry = tk.Entry(root)
num_iterations_entry.grid(row=1, column=1, padx=10, pady=5)

# List of points input
list_of_points_label = tk.Label(root, text="Enter the list of points (x1,y1; x2,y2; ...): ")
list_of_points_label.grid(row=2, column=0, padx=10, pady=5)
list_of_points_entry = tk.Entry(root)
list_of_points_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_inputs)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
