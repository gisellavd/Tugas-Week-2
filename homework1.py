arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    bMin = min(arrBerat)
    bMax = max(arrBerat)

def rerata(arrBerat):
    total = 0
    # Definisikan Proses Mencari Rerata Dari Total Berat
    for i in arrBerat:
        total = total + i
    rata = total/(len(arrBerat))
    # Return Hasil Rerata
    return rata

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    berat = float(input())
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(berat)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
print('Berat balita minimum:','{:.2f}'.format(bMin),'kg')
print('Berat balita maksimum:','{:.2f}'.format(bMax),'kg')
print('Rerata berat balita:','{:.2f}'.format(rerata(arrBerat)),'kg')
