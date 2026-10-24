ilkin_qiymet = float(input("Məhsulun ilkin qiymətini daxil edin: "))
endirim_faizi = float(input("Endirim faizini daxil edin (%): "))

endirim_meblegi = ilkin_qiymet * (endirim_faizi / 100)
son_qiymet = ilkin_qiymet - endirim_meblegi

print(f"Endirim məbləği: {endirim_meblegi}")
print(f"Endirimdən sonra qiymət: {son_qiymet}")