import tkinter as tk
import turtle
import app
import copy

running = False

def solve():
    global running
    if running:
        return
    running = True
    solve_button.config(state=tk.DISABLED)
    t.clear()
    num_of_iteration = num_iterations_entry.get()
    num_of_point = num_points_entry.get()
    list_of_point = list_of_point_entry.get("1.0", "end")
    list_of_point = list_of_point.split(" ")
    try:
        for i in range(len(list_of_point)):
            point = list_of_point[i].split(",")  
            list_of_point[i] = [float(xy) for xy in point] 
        num_of_iteration = int(num_of_iteration)
        num_of_point = int(num_of_point)
        if num_of_iteration <= 0 or num_of_point <= 2:
            raise ValueError
        if num_of_point != len(list_of_point):
            raise ValueError
    except ValueError:
        tk.messagebox.showwarning(title="Invalid input", message="Invalid input!")
        running = False
        solve_button.config(state=tk.NORMAL)
        return
    draw_axes()
    list_step = [[[0, 0], [4, 4], [8, 4], [12, 0]], [[2.0, 2.0], [6.0, 4.0], [10.0, 2.0]], [[4.0, 3.0], [8.0, 3.0]], [[6.0, 3.0]], [[0, 0], [2.0, 2.0], [4.0, 3.0], [6.0, 3.0]], [[1.0, 1.0], [3.0, 2.5], [5.0, 3.0]], [[2.0, 1.75], [4.0, 2.75]], [[3.0, 2.25]], [[6.0, 3.0], [8.0, 3.0], [10.0, 2.0], [12, 0]], [[7.0, 3.0], [9.0, 2.5], [11.0, 1.0]], [[8.0, 2.75], [10.0, 1.75]], [[9.0, 2.25]]]
    result_dnc = app.general_iterate(num_of_point, num_of_iteration, 0, list_of_point, list_step)
    draw_bezier(list_step)
    running = False
    solve_button.config(state=tk.NORMAL)

def draw_bezier(points):
    points = [[[0, 0], [4, 4], [8, 4], [12, 0]], [[2.0, 2.0], [6.0, 4.0], [10.0, 2.0]], [[4.0, 3.0], [8.0, 3.0]], [[6.0, 3.0]], [[0, 0], [2.0, 2.0], [4.0, 3.0], [6.0, 3.0]], [[1.0, 1.0], [3.0, 2.5], [5.0, 3.0]], [[2.0, 1.75], [4.0, 2.75]], [[3.0, 2.25]], [[6.0, 3.0], [8.0, 3.0], [10.0, 2.0], [12, 0]], [[7.0, 3.0], [9.0, 2.5], [11.0, 1.0]], [[8.0, 2.75], [10.0, 1.75]], [[9.0, 2.25]]]
    t.penup()
    max_value= float('-inf')
    for sublist in points:
        for point in sublist:
            max_value= max(max_value, max(map(abs, point)))
    scaling_points = copy.deepcopy(points)
    divisor = 220 / max_value 
    for sublist in points:
        for point in sublist:
            point[0] *= divisor
            point[1] *= divisor
    draw_curve(points, scaling_points)

def draw_curve(points, scaling_points):
    t.color("grey")
    for sublist in points:
        t.penup()
        t.goto(sublist[0][0], sublist[0][1])
        t.pendown()
        for point in sublist[1:]:
            t.goto(point[0], point[1])
        t.penup()
    return

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
    t.penup()


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

label1 = tk.Label(left_frame, text="Format input: x1,y1 x2,y2 x3,y3...", bg="#2C2B30", fg="white", font=("Palatino", 10))
label2 = tk.Label(left_frame, text="Each point is split by a space", bg="#2C2B30", fg="white", font=("Palatino", 10))
label3 = tk.Label(left_frame, text="Each x and y is split by a comma", bg="#2C2B30", fg="white", font=("Palatino", 10))
label1.grid(row=7, columnspan=2)
label2.grid(row=8, columnspan=2)
label3.grid(row=9, columnspan=2)

# Turtle canvas
canvas_frame = tk.Frame(right_frame, width=600, height=600, bg="#2C2B30")
canvas_frame.pack(padx=10, pady=10)
canvas = tk.Canvas(canvas_frame, width=600, height=600, bg="#2C2B30")
canvas.pack()
screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)

root.mainloop()
