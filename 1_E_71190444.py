deret_awal = int(input("Masukan awal deret: "))
deret_akhir = int(input("Masukan akhir deret: "))

for j in range(deret_awal,deret_akhir):
    if j % 2 == 0:
        if j % 5 != 0 and j % 9 != 0:
            print(j, end=" ")
