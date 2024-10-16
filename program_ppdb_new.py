print("SELAMAT DATANG DI PPDB SMP 69 XXX 2024")
print("="*100)

nama = str (input("Nama Siswa:"))
nik = int (input("NIK:"))
nisn = int (input("NISN:"))
lahir = str (input("Tanggal Lahir (07 Agustus):"))
tahun = int (input("Tahun Lahir:"))

umur = 2024 - tahun

if ( umur <= 17 and umur>=12 ):
    nilai = float (input("Nilai Ijazah (8.0):"))
    prestasi = int (input("Jumlah Prestasi (Ketik '0' Jika Tidak Punya):"))

    print("="*100)
    print('Pilih Jalur PPDB')
    print("Afirmasi")
    print("Zonasi")
    print("Prestasi")

    jalur = str(input("Pilih Jalur (Afirmasi/Zonasi/Prestasi):")).capitalize()
    program = {"KIP", "KKS", "KPS", "PKH"}

    if jalur in ("Afirmasi", "Zonasi", "Prestasi") and jalur == "Afirmasi":
        print("="*100)
        print("Pilih Program DTKS")
        print("KIP")
        print("KKS")
        print("KPS")
        print("PKH")
        pilih_dtks = str (input("Pogram DTKS:")).upper()
        no_dtks = int(input("Masukan Nomor Program DTKS:"))
        if pilih_dtks in program  and nilai >= 7.2:
            hasil = "Selamat Anda Diterima Di SMP 69 XXX"
        else:
            hasil = "Maaf Anda Tidak Diterima Di SMP 69 XXX"

    elif jalur in ("Afirmasi", "Zonasi", "Prestasi") and jalur == "Zonasi":
        jarak = float (input("Jarak Rumah Ke Sekolah (3.4)Km:"))
        if (jarak <= 5.0):
            hasil = "Selamat Anda Diterima Di SMP 69 XXX"
        elif (jarak > 5.0 and jarak <= 8.0 and nilai >=7.2):
            hasil = "Selamat Anda Diterima Di SMP 69 XXX"
        else:
            hasil = "Maaf Anda Tidak Diterima Di SMP 69 XXX"

    elif jalur in ("Afirmasi", "Zonasi", "Prestasi") and jalur == "Prestasi":
        if (nilai >= 8.9):
            hasil = "Selamat Anda Diterima Di SMP 69 XXX"
        elif (nilai < 8.9 and nilai >= 7.0 and prestasi >0):
            hasil = "Selamat Anda Diterima Di SMP 69 XXX"
        else:
            hasil = "Maaf Anda Tidak Diterima Di SMP 69 XXX"

print("="*100)
print("NAMA:", nama.upper())
print("NIK:", nik)
print("NISN:", nisn)
print("TANGGAL LAHIR:", lahir.upper())
print("TAHUN:", tahun)

if umur <= 17 and umur >=12:
    print("NILAI IJAZAH:", nilai)
    print("PRESTASI:", prestasi)
    print("JALUR YANG DIPILIH:", jalur.upper())
    if jalur == "Afirmasi":
            print("PROGRAM DTKS:", pilih_dtks)
            print("NO PROGRAM DTKS:", no_dtks)

    elif jalur == "Zonasi":
        print("JARAK RUMAH KE SMP 69 XXX:", jarak, "KM")
    
    print(hasil)

else:
    print("Maaf Anda Tidak Bisa Ikut Kegiatan PPDB")
