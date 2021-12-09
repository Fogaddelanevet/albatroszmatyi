def derekszog(a,b,c):
    if c>b and c>a:
        if a*a+b*b == c*c and c*c-a*a== b*b and c*c - b*b == a*a :
         return True
        else:
            return False
    if b>c and b>a:
        if a*a+c*c == b*b and b*b-a*a== c*c and b*b - c*c == a*a :
         return True
        else:
            return False        
    if a>b and a>c:
        if c*c+b*b == a*a and a*a-b*b== c*c and a*a - b*b == c*c :
         return True
        else:
            return False
print(derekszog(int(input("irjbe egy szamot")),int(input("irjbe egy masik szamot")),int(input("harmadik oldal"))))
