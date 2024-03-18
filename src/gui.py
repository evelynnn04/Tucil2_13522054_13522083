import tkinter as tk
import turtle
import app
import copy

running = False
global multiplier

def solve():
    global running
    if running:
        return
    running = True
    solve_button.config(state=tk.DISABLED)
    pass
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
    list_step = []
    result_dnc = app.general_iterate(num_of_point, num_of_iteration, 0, list_of_point, list_step)
    result_dnc = app.take_result_point(result_dnc, num_of_point)
    draw_bezier(list_step)
    draw_bezier_final(result_dnc)
    tk.messagebox.showinfo(title="Points info", message=result_dnc)
    running = False
    solve_button.config(state=tk.NORMAL)

def add_scrollbar(content):
    scrollbar_frame = tk.Frame(left_frame)
    scrollbar_frame.grid(row=7, column=0, columnspan=2, rowspan=3, pady=5)
    scrollbar = tk.Scrollbar(scrollbar_frame, orient="vertical", bg="white", fg="black", font=("Palatino", 10))
    scrollbar.grid(row=0, column=1, sticky="ns")
    text_widget = tk.Text(scrollbar_frame, width=25, height=5, yscrollcommand=scrollbar.set)
    text_widget.grid(row=0, column=0)
    scrollbar.config(command=text_widget.yview)
    for item in content:
        text_widget.insert(tk.END, item + "\n")

def draw_bezier(points):
    t.penup()
    max_value = 0
    for sublist in points:
        for point in sublist:
            for xy in point:
                max_value= max(max_value, abs(xy))
    global multiplier 
    multiplier = 220 / max_value
    if (multiplier > 1):
        multiplier = 220 // max_value
    
    scaling_points = []
    for sublist1 in points:
        multiplied_sublist1 = []
        for sublist2 in sublist1:
            multiplied_sublist2 = []
            for value in sublist2:
                multiplied_sublist2.append(value * multiplier)
            multiplied_sublist1.append(multiplied_sublist2)
        scaling_points.append(multiplied_sublist1)
    draw_axes(multiplier)
    draw_curve(points, scaling_points)

def draw_curve(points, scaling_points):
    t.color("#219EBC")
    for sublist in scaling_points:
        t.penup()
        t.goto(sublist[0][0], sublist[0][1])
        t.pendown()
        for point in sublist[1:]:
            t.goto(point[0], point[1])
        t.penup()
    return

def draw_bezier_final(points):
    scaling_points = copy.deepcopy(points)
    for i in range(len(points)):
        scaling_points[i][0] *= multiplier
        scaling_points[i][1] *= multiplier
    draw_curve_final(points, scaling_points)

def draw_curve_final(points, scaling_points):
    t.penup()
    t.goto(scaling_points[0][0], scaling_points[0][1])
    t.color("black")
    t.pendown()
    for point in scaling_points:
        t.goto(point[0], point[1])
        if (point == scaling_points[0]):
            if (points[0][0] < 0):
                t.write(f"({points[0][0]}, {points[0][1]})", align="left")
            else:
                t.write(f"({points[0][0]}, {points[0][1]})", align="right")
        if (point == scaling_points[-1]):
            if (points[-1][0] < 0):
                t.write(f"({points[-1][0]}, {points[-1][1]})", align="left")
            else:
                t.write(f"({points[-1][0]}, {points[-1][1]})", align="right")

def draw_axes(multiplier):
    t.color("lightgrey")
    t.penup()
    t.goto(-canvas.winfo_width() / 2, 0)
    t.pendown()
    t.goto(canvas.winfo_width() / 2, 0)
    t.penup()
    t.goto(0, -canvas.winfo_height() / 2)
    t.pendown()
    t.goto(0, canvas.winfo_height() / 2)
    t.penup()

    x = -200
    while x < 201:
        t.goto(x, -5)
        t.pendown()
        t.goto(x, 5)
        t.penup()
        t.goto(x, -20)
        t.write(str(round(x / multiplier, 1)), align="center")  
        x += 50

    y = -200
    while y < 201:
        t.goto(-5, y)
        t.pendown()
        t.goto(5, y)
        t.penup()
        t.goto(-20, y)
        t.write(str(round((y / multiplier), 1)), align="right") 
        y += 50

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
canvas = tk.Canvas(canvas_frame, width=500, height=500, bg="#2C2B30")
canvas.pack()
screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)

root.mainloop()
