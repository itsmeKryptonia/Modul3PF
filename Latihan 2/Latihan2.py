data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

def get_integers(text): #Untuk mengambil nilai integer dari text
    return list(filter(str.isdigit, text.split())) #Text dipecah menggunakan Split

filtered_data = list(map(get_integers, data)) # filter untuk mengambil hanya nilai integer

for item in filtered_data:
    print(item)
