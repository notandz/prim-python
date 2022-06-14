import sys

masuk = int(input("Masukkan jumlah Vertex : "))
matriks = []

for i in range(masuk): #input matriks ketetanggaan
    print("Masukkan Vertex ke-", i+1)
    x = [int(x) for x in input().split()]
    matriks.append(x)
print(*matriks,'\n',sep='\n') #tampilkan matriks ketetanggan

lewat = [] #buat array baru untuk vertex yg udah dikunjungi
for i in range(masuk):
    lewat.append(0)

lewat[0] = True #set vertex pertama udah dikunjungi
mst = 0 #buat variabel nampung mst

print("Edge ||| Weight\n")

for x in range(masuk-1): #perulangan akan dilakukan sejumlah vertex - 1
    minimum = sys.maxsize #set nilai min untuk dibandingkan sama bobot
    mina = 0 #buat nampung indeks minimum
    minb = 0   
    for i in range(masuk):
        if lewat[i]:
            for j in range(masuk):
                if ((not lewat[j]) and matriks[i][j]):
                    #kl pasangannya belum dilihat, dan tentunya ada edge (kl dah terlihat berarti cycle)
                    if minimum > matriks[i][j]:
                        minimum = matriks[i][j]
                        mina = i
                        minb = j
    print (str(mina) + " --> " + str(minb) + " ||| " + str(matriks[mina][minb]))
    mst = mst + matriks[mina][minb] #jumlahkan ke mst
    lewat[minb] = True #set udah dikunjungin

print(f'Minimum Spanning Tree: {mst}') #cetak mst akhir
