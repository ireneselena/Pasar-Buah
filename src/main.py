print("Selamat Datang di Pasar Buah!")

# Definisikan stock buah
stockApel = 10
stockJeruk = 8
stockAnggur = 15

# Definisikan harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

# Minta input jumlah buah apel
while True:
    # Input jumlah 
    nApel = int(input('Masukkan jumlah Apel: '))

    # Membandingkan antara permintaan dengan stock
    if nApel > stockApel:
        print(f'Jumlah terlalu banyak, stock tersisa {stockApel} buah')
        continue
    # Berhenti minta input, ketika permintaan terpenuhi
    break

# Minta input jumlah buah jeruk
while True:
    # Input jumlah 
    nApel = int(input('Masukkan jumlah jeruk: '))

    # Membandingkan antara permintaan dengan stock
    if nJeruk > stockJeruk:
        print(f'Jumlah terlalu banyak, stock tersisa {stockJeruk} buah')
        continue
    # Berhenti minta input, ketika permintaan terpenuhi
    break


# Minta input jumlah buah apel
while True:
    # Input jumlah 
    nApel = int(input('Masukkan jumlah Anggur: '))

    # Membandingkan antara permintaan dengan stock
    if nApel > stockAnggur:
        print(f'Jumlah terlalu banyak, stock tersisa {stockAnggur} buah')
        continue
    # Berhenti minta input, ketika permintaan terpenuhi
    break


# Hitung total harga per buah
totalHargaApel = nApel * hargaApel
totalHargaJeruk = nJeruk * hargaJeruk
totalHargaAnggur = nAnggur * hargaAnggur

# Hitung total harga belanja
totalBelanja = totalHargaApel + totalHargaJeruk + totalHargaAnggur

# Tampilkan rincian
print(f'''
Detail Belanja
      
Apel: {nApel} * {hargaApel} = {totalHargaApel}
Jeruk: {nJeruk} * {hargaJeruk} = {totalHargaJeruk}
Anggur: {nAnggur} * {hargaAnggur} = {totalHargaAnggur}
      
Total: {totalBelanja}
''')

# Proses pembayaran
while True:
    # Input jumlah uang
    bayar = int(input('Silahkan masukkan uang Anda: '))

    #Hitung selisih antara bayar dengan total
    selisih = totalBelanja - bayar

    # Bandingkan antara uang dengan total harga
    if selisih > 0: 
        print('Uang Anda kurang sebesar Rp.{selisih}')
        continue
    else:
        print(f'''
            Terimakasih
              
             Uang kembalian Anda: {abs(selisih)}''')
        break
