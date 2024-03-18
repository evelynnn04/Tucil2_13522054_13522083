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

### Algoritma Divide & Conquer

Pada algoritma Divide and Conquer, antar titik-titik kontrol akan ditarik garis.
Dari setiap garis terbentuk, titik tengah garis akan menjadi titik kontrol baru.
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
    ```
    pip install tkinter
    ```
- Matplotlib
    ```
    pip install matplotlib
    ```

#### Menjalankan program

- Menggunakan CLI

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