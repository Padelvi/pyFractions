from math import fmod

def div_con_resto(a: int | float ,b: int | float):
    if isinstance(a,int) and isinstance(b,int):
        return a//b, a%b
    else:
        return a//b, fmod(a,b)

if __name__ == "__main__":
    while True:
        numerator, denominator = tuple(map(int,input().split()))
        print(div_con_resto(numerator, denominator))