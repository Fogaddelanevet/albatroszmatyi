#print("szeretem a pitont"*1000)
#ev=["Az év 1. hónapja januar","Az év 2. hónapja.februar","Az év 3. hónapja marcius","Az év 4. hónapja aprilis","Az év 5. hónapja majus","Az év 6. hónapja junius","Az év 7. hónapja julius","Az év 8. hónapja augusztus","Az év 9. hónapja szeptember","Az év 10. hónapja oktober","Az év 11. hónapja november","Az év 12. hónapja december"]
#for a in ev: 
 #   print(a)
#3.4 feladat
#körbe-körbe forog,balra



xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in xs:
    print(i)
print(" ")
def new_func(xs):
    for i in xs:
        print(i*i)

new_func(xs)

valtozo=0

def new_func1(xs, valtozo):
    for i in range(0, len(xs)):
        valtozo=valtozo + xs[i]
        
        #print(valtozo)

new_func1(xs, valtozo)


szorzas=0

for j in xs:
    szorzas=xs[0]*xs[1]*xs[2]*xs[3]*xs[4]*xs[5]*xs[6]*xs[7]*xs[8]
print(szorzas)



