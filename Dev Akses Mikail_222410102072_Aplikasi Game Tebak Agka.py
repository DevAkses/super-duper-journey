batas_tebak = 0 # Varibel batas_tebak bernilai 0
import random # Menampilkan karakter acak
angka = random.randint(1, 100) # Memberikan batasan dari angka 1-100
print('=' *15) #Mencetak "=" sebanyak 15 kali
print('Silahkan tebak!') #Mencetak kalimat 'Silahkan Tebak'
print('=' *15) #Mencetak "=" sebanyak 15 kali
for i in range (7): # perulangan dengan batasan mengulang sebanyak 7 kali
    batas_tebak += 1 # setiap kali mencoba untuk menebak angka, akan menambah variabel batas_tebak sebanyak 1
    jawaban = int(input('\nMasukkan angka: ')) # Variabel untuk membuat input yang baru
    if jawaban == angka: # percabangan bila nilai input yang dimasukkan sama dengan angka
        print('Tebakan anda tepat, anda menebak sebanyak', batas_tebak, 'kali') # Mencetak kalimat dengan string 
        break # program berhenti jika tebakan benar
    else:
        print('Tidak tepat, angka terlalu', 'kecil' if jawaban < angka else 'besar') 
        # mencetak kalimat 'Tidak tepat, angka terlalu kecil' jika variabel jawaban lebih kecil dari angka 
        # mencetak kalimat 'Tidak tepat, angka terlalu besar' jika variabel jawaban lebih besar dari angka 
    if batas_tebak == 7 : #percabangan bila nilai variabel batas_tebak mencapai 7
        print("Anda kurang beruntung") #mencetak kalimat 'anda kurang beruntung' 