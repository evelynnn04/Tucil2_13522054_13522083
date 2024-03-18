import matplotlib.pyplot as plt

# Input 
def input_point(point_n, list_of_point, list_of_x, list_of_y):
    while True:
        try:
            p = input(f"Silahkan masukkan koodinat x{point_n+1} dan y{point_n+1} dipisahkan spasi (dalam float) tanpa spasi di akhir: ")
            px, py = p.split(" ")
            px = float(px)
            py = float(py)
            list_of_point.append([px, py])
            list_of_x.append(px)
            list_of_y.append(py)
            break
        except ValueError:
            print(f"Input invalid!")

def input_value(value_name, min):
    while True:
        value = input(f"Silakan masukkan banyaknya {value_name}: ")
        try:
            value = int(value)
            if value < min:
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
            value += constant[i] * ((1-idx)**(num_of_point-i-1)) * list_of_point[i] * (idx**i)
        list_result.append(value)
        idx += offset
    return list_result

# Brute force 3 titik
def brute_force_3titik (list_of_point, itr):
    list_result = []
    idx = 0
    offset = 1 / (2**itr)
    constant = [1, 2, 1]
    while idx <= 1:
        value = 0
        for i in range (3):
            value += constant[i] * ((1-idx)**(2-i)) * list_of_point[i] * (idx**i)
        list_result.append(value)
        idx += offset
    return list_result

# Gabungkan x dan y 
def merge_xy(list_of_x, list_of_y):
    list_result = []
    for i in range(len(list_of_x)):
        list_result.append([list_of_x[i], list_of_y[i]])
    return list_result

def midPoint(p1,p2):
    return [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]

def wide(i,list,f):
    temp = list
    temp.insert(0,i)
    temp.append(f)
    return temp

def base_iterate(n, list, listProses):
    if(n == 1):
        listProses.append([list[len(list)//2]])
        return list
    else:
        temp = []
        listProses.append(list)
        for i in range(n-1):
            temp.append(midPoint(list[i],list[i+1]))
        return wide(list[0],base_iterate(n-1,temp,listProses),list[-1])

def connect(list1,list2):
    if(len(list1) == 0):
        return list2
    else:
        list2.pop(0)
        return list1 + (list2)

def connect1(list1,list2):
    if(len(list1) == 0):
        return list2
    else:
        return list1 + (list2)

def general_iterate(n, iterate, count, list, listProses):
    if(iterate == count):
        return list
    else:
        result = []
        for i in range(2**count):
            temp = []
            for j in range(n):
                temp.append(list[(n-1)*i+j])
            temp = base_iterate(n,temp,listProses)
            result = connect(result,temp)
        return general_iterate(n,iterate,count+1,result,listProses)

def one_iterate(n, count, list):
    result = []
    for i in range(2**count):
        temp = []
        for j in range(n):
            temp.append(list[(n-1)*i+j])
        temp = base_iterate(n,temp)
        result = connect(result,temp)
    return result

def take_result_point(list, n):
    result = []
    for i in range(len(list)):
        if(i%(n-1) == 0):
            result.append(list[i])
    return result

def makePic(awal,akhir):
    x = [point[0] for point in akhir]
    y = [point[1] for point in akhir]
    plt.plot(x, y, marker='.')
    px = [point[0] for point in awal]
    py = [point[1] for point in awal]
    plt.plot(px, py, marker='x')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bezier')
    plt.savefig('graph.png')
