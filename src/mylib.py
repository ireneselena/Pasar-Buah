from tabulate import tabulate

def string_validation(title):
    while True:
        text = input(title)
        if text.isalpha() == True:
            break
        else:
            print("Silahkan inputkan hanya teks")
    return text.capitalize()


def integer_validation(title, minval=0, maxval=100):
    while True:
        num = input(title)
        try:
            num = int(num)
            if num >= minval and num <= maxval:
                break
            else:
                print('Angka yang anda masukkan di luar rentang')
        except:
            print("yang Anda inputkan bukan bilangan")
    return num 


def show(database, header=["index", "name", "stock", "price"]):
    # Menampilkan data dalam format tabulasi
    print(tabulate(database,
               headers = header,
               tablefmt = 'grid'))
    

def showCart(database, header=["Name", "Qty", "Price"]):
    # Menampilkan data dalam format tabulasi
    print(tabulate(database, headers = header, tablefmt = 'grid'))

def add(database):
    # Meminta input data buah yang baru
    name = string_validation("Masukkan Nama Buah: ")
    stock = integer_validation("Masukkan Stock Buah: ")
    price = integer_validation("Masukkan Harga Buah: ", maxval=150000)

    # Menambahkan data ke database
    for id, buah in enumerate(database):
        if name in buah:
            database[id] = [id, name, stock, price]
            break
    else:
        database.append([id+1, name, stock, price])
    
    # Menampilkan database ter-update
    show(database)


def delete(database):
    # Menampilkan database terbaru
    show(database)

    # Meminta user input indeks yang akan dihapus
    idx = integer_validation("Masukkan index buah yang ingin dihapus: ", maxval=len(database))

    # Melakukan proses penghapusan sesuai index
    for id, buah in enumerate(database):
        if idx == buah[0]:
            del database[idx]
        else:
            print('Buah yang Anda cari tidak ada')

    # Memperbarui index
    for id, buah in enumerate(database):
        if id != buah[0]:
            database[id][0] = id

    # Menampilkan database terbaru
    show(database)


def buy(database):
    # Menyalin database ke dalam penyimpanan sementara
    databaseTemp =database.copy()

    # Definisi variabel untuk menyimpan belanjaan 
    buahDiKeranjang = []

    # Proses pembelian
    reorder = None
    while reorder != "no": 

        # Menampilkan database
        show(databaseTemp)

        # Meminta input untuk index dan jumlah buah yang ingin dibeli
        idBuah = integer_validation('Masukkan index buah yang ingin dibeli: ', maxval=len(databaseTemp)-1)
        jumlahBuah = integer_validation('Masukkan jumlah yang ingin dibeli: ', minval=1, maxval=databaseTemp[idBuah][2])

        # Menambahkan ke dalam keranjang belanja
        buahDiKeranjang.append([databaseTemp[idBuah][1], jumlahBuah, databaseTemp[idBuah][3]])

        # Menampilkan keranjang belanja
        showCart(buahDiKeranjang)

        # Konfirmasi reorder
        while True:
            beliLain = string_validation('Mau beli yang lain? (ya/tidak)= ').lower()
            if beliLain in ["ya", "yes", "y", "iya"]:
                reorder = "yes"
            elif beliLain in ["tidak", "enggak", "gak", "g", "no", "n"]:
                reorder = "no"
            break
    
        # Update stock sementara
        databaseTemp[idBuah][2] -= jumlahBuah

    # Menghitung total harga
    total = 0


    for idx, buah in enumerate(buahDiKeranjang):
        # Hitung total harga per buah
        totalHarga = buah[1] * buah[2]

        # Input total harga ke buahDiKeranjang
        buahDiKeranjang[idx].append(totalHarga)
        
        # Sum seluruh harga
        total += totalHarga

    # Menampilkan keranjang belanja
    show(database= buahDiKeranjang, header = ["Nama", "Qty", "Harga", "Total Harga"])

    # Menampilkan uang yang harus dibayar
    print(f'Total yang harus dibayar: Rp.{total}')  
    
    # Proses pembayaran
    pembayaran(total)
    
    # Update database
    database = databaseTemp.copy()


def pembayaran(total): 
    while True:
         # Input jumlah uang
        bayar = int(input('Silahkan masukkan uang Anda: '))

        # Hitung selisih antara bayar dengan total
        selisih = total - bayar

        # Bandingkan antara uang dengan total harga
        if selisih > 0: 
            print(f'Uang Anda kurang sebesar Rp.{selisih}')
            continue
    
        # Ucapkan terima kasih ketika selesai pembayaran
        else:
            print(f'''Terimakasih. Uang kembalian Anda: {abs(selisih)}''')
            break
    
