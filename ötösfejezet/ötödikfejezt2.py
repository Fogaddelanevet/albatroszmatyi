def napok(i, n):
    napos=["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
    osszeg = (i + n) % 7
    print(napos[osszeg-1])


napok(int(input("Számot:")),int(input("Másik számot:")))


