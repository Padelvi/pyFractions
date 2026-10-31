from typing import Any
from math import gcd, floor

# Ver cuántas veces x tiene a un factor (count), y ver el producto del resto de factores de x (n)
def eliminate(x: int, divisor: int) -> tuple[int,int]:
    n = x
    count = 0
    if divisor > n:
        return x, 0
    while n % divisor:
        n //= divisor
        count += 1
    return n, count

def fractionToDecimal(numerator: int, denominator: int) -> str | Any:
    def format(result):
        return f"{result}"

    div = numerator/denominator
    if div == int(div):
        return format(int(div))

    g = gcd(numerator, denominator)
    r_num, r_dem = numerator//g, denominator//g
    
    i, count2 = eliminate(r_dem,2)
    elim_dem, count5 = eliminate(i,5)

    print((g,r_num,r_dem,"",count2,i,"",count5,elim_dem))

    if elim_dem == 1:
        # Exacto: r_dem no tiene factores primos distinos de 2 y 5
        return format(div)
    elif elim_dem == r_dem:
        print(f"Puro: {div}")
        return (i,elim_dem, r_dem, r_num)
        # Periódico puro: r_dem solo tiene factores primos distinos de 2 y 5
        dec = str(div - floor(div))[2:]
        for l_prueba in range(1,r_dem):
            p = dec[:l_prueba]
            for j in range(l_prueba,len(dec),l_prueba):
                try:
                    new_p = dec[j:j+l_prueba]
                except IndexError:
                    bien = True
                    break
                if new_p != p:
                    bien = False
                    break
            else:
                bien = True
            if bien:
                return f"{floor(div)}.({p})"+ str(elim_dem)
    else:
        # Periódico mixto
        print(f"Mixto: {div}")
        return (i,elim_dem, r_dem, r_num)
        # Periódico puro: r_dem solo tiene factores primos distintos de 2 y 5

if __name__ == "__main__":
    num, dem = tuple(map(int,input().split()))
    print(fractionToDecimal(num,dem))