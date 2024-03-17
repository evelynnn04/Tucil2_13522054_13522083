import tkinter as tk
import turtle

def solve():
    draw_axes()
    draw_bezier()
    num_iterations = num_iterations_entry.get()
    num_points = num_points_entry.get()
    list_of_point = list_of_point.get()
    list_of_point = list_of_point.splitby(",")
    list_of_point = list_of_point.splitby(" ")
    try:
        num_iterations = int(num_iterations)
        num_points = int(num_points)
        list_of_point = float(list_of_point)
        if num_iterations <= 2 or num_points <= 2:
            raise ValueError
    except ValueError:
        tk.messagebox.showwarning(title="Invalid input", message="Input invalid!")
        return

def draw_bezier():
    list_result = [[90,7], [0,8], [9,4000], [3,4]]
    draw_curve(list_result)

def draw_curve(points):
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    t.color("grey")
    for i in range(1, len(points)):
        t.goto(points[i][0], points[i][1])

def draw_axes():
    t.color("lightgrey")
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.goto(300, 0)
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.goto(0, 300)

# Initialization
root = tk.Tk()
root.title("Bezier Graphic")
root.configure(bg="#2C2B30")

# Fix size
root.geometry("920x600")
root.resizable(False, False)

# Left side
left_frame = tk.Frame(root, bg="#2C2B30", padx=10, pady=10) 
left_frame.pack(side=tk.LEFT)

# Right side
right_frame = tk.Frame(root, bg="#2C2B30", padx=10, pady=10)
right_frame.pack(side=tk.LEFT)  

left_frame.grid_columnconfigure(1, weight=1)  
right_frame.grid_columnconfigure(0, weight=2) 

# Num of point
num_points_label = tk.Label(left_frame, text="Number of Points:", bg="#2C2B30", fg="white", font=("Palatino", 10))
num_points_label.grid(row=0, column=0, pady=10, padx=30) 
num_points_entry = tk.Entry(left_frame, width=15)
num_points_entry.grid(row=0, column=1, padx=5, pady=5) 

# Num of iteration
num_iterations_label = tk.Label(left_frame, text="Number of Iterations:", bg="#2C2B30", fg="white", font=("Palatino", 10))
num_iterations_label.grid(row=1, column=0, pady=10) 
num_iterations_entry = tk.Entry(left_frame, width=15) 
num_iterations_entry.grid(row=1, column=1, padx=5, pady=5)

# List of point
list_of_point = tk.Label(left_frame, text="List of Points:", bg="#2C2B30", fg="white", font=("Palatino", 10))
list_of_point.grid(row=2, column=0, pady=10, columnspan=2) 
list_of_point_entry = tk.Text(left_frame, width=25, height=3)
list_of_point_entry.grid(row=3, column=0, columnspan=2, pady=5)  

# Solve button
solve_button = tk.Button(left_frame, text="Solve", command=solve, bg="lightblue", font=("Palatino", 10), width=6, height=1)
solve_button.grid(row=6, columnspan=2, pady=15)

# Turtle canvas
canvas_frame = tk.Frame(right_frame, width=600, height=600, bg="#2C2B30")
canvas_frame.pack(padx=10, pady=10)
canvas = tk.Canvas(canvas_frame, width=600, height=600, bg="#2C2B30")
canvas.pack()
screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)

root.mainloop()
