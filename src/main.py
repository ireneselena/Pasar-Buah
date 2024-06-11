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
            break
        elif option == "5":
            break
        else:
            print("Input anda salah. Silahkan input ulang!")


main()