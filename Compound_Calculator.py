def compound(yrs,princ,contrib):
    for n in range(0,yrs):
        r = float(input(f"Interest rate for year {n}: "))
        princ = (princ+contrib)*(1+r)
    return princ

year = int(input("How many years?: "))
principle = float(input("What is the principle?: "))
contrib = float(input("Yearly contribution?: "))
print(compound(year,principle,contrib))
