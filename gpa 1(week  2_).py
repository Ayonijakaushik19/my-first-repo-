a,b,c=[int(x) for x in input().split()]
if a>b and a>c:
    if a**2==b**2+c**2:
         print("YES")
    else:
        print("NO")
elif b>a and b>c:
    if b**2==a**2+c**2:
        print("YES")
    else:
        print("NO")
elif c>a and c>b:
    if c**2==a**2+b**2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
