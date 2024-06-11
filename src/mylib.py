from tabulate import tabulate

def string_validation(title):
    while True:
        a = input(title)
        if a.isalpha() == True:
            break
        else:
            print("Silahkan inputkan hanya teks")
    return a.capitalize()


def integer_validation(title):
    while True:
        a = input(title)
        if a.isnumeric() != True:
            print("Yang Anda inputkan bukan bilangan")
        elif int(a) >= 0:
            break
        else:
            print("Angka yang Anda inputkan salah")
    return int(a) 


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
    price = integer_validation("Masukkan Harga Buah: ")

    # Menambahkan data ke database
    for id, buah in enumerate(database):
        if name in buah:
            database[id] = [id, name, stock, price]
            break
    else:
        database.append([id+1, name, stock, price])
    
    # Menampilkan database ter-update
    show(database)

daftarBuah = [
    [0, "Apel", 20, 10000],
    [1, "Jeruk", 15, 15000],
    [2, "Anggur", 25, 20000]
    ]

def delete(database):
    # Menampilkan database terbaru
    show(database)

    # Meminta user input indeks yang akan dihapus
    idx = integer_validation("Masukkan index buah yang ingin dihapus: ")

    # Melakukan proses penghapusan sesuai index
    for buah in database:
        if idx == buah[0]:
            del database[idx]
            break
    else:
        print('Buah yang Anda cari tidak ada')

    # Memperbarui index
    for id, buah in enumerate(database):
        if id != buah[0]:
            database[id][0] = id

    # Menampilkan database terbaru
    show(database)

def buy(database):
    # Menampilkan database terbaru
    show(database)

    buahDiKeranjang = []
    reorder = None
    while reorder != "tidak": 
        idBuah = integer_validation('Masukkan index buah yang ingin dibeli: ')
        jumlahBuah = integer_validation('Masukkan jumlah yang ingin dibeli: ')
        if jumlahBuah > database[idBuah][2]:
            print(f'Stock tidak cukup, stock {database[idBuah][1]} tinggal {database[idBuah][2]}')
            print('Isi cart:')
            showCart(buahDiKeranjang)
            
        elif jumlahBuah <= database[idBuah][2]:
            buahDiKeranjang.append([database[idBuah][1],jumlahBuah,database[idBuah][3]])
            showCart(buahDiKeranjang)
            
        while True:
            beliLain = string_validation('Mau beli yang lain? (ya/tidak)= ').lower()
            if beliLain == "ya":
                reorder = "ya"
            elif beliLain == "tidak":
                reorder = "tidak"

            break
    
        # Menghitung total harga
        total = 0


    for idx, buah in enumerate(buahDiKeranjang):
        # Hitung total harga per buah
        totalHarga = buah[1] * buah[2]

        # Input total harga ke buahDiKeranjang
        buahDiKeranjang[idx].append(totalHarga)
        
        # Sum seluruh harga
        total += totalHarga

    show(database= buahDiKeranjang, header = ["Nama", "Qty", "Harga", "Total Harga"])
    print(f'Total yang harus dibayar: Rp.{total}')  
    
    pembayaran(total)
    


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
    


def inputBuah(nama, stock, harga):
    """Fungsi meminta user untuk input jumlah buah 
    dan menghitung harganya.

    Args:
        nama (String): Nama buah yang akan dibeli
        stock (Integer): Stock buah yang akan dibeli
        harga (Integer): Harga buah per kg

    Returns:
        nBuah (Integer): Jumlah buah yang dipesan 
        hargaBuah (Integer): Total harga buah
    """
    while True:
        # Input jumlah buah
        nBuah = int(input(f'Masukkan jumlah {nama}: '))

        # Membandingkan antara jumlah permintaan dengan stock
        if nBuah > stock:
            print(f'Jumlah terlalu banyak, stock tersisa {stock} buah')
            continue

        # Berhenti minta input, ketika jumlah permintaan terpenuhi
        break

    # Hitung total harga untuk buah tersebut
    hargaBuah = nBuah * harga

    return nBuah, hargaBuah