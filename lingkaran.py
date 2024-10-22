
import math  # Mengimpor library untuk operasi matematika

# Membuat fungsi lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r * r

# Menentukan nilai jari-jari lingkaran
jari_jari = 7  

# Menghitung luas lingkaran menggunakan fungsi lambda
area = luas_lingkaran(jari_jari)

# Mencetak hasil luas lingkaran dengan format dua angka desimal
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")