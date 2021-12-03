print("Test Case 1:")
angka = [3,20,100,-35,50]
def nilai_maksimal(db):
    nt = db[0]
    for n in db:
        if n > nt:
            nt = n
    return nt
def nm(db):
    nk = db[0]
    for n in db:
        if n < nk:
            nk = n
    return nk
print(angka)
print("Nilai terbesar: ",nilai_maksimal(angka))
print("Nilai terkecil: ",nm(angka))
print("\nTest Case 2:")
angka = [3,20,90,35,75]
def nilai_maksimal(db):
    nt = db[0]
    for n in db:
        if n > nt:
            nt = n
    return nt
def nm(db):
    nk = db[0]
    for n in db:
        if n < nk:
            nk = n
    return nk
print(angka)
print("Nilai terbesar: ",nilai_maksimal(angka))
print("Nilai terkecil: ",nm(angka))
