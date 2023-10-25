def konversi(minggu=0, hari=0, jam=0, menit=0): #fungsi yang menerima empat argumen opsional yang menggambarkan waktu dalam bentuk minggu, hari, jam, dan menit.
    return ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit) #

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

output_data = []
for item in data:
    parts = item.split() #memecah string item menjadi bagian-bagian yang dipisahkan oleh spasi dan menyimpannya dalam list parts
    minggu = int(parts[0]) # Mengambil angka pertama (minggu) 
    hari = int(parts[2]) # Mengambil angka ketiga (hari) 
    jam = int(parts[4]) # Mengambil angka kelima (jam) 
    menit = int(parts[6]) #Mengambil angka ketujuh (menit) 
    hasil_konversi = konversi(minggu, hari, jam, menit)
    output_data.append(hasil_konversi) #Hasil konversi dimasukkan ke dalam list output_data

print("OutputData =", output_data)
