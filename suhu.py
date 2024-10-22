def Konversi_Suhu(Temperature, value):
    # Membuat Fungsi untuk mengonversi suhu antara Celsius dan Fahrenheit
    # Temperature: Nilai suhu yang akan dikonversi
    # value: Satuan suhu asal ('C' untuk Celsius, 'F' untuk Fahrenheit)

    if value == 'C':
        # Jika satuan yang diberikan adalah Celsius
        # Konversi dari Fahrenheit ke Celsius
        Temperatur_suhu = (Temperature - 32) * 5 / 9
        return Temperatur_suhu, 'C'  # Mengembalikan suhu yang sudah dikonversi dan satuan 'C'
    
    else:
        # Jika satuan bukan Celsius, maka diasumsikan Fahrenheit
        # Konversi dari Celsius ke Fahrenheit
        Temperatur_suhu = (Temperature * 9 / 5) + 32
        return Temperatur_suhu, 'F'  # Mengembalikan suhu yang sudah dikonversi dan satuan 'F'

# Mengonversi dari Celsius ke Fahrenheit
celsius_temperatur = 30  # Nilai suhu dalam Celsius yang ingin dikonversi
Temperatur_suhu, target_value = Konversi_Suhu(celsius_temperatur, 'F')  # Memanggil fungsi konversi
print(f"{celsius_temperatur}°C dikonversi ke Fahrenheit adalah {Temperatur_suhu:.2f}°{target_value}")
# Menampilkan hasil konversi dari Celsius ke Fahrenheit

# Mengonversi dari Fahrenheit ke Celsius
fahrenheit_temperatur = 86  # Nilai suhu dalam Fahrenheit yang ingin dikonversi
Temperatur_suhu, target_value = Konversi_Suhu(fahrenheit_temperatur, 'C')  # Memanggil fungsi konversi
print(f"{fahrenheit_temperatur}°F dikonversi ke Celsius adalah {Temperatur_suhu:.2f}°{target_value}")
# Menampilkan hasil konversi dari Fahrenheit ke Celsius





