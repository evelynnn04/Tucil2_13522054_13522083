import app
import time

# Inisialisasi 
start = time.time()
list_of_point = []
list_of_x = []
list_of_y = []

# Input
print("Selamat datang di generator kurva berzier!")
itr = app.input_value("iterasi")
num_of_point = app.input_value("banyak pasangan titik")
for i in range(num_of_point):
    app.input_point(i, list_of_point, list_of_x, list_of_y)

list_of_x = [238.0, 312.8, 374.0, 442.0]
list_of_y = [680.0, 0.0, 0.0, 680.0]

# Solve 
result_x = app.brute_force_bezier (num_of_point, list_of_x, itr)
result_y = app.brute_force_bezier (num_of_point, list_of_y, itr)
list_result = app.merge_xy(result_x, result_y)
print(list_result)

# Time End 
end = time.time()

# Print Time
print("Runtime:", (end-start) * 10**3, "ms")