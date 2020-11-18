kluba = input('Klub A : ')
klubb = input('Klub B : ')
hasil = []
i = 1
a = 0
b = 0
while a >= 0 and b >= 0:
    a, b = map(int,input(f'Pertandingan {i} : ').split())
    i = i + 1
    if a >= 0 and b >= 0:
        if a > b:
            hasil.append(kluba)
        elif a == b:
            hasil.append('Draw')
        else:
            hasil.append(klubb)
c = 1
for i in hasil:
    print(f'Hasil {c} : {i}')
    c = c + 1
print('Pertandingan selesai')