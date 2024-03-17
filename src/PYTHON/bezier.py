import app

# Inisialisasi 
list_of_point = []
list_of_x = []
list_of_y = []

# Input
print("Selamat datang di generator kurva berzier!")
itr = app.input_value("iterasi")
num_of_point = app.input_value("banyak pasangan titik")
for i in range(num_of_point):
    app.input_point(i, list_of_point, list_of_x, list_of_y)

# Solve
for point in list_of_point:
    list_of_x.append(point[0])
    list_of_y.append(point[1])
result_dnc = app.general_iterate(num_of_point, itr, 0, list_of_point)
result_dnc = app.take_result_point(result_dnc, num_of_point)
result_x = app.brute_force_bezier (num_of_point, list_of_x, itr)
result_y = app.brute_force_bezier (num_of_point, list_of_y, itr)
result_bf = app.merge_xy(result_x, result_y)
print(result_dnc)
print(result_bf)
