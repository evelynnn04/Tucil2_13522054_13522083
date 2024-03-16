import app
import time 

# Time Start
start = time.time()

# Input
print("Selamat datang di generator kurva berzier!")
p1 = app.input_point(1)
p2 = app.input_point(2)
p3 = app.input_point(3)
while True:
    try:
        iterasi = input("Silakan masukkan banyaknya iterasi yang ingin dilakukan: ")
        iterasi = int(iterasi)
        if iterasi < 2:
            raise ValueError 
        break 
    except ValueError:
        print("Input invalid!")


# Time End 
end = time.time()

# Print Time
print("Runtime:", (end-start) * 10**3, "ms")