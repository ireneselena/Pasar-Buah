print("Selamat Datang di Pasar Buah!")

# Minta input user
nApel = int(input('Masukkan jumlah Apel: '))
nJeruk = int(input('Masukkan jumlah Jeruk: '))
nAnggur = int(input('Masukkan jumlah Anggur: '))

# Definisikan harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

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