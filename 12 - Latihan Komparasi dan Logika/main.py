#membuat gabungan area rentang dari angka
#++++++3--------------10+++++++

cin = float(input('Masukan angka yang berniai\nkurang dari 3\natau\nlebih dari 10 :'))
#memeriksa kurang dari 3 
isKurangDari = (cin < 3)
print('Kurang dari 3 ',isKurangDari)
#memeriksa lebih dari 10
isLebihDari = (cin > 3)
print('Lebih dari 10',isLebihDari)

#memeriksa lhasil
isHasil = (isLebihDari or isKurangDari)
print('Hasil = ',isHasil)