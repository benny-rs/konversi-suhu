print('''
PROGRAM KONVERSI SUHU
=====================
''')
suhuAwal = int(input('Masukkan Suhu : '))
satAwal = input('Masukkan Satuan (C/F) : ').upper()
if satAwal == 'C':
    suhuAkhir = (9 * suhuAwal) / 5 + 32
    satAkhir = 'Fahrenheit'
elif satAwal == 'F':
    suhuAkhir = (suhuAwal - 32) * 5 / 9
    satAkhir = 'Celcius'
print('Suhu setelah dikonversi adalah {} derajat {}'.format(suhuAkhir, satAkhir))