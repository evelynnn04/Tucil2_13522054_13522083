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

<<<<<<< HEAD
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

# def divide(n,list):
#     if(len(list) == n):
#         return list
#     else:
#         mid = len(list)//2
#         left = [divide(n, list[:mid+1])]
#         right = [divide(n, list[mid:])]
#         result = connect1(left,right)
#         print(result)
#         return result

def general_iterate(n, iterate, count, list):
    if(iterate == count):
        return list
    else:
        result = []
        for i in range(2**count):
            temp = []
            for j in range(n):
                temp.append(list[(n-1)*i+j])
            temp = base_iterate(n,temp)
            result = connect(result,temp)
        return general_iterate(n,iterate,count+1,result)

def take_result_point(list, n):
    result = []
    for i in range(len(list)):
        if(i%(n-1) == 0):
            result.append(list[i])
    return result


p = (1,2)
pp = (0,5)

mp = midPoint(p,pp)
# print(mp)

list = [(0,0)]
list = wide(p,list,mp)
# print(list)

d = [[0,0],[2,2],[4,2],[6,2],[8,0]]
# d = divide(3,d)
# print(d)
# print(len(bez))

kr = [[0, 0], [1.0, 1.0], [2.0, 1.5], [3.0, 2.0], [4.0, 2.0]]
kn = [[4.0, 2.0], [5.0, 2.0], [6.0, 1.5], [7.0, 1.0], [8, 0]]
# gb = connect(kr,kn)
# print(gb)

# bez = base_iterate(3,bez)
bez = [[238.0, 680.0], [312.8, 0.0], [374.0, 0.0], [442.0, 680.0]]

start_time = time.time()
bez = general_iterate(4,4,0,bez)
end_time = time.time()
t = end_time - start_time
print(bez)
print()
print(take_result_point(bez,4))
print(len(bez))
print(t)
=======
# Solve
for point in list_of_point:
    list_of_x.append(point[0])
    list_of_y.append(point[1])
result_dnc = app.general_iterate(num_of_point, itr, 0, list_of_point)
result_x = app.brute_force_bezier (num_of_point, list_of_x, itr)
result_y = app.brute_force_bezier (num_of_point, list_of_y, itr)
result_bf = app.merge_xy(result_x, result_y)
print(result_dnc)
print(result_bf)
>>>>>>> a90d25875a8ec9d1f15e77b38df1e6080536cb4d
