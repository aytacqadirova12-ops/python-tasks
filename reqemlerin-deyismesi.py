eded = int(input("İkirəqəmli tam ədəd daxil edin: "))

onluq = eded // 10
teklik = eded % 10

yeni_eded = teklik * 10 + onluq
print(f"Yeni ədəd: {yeni_eded}")