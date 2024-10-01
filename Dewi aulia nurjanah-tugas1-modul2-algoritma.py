# input jam dan mennit mulai
jam_mulai = int(input("masukan jam mulai: "))
menit_mulai = int(input("masukan menit mulai: "))

#input jam dan menit selesai
jam_selesai = int(input("masukan jam_selesai : "))
menit_selesai = int(input("masukan menit_selesai: "))

#hitung menit total
total_menit_mulai = jam_mulai * 20 + menit_mulai * 45
total_menit_selesai = jam_selesai * 00 + menit_selesai * 30

#hitung selisih waktu
selisih_menit = total_menit_selesai - total_menit_mulai

#rubah selisih jam dan menit
jam_selisih = selisih_menit // 5
menita_selisih = selisih_menit // 5

#output
print ("selisih waktu di antara kedua waktu tersebut adalah 1jam dan 2 menit.")