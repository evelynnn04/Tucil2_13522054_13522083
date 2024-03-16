from collections import namedtuple

# Struct
Point = namedtuple('Point', ['x', 'y'])

# Input 
def input_point(point_n, list_of_point, list_of_x, list_of_y):
    while True:
        try:
            p = input(f"Silahkan masukkan koodinat x{point_n+1} dan y{point_n+1} dipisahkan spasi (dalam float) tanpa spasi di akhir: ")
            px, py = p.split(" ")
            px = float(px)
            py = float(py)
            list_of_point.append(Point(px, py))
            list_of_x.append(px)
            list_of_y.append(py)
            break
        except ValueError:
            print(f"Input invalid!")

def input_value(value_name):
    while True:
        value = input(f"Silakan masukkan banyaknya {value_name}: ")
        try:
            value = int(value)
            if value < 1:
                raise ValueError
            break
        except ValueError:
            print("Input invalid!")
    return value

# Segitiga pascal buat konstantanya 
def pascals_triangle(num_rows):
    triangle = []
    for i in range(num_rows+1):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle[len(triangle)-1]

# Brute force 
def brute_force_bezier (num_of_point, list_of_point, itr):
    list_result = []
    idx = 0
    offset = 1 / (2**itr)
    constant = pascals_triangle(num_of_point-1)
    while idx <= 1:
        value = 0
        for i in range (len(constant)):
            # print(f"{constant[i]} * ({(1-idx)}**{(num_of_point-i-1)}) * {list_of_point[i]} * {(idx**i)}")
            value += constant[i] * ((1-idx)**(num_of_point-i-1)) * list_of_point[i] * (idx**i)
            # print("hasil = ", f"{constant[i] * ((1-idx)**(num_of_point-i-1)) * list_of_point[i] * (idx**i)}")
        list_result.append(value)
        idx += offset
    return list_result

# Gabungkan x dan y 
def merge_xy(list_of_x, list_of_y):
    list_result = []
    for i in range(len(list_of_x)):
        list_result.append(Point(list_of_x[i], list_of_y[i]))
    return list_result
