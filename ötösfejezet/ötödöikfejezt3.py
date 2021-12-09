def szamol(p):
    eredmeny = [["Elégtelen", 0 , 59],["Elégséges", 60, 69],["Közepes", 70, 79],["Jó", 80, 89],["Jeles", 90, 100]]
    for i in eredmeny:
        if i[1] <= p <= i[2]:
            print(i[0]) 

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in xs:
    szamol(i)
szamol(int(input("Számot:")))