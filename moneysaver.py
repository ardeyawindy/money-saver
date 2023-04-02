import csv
file_name ="moneysaver.csv"
data = []

def awal():
    namaUser = input("Masukkan Nama Anda:")
    print("Halo {}, Selamat datang di Money Saver!". format(namaUser))
    print("Money Saver akan membantu anda mengatur keuangan anda dengan cara yang sederhana")

def menu():
    print(" ")
    print("Pilih menu di bawah dengan angka yang tersedia")
    print('''
    1. Lihat Data
    2. Tambah Data
    3. Hapus Data
    ''')
    return int(input("masukan pilihan : "))

def bacaData() :
    print("             TRANSAKSI PEMBELIAN             ")
    print("===============================================")
    with open(file_name,'r') as csvFile:
        read = csv.reader(csvFile)
        for isi in read:
            print(isi)
            print("="*100)    

def csv_ke_list():
    with open(file_name,'r',newline='') as csvFile:
        baca = csv.reader(csvFile)
        for baris in baca:
            data.append(baris)

def tambahNabung():
    mingguKe = input ("Minggu ke :")
    namaHari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    pemasukan = int(input('Pemasukan anda pada minggu ini =Rp.'))
    NabungMingguan = int(input('anda ingin menabung pada minggu ini berapa:Rp.')) 
    SisaTarget = int(input('target menabung anda:Rp.')) 
    PengeluaranMingguan = pemasukan - NabungMingguan
    realisasi = 0
    for i in namaHari:
        pengeluaran = int(input('Pengeluaran anda hari {} minggu ini:Rp.'. format(i)))
        realisasi += pengeluaran
    if realisasi > PengeluaranMingguan:
        print('maaf, minggu ini anda harus utang atau tabungan anda dipotong.')
        NabungMingguan = NabungMingguan - (realisasi - PengeluaranMingguan)
        print('tabungan anda saat ini:Rp. {}'.format(NabungMingguan))
        SisaTarget = SisaTarget - NabungMingguan
        if SisaTarget > 0 :
            print('tinggal Rp. {} lagi untuk mewujudkan mimpi anda'.format(SisaTarget))
        elif SisaTarget <= 0:
            print('Selamat tabungan anda sudah mencukupi')
    elif realisasi < PengeluaranMingguan:
        SisaPengeluaran = (input('sisa uang anda minggu ini akan anda apakan(sedekah, menabung, atau foya-foya)?')).lower()
        if SisaPengeluaran == 'sedekah':
            UangLebih = PengeluaranMingguan - realisasi
            print('tabungan anda saat ini:Rp. {}'.format(NabungMingguan))
            SisaTarget = SisaTarget - NabungMingguan
            if SisaTarget > 0 :
                print('tinggal Rp. {} lagi untuk mewujudkan mimpi anda'.format(SisaTarget))
            elif SisaTarget <= 0:
                print('Selamat tabungan anda sudah mencukupi')
            print('Uang yang akan anda sedekahkan sebesar Rp.{}'.format(UangLebih))
            print('semoga Allah SWT membalas kebaikan anda')
        elif SisaPengeluaran == 'menabung':
            UangLebih = PengeluaranMingguan - realisasi
            NabungMingguan = NabungMingguan + UangLebih
            print('Anda menambah tabungan anda sebesar Rp. {}'.format(UangLebih))
            print('tabungan anda saat ini: {}'.format(NabungMingguan))
            SisaTarget = SisaTarget - NabungMingguan
            if SisaTarget > 0 :
                print('tinggal Rp. {} lagi untuk mewujudkan mimpi anda'.format(SisaTarget))
            elif SisaTarget <= 0:
                print('Selamat tabungan anda sudah mencukupi')
        elif SisaPengeluaran == 'foya-foya':
            UangLebih = PengeluaranMingguan - realisasi
            print('Uang yang akan anda gunakan untuk foya-foya sebesar Rp.{}'.format(UangLebih))
            print('tabungan anda saat ini:Rp. {}'.format(NabungMingguan))
            SisaTarget = SisaTarget - NabungMingguan
            if SisaTarget > 0 :
                print('tinggal Rp. {} lagi untuk mewujudkan mimpi anda'.format(SisaTarget))
            elif SisaTarget <= 0:
                print('Selamat tabungan anda sudah mencukupi')
                print('semoga anda dapat memanfaatkan uang anda untuk hal yang lebih baik')
        else:
            print('maaf, input yang anda masukkan tidak tersedia')
    with open(file_name,'a', newline='') as csvFile:
        tulis = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tulis.writerow([mingguKe,pemasukan, pengeluaran, NabungMingguan])

def tambahTdkNabung():
    mingguKe = input ("Minggu ke :")
    namaHari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    pemasukan = int(input('Pemasukan anda pada minggu ini =Rp.'))
    realisasi = 0
    for i in namaHari:
        pengeluaran = int(input('Pengeluaran anda hari {} minggu ini:Rp.'. format(i)))
        realisasi += pengeluaran
    if realisasi > pemasukan :
        utang = realisasi - pemasukan
        print("Mohon maaf minggu ini Anda harus utang atau pemasukan minggu depan anda akan dipotong Rp.", utang)
    elif realisasi < pemasukan:
        SisaPengeluaran = (input('sisa uang anda minggu ini akan anda apakan(sedekah atau foya-foya)? ')).lower()
        if SisaPengeluaran == 'sedekah':
            UangLebih = pemasukan - realisasi
            print('Uang yang akan anda sedekahkan sebesar RP.{}'.format(UangLebih))
            print('Semoga Allah SWT membalas kebaikan anda')
        elif SisaPengeluaran == 'foya-foya':
            UangLebih = pemasukan - realisasi
            print('Uang sebesar Rp.{} akan anda gunakan untuk foya-foya'.format(UangLebih))
            print('semoga anda dapat memanfaatkan uang anda untuk hal yang lebih baik')
        else:
            print( 'maaf, input yang anda masukkan tidak tersedia')
    with open(file_name,'a', newline='') as csvFile :
        tulis = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tulis.writerow([mingguKe,pemasukan, pengeluaran, "-"])

def hapusData(inputan):
    data.remove(data[inputan])
    with open(file_name,'w',newline='') as csvFile:
        tulisUlang = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tulisUlang.writerows(data)

if __name__ == "__main__":
    csv_ke_list()
    print("                 MONEY SAVER                 ")
    awal()
    pilihan = menu()

    if pilihan == 1 :
        bacaData()
    elif pilihan == 2 :
        menabung = input('apakah anda ingin menabung(ya/tidak)? ').lower()
        if menabung == "ya":
            tambahNabung()
        elif menabung == "tidak":
            tambahTdkNabung()
    elif pilihan == 3 : 
        inputan = int(input("Minggu ke berapa yang ingin dihapus? : "))
        print("anda akan menghapus data {}".format(data[inputan]))
        hapusData(inputan)
        print("data berhasil dihapus")