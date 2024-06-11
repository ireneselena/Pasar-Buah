import mylib

daftarBuah = [
    [0, "Apel", 20, 10000],
    [1, "Jeruk", 15, 15000],
    [2, "Anggur", 25, 20000]
    ]

def main():
    listMenu = '''Selamat Datang di Pasar Buah!
    
    List Menu:
    1. Menampilkan Daftar Buah
    2. Menambah Buah
    3. Menghapus Buah
    4. Membeli Buah
    5. Exit Program'''

    while True:
        # Menampilkan tampilan utama
        print(listMenu)

        # Meminta input menu yang dipilih
        option = input('Masukkan angka Menu yang ingin dijalankan: ')

        # Menjalankan fungsi sesuai input angka Menu
        if option == "1":
            mylib.show(daftarBuah)
        elif option == "2":
            mylib.add(daftarBuah)
        elif option == "3":
            mylib.delete(daftarBuah)
        elif option == "4":
            mylib.buy(daftarBuah)
        elif option == "5":
            break
        else:
            print("Input anda salah. Silahkan input ulang!")


main()



# # Definisikan stock buah
# stockApel = 10
# stockJeruk = 8
# stockAnggur = 15

# # Definisikan harga buah
# hargaApel = 10000
# hargaJeruk = 15000
# hargaAnggur = 20000

# # Minta input jumlah buah dan hitung harga buah
# nApel, totalHargaApel = mylib.inputBuah(nama='Apel', stock=stockApel, harga=hargaApel)
# nJeruk, totalHargaJeruk = mylib.inputBuah(nama='Jeruk', stock=stockJeruk, harga=hargaJeruk)
# nAnggur, totalHargaAnggur = mylib.inputBuah(nama='Anggur', stock=stockAnggur, harga=hargaAnggur)

# # Hitung total harga belanjaan
# totalBelanja = totalHargaApel + totalHargaJeruk + totalHargaAnggur

# # Tampilkan rincian belanjaan
# print(f'''
# Detail Belanja
      
# Apel: {nApel} x {hargaApel} = {totalHargaApel}
# Jeruk: {nJeruk} x {hargaJeruk} = {totalHargaJeruk}
# Anggur: {nAnggur} x {hargaAnggur} = {totalHargaAnggur}

# Total: {totalBelanja}
# ''')

# # Proses pembayaran
# while True:
#     # Input jumlah uang
#     bayar = int(input('Silahkan masukkan uang Anda: '))

#     # Hitung selisih antara bayar dengan total
#     selisih = totalBelanja - bayar

#     # Bandingkan antara uang dengan total harga
#     if selisih > 0: 
#         print(f'Uang Anda kurang sebesar Rp.{selisih}')
#         continue
    
#     # Ucapkan terima kasih ketika selesai pembayaran
#     else:
#         print(f'''Terimakasih. Uang kembalian Anda: {abs(selisih)}''')
#         break