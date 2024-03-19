# Tucil2_13522054_13522083

## Kelompok 

|   NIM    |              Nama                   |
| :------: |    :---------------------------:    |
| 13522054 |         Benjamin Sihombing          |
| 13522083 |           Evelyn Yosiana            |

## Kurva Bézier

Kurva Bézier adalah kurva halus yang sering digunakan dalam desain grafis, animasi, dan manufaktur.
Kurva ini dibuat dengan menghubungkan beberapa titik kontrol, yang menentukan bentuk dan arah kurva.
Cara membuatnya cukup mudah, yaitu dengan menentukan titik-titik kontrol dan menghubungkannya dengan kurva.
Pada program ini, kurva Bézier akan dibuat dengan 2 algoritma. 
Algortima yang digunakan adalah algortima Brute Force (sebagai pembanding) dan algortima Divide and Conquer.

### Algoritma Brute Force

Pada algoritma Brute Force, koordinat x dan y dicari dengan menggunakan suatu rumus umum.
Rumus umumnya:
$$
\mathbf{B}(t)=\sum_{i=0}^{n}\binom{n}{i}(i-t)^{n-i}t^i\mathbf{P}_i
$$
dengan B adalah titik koordinat hasil, P titik kontrol, n adalah banyak titik kontrol, i adalah pencacah titik, 
dan t adalah rasio jarak titik awal ke titik tengah dengan jarak titik awal ke titik selanjutnya.

### Algoritma Divide & Conquer

Pada algoritma Divide and Conquer, antar titik-titik kontrol akan ditarik garis.
Dari setiap garis terbentuk, titik tengah (tepat membagi 2 gari) garis akan menjadi titik kontrol baru.
Proses ini akan berulang hingga terbentuk 1 titik kontrol tunggal.
Titik-titik kontrol baru tersebut akan digunakan pada proses iterasi selanjutnya.

### Requirements

Berikut ini tools yang diperlukan untuk menjalankan program:
1. Python
2. pip
3. Tkinter
4. Turtle

### How to Run

#### Instalasi module python

- pip 
    - Untuk windows:
        1. Jalankan command ini di terminal
            ```
            python get-pip.py
            ```
        2. Masukkan pip ke path
    - Untuk WSL:
        1. Jalankan command ini di terminal 
            ```
            sudo apt update && upgrade
            sudo apt install python3 python3-pip ipython3 
            ```
- Tkinter
    - Untuk windows:
        ```
        pip install tkinter
        ```
    - Untuk WSL:
        ```
        sudo apt install python3-tk
        ```
- Matplotlib
    - Untuk windows:
        ```
        pip install matplotlib
        ```
    - Untuk WSL:
        ```
        sudo apt-get install python3-matplotlib 
        ```
- Turtle (sebenarnya tergabung dalam Tkinter)
    - Untuk windows:
        ```
        pip install turtle
        ```
    - Untuk WSL:
        ```
        sudo pip3 install PythonTurtle
        ```

#### Menjalankan program

- Menggunakan CLI
    1. Buka terminal
    2. Pindah ke directory tempat bezier.py berada
    3. Jalankan command ini pada terminal
        ```
        py bezier.py
        ```
        atau
        ```
        python bezier.py
        ```
- Menggunakan GUI
    1. Buka terminal
    2. Pindah ke directory tempat gui.py berada
    3. Jalankan command ini pada terminal
        ```
        py gui.py
        ```
        atau
        ```
        python gui.py
        ```

#### Note: