print("SELAMAT DATANG DI PPDB SMP 69 XXX 2024")
print("="*100)

nama = str (input("Nama Siswa:"))
nik = int (input("NIK:"))
nisn = int (input("NISN:"))
lahir = str (input("Tanggal Lahir (07 Agustus):"))
tahun = int (input("Tahun Lahir:"))
umur = 2024 - tahun


if ( umur <= 17 and umur>=13 ):
    pilih_jalur = 'Pilih Jalur PPDB'

    print("="*10)
    print(pilih_jalur)
    print("Afirmasi")
    print("Zonasi")
    print("Prestasi")

    jalur = str(input("Pilih Jalur (Afirmasi/Zonasi/Prestasi):"))

    if jalur.capitalize() in ("Afirmasi", "Zonasi", "Prestasi"):
        if jalur.capitalize() == "Afirmasi":
            print("="*10)
            print(jalur.upper())
            nilai = float(input("Nilai Rata-Rata Ijazah (0.0):"))
            prestasi = int (input("Jumlah Prestasi Yang Dimiliki (Ketik '0' Jika Tidak Punya):"))
            miskin = bool (input("Terdaftar Dalam DTKS (True/False):").capitalize())
            if miskin == True:
                fakir= "Pilih Program DTKS"
                print("KIP")
                print("KKS")
                print("KPS")
                print("PKH")

                dtks = str (input("Pilih Program DTKS (KIP/KKS/KPS/PKH):"))

                if dtks.upper() in ("KIP", "KKS", "KPS", "PKH"):
                    if dtks.upper() == "KIP":

                        no_dtks = int(input("No KIP:"))
                        if no_dtks >= 100 and nilai >= 7.4 :
                            hasil = ("SELAMAT ANDA DITERIMA!")


                        elif no_dtks >= 100 and nilai < 7.4:
                            hasil = ("MAAF ANDA TIDAK DITERIMA!")
        
                        else:
                            hasil = ("MASUKAN DATA ANDA DENGAN BENAR!")


                    elif dtks.upper() == "KKS":

                        no_dtks = int(input("No KKS:"))
                        if no_dtks >= 100 and nilai >= 7.4 :
                            hasil = ("SELAMAT ANDA DITERIMA!")


                        elif no_dtks >= 100 and nilai < 7.4:
                            hasil = ("MAAF ANDA TIDAK DITERIMA!")


                        else:
                            hasil = ("MASUKAN DATA ANDA DENGAN BENAR!")


                    elif dtks.upper() == "KPS":

                        no_dtks = int(input("No KPS:"))
                        if no_dtks >= 100 and nilai >= 7.4 :
                            hasil = ("SELAMAT ANDA DITERIMA!")

                        elif no_dtks >= 100 and nilai < 7.4:
                            hasil = ("MAAF ANDA TIDAK DITERIMA!")


                        else:
                            hasil = ("MASUKAN DATA ANDA DENGAN BENAR!")
                            
                    elif dtks.upper() == "PKH":

                        no_dtks = int(input("No PKH:"))
                        if no_dtks >= 100 and nilai >= 7.4 :
                            hasil = ("SELAMAT ANDA DITERIMA!")


                        elif no_dtks >= 100 and nilai < 7.4:
                            hasil = ("MAAF ANDA TIDAK DITERIMA!")

                        else:
                            hasil = ("MASUKAN DATA ANDA DENGAN BENAR!")

                    else:
                        hasil = ("MASUKAN DATA ANDA DENGAN BENAR!")
    
                    print("="*100)
                    print("NAMA:", nama.upper())
                    print("NIK:", nik)
                    print("NISN:", nisn)
                    print("TANGGAL LAHIR:", lahir.upper())
                    print("TAHUN:", tahun)
                    print("JALUR YANG DIPILIH:", jalur.upper())
                    print("NILAI IJAZAH:", nilai)
                    print("PRESTASI:", prestasi)
                    print("PROGRAM DTKS:", dtks.upper())
                    print("NO Program:", no_dtks)
                    print(hasil)
    
        elif jalur.capitalize() == "Zonasi":
            print("="*10)
            print(jalur.upper())
            nilai = float(input("Nilai Rata-Rata Ijazah (0.0):"))
            prestasi = int (input("Jumlah Prestasi Yang Dimiliki (Ketik '0' Jika Tidak Punya):"))
            jarak = float (input("Jarak Rumah Dalam Kilometer (3.2):"))

            if jarak <= 5.0 :
                hasil = ("SELAMAT ANDA DITERIMA!")

            elif jarak > 5.0 and jarak <= 8.0 and nilai >= 7.2  :
                hasil = ("SELAMAT ANDA DITERIMA!")

            elif jarak > 5.0 and nilai < 7.2:
                hasil = ("MAAF ANDA TIDAK DITERIMA!")

            else : 
                hasil = ("MASUKAN DATA ANDA DENGAN BENAR!")

            print("="*100)
            print ("NAMA:", nama.upper())
            print ("NIK:", nik)
            print ("NISN:", nisn)
            print ("TANGGAL LAHIR:", lahir.upper())
            print ("TAHUN:", tahun)
            print ("JALUR YANG DIPILIH:", jalur.upper())
            print("NILAI IJAZAH:", nilai)
            print("PRESTASI:", prestasi)
            print("JARAK RUMAH:", jarak,"KM")
            print (hasil)

        elif jalur.capitalize() == "Prestasi":
            print("="*10)
            print(jalur.upper())
            nilai = float(input("Nilai Rata-Rata Ijazah (0.0):"))

            if nilai >= 8.9:
                hasil = ("SELAMAT ANDA DITERIMA!")

            elif nilai < 8.9 and nilai >= 7.0:
                prestasi = int (input("Jumlah Prestasi Yang Dimiliki (Ketik '0' Jika Tidak Punya):"))
                if prestasi >= 1:
                    hasil = ("SELAMAT ANDA DITERIMA!")

                elif prestasi >= 0:
                    hasil = ("MAAF ANDA TIDAK DITERIMA!")

                else:
                    hasil = ("MASUKAN DATA ANDA DENGAN BENAR!")

            else:
                hasil = ("MASUKAN DATA ANDA DENGAN BENAR!")

            print("="*100)
            print ("NAMA:", nama.upper())
            print ("NIK:", nik)
            print ("NISN:", nisn)
            print ("TANGGAL LAHIR:", lahir.upper())
            print ("TAHUN:", tahun)
            print ("JALUR YANG DIPILIH:", jalur.upper())
            print("NILAI IJAZAH:", nilai)
            print("PRESTASI:", prestasi)
            print (hasil)

    else:
        print("MASUKAN DATA ANDA DENGAN BENAR!")

else:
    print('Maaf Anda Tidak Bisa Melakukan PPDB')





# NOTE!!!!!

#  elif (kondisi if jamak)

# hasil = ("SELAMAT ANDA DITERIMA!")
# data = ("MASUKAN DATA ANDA DENGAN BENAR!")
# hasil = ("MAAF ANDA TIDAK DITERIMA!")




        # if nilai >= 7.8 and miskin == True:
        #     no_kip = int (input("Masukan Nomor KIP/Kartu PKH:"))
        #     if no_kip >=100000:
                # hasil = ("Selamat Anda Diterima")
                # print("="*10)
                # print ("NAMA:", nama.upper())
                # print ("NIK:", nik)
                # print ("NISN:", nisn)
                # print ("TANGGAL LAHIR:", lahir.capitalize())
                # print ("TAHUN:", tahun)
                # print("NILAI IJAZAH:", nilai)
                # print("PRESTASI:", prestasi)
                # print ("JALUR YANG DIPILIH ", jalur)
                # print()
                # print (hasil)   