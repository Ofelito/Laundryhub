def hitung_kilo (Kg):
    hasil = 4000 * int(Kg)
    return hasil

def hitung_kembalian (jmlh_uang,total):
    kembali = int(jmlh_uang) - int(total)
    return kembali

def tambah_nol(number,length):
    for i in range(1,length):
        number = "0"+number
    return number