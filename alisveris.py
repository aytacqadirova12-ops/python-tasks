qiymet = float(input("Məhsulun qiymətini daxil edin: "))
say = int(input("Alınacaq məhsulların sayını daxil edin: "))
verilen_pul = float(input("Verdiyiniz pul məbləğini daxil edin: "))

umumi_qiymet = qiymet * say
qalan_pul = verilen_pul - umumi_qiymet

print(f"Ümumi qiymət: {umumi_qiymet}")
print(f"Qalacaq pul: {qalan_pul}")