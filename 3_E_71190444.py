angka1 = int(input("Masukan Angka :"));
init= angka1;
for ketupat in range (0,angka1):
    for  pola in range (-2, init+1):
         print(" ",end="")

    for shape in range (0, ketupat+1):
        print("* ", end="")
    init-=1
    print("")
init=angka1;
for ketupat in range (1,angka1):
    for pola in range (-4, ketupat):
        print(" ",end="")

    for shape in range (1, init):
        print("* ",end="")
    init-=1
    print("")
