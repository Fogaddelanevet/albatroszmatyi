def derekszog(a,b,c):
    if a*a+b*b == c*c and c*c-a*a== b*b and c*c - b*b == a*a :
        return True
    else:
        return False
print(derekszog(int(input("irjbe egy szamot")),int(input("irjbe egy masik szamot")),int(input("harmadik oldal"))))
