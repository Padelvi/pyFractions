from math import gcd, ceil, log10, copysign
# from divlarga import expr_decimal

class Fraction:
    @staticmethod
    def _float_to_numdem(f: float) -> tuple[int,int]:
        int_digits: int = ceil(log10(abs(f)))
        dec_digits: int = len(str(f)) - int_digits - 1
        power = pow(10,dec_digits)
        return int(f*power), power

    def _float_to_fraction(self, f: float):
        return Fraction(*self._float_to_numdem(f))

    @staticmethod
    def _ints_to_numdem(n: int, d: int) -> tuple[int,int]:
        if d == 0:
            raise ZeroDivisionError("The denominator cannot be zero!")

        num = abs(n)
        dem = abs(d)

        sign = int(copysign(1,d*n))
        divide = gcd(num, dem)

        num //= divide
        dem //= divide

        num *= sign

        return num, dem

    def __init__(self, n: int | float, d: int | None = None) -> None:
        if isinstance(n,int) and isinstance(d,int):
            self.num, self.dem = self._ints_to_numdem(n,d)
        elif d is None:
            if isinstance(n, float):
                self.num, self.dem = self._float_to_numdem(n)
            elif isinstance(n,int):
                self.num, self.dem = n, 1
            else:
                raise TypeError("Arguments must be two integers or a float!")
        else:
            raise TypeError("Arguments must be two integers or a float!")

    def __str__(self) -> str:
        if self.dem == 1:
            return str(self.num)
        return f"{self.num}/{self.dem}"

    def __bool__(self) -> bool:
        return self.num == 0

    def __int__(self) -> int:
        return self.num // self.dem

    def __float__(self) -> float:
        return self.num / self.dem

    # Hay que implementarlo en divlarga.py
    def decimals(self) -> str:
        return "lala"

    def __repr__(self) -> str:
        return f"<Rational number {str(self)}, with decimal representation {self.decimals()}>"

    def __add__(self, other):
        if isinstance(other,Fraction):
            return Fraction(self.num*other.dem + self.dem*other.num, self.dem * other.dem)
        elif isinstance(other,int):
            return Fraction(self.num + self.dem*other, self.dem)
        elif isinstance(other,float):
            return self + self._float_to_fraction(other)
        else:
            return NotImplemented

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other,Fraction):
            return Fraction(self.num * other.num, self.dem * other.dem)
        elif isinstance(other,int):
            return Fraction(self.num * other, self.dem)
        elif isinstance(other,float):
            return self * self._float_to_fraction(other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        fdiv = float(self // other)
        if fdiv is NotImplemented:
            return float(self)/other
        return fdiv
    
    def __floordiv__(self, other):
        if isinstance(other, int):
            return Fraction(self.num, self.dem*other)
        elif isinstance(other, Fraction):
            return Fraction(self.num*other.dem, self.dem*other.num)
        else:
            return NotImplemented

    def inverse(self):
        return Fraction(self.dem,self.num)