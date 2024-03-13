from collections import namedtuple

# Struct
Point = namedtuple('Point', ['x', 'y'])

# Input 
def input_point(point_n):
    while True:
        try:
            p = input(f"Silahkan masukkan koodinat p{point_n}.x dan p{point_n}.y dipisahkan spasi: ")
            px, py = p.split(" ")
            px = float(px)
            py = float(py)
            return Point(px, py)
        except ValueError:
            print(f"Input invalid!")


# For All
def control_point_coordinate(p1, p2):
    p3_x = (p1.x + p2.x) / 2
    p3_y = (p1.y + p2.y) / 2
    p3 = Point(p3_x, p3_y)
    return p3

# For Brute Force Method
def brute_force_berzier(p1, p2, order):
    pass
    
# For Divide and Conquer Method
def DNC_berzier(p1, p2, order):
    pass

