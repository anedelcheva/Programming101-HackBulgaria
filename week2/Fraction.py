from fractions import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = int(numerator / gcd(numerator, denominator))
        self.denominator = int(denominator / gcd(numerator, denominator))

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        elif self.numerator == 0:
            return 0
        else:
            return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        numer = self.numerator * other.denominator + \
            self.denominator * other.numerator
        denom = self.denominator * other.denominator
        if denom == 1:
            return numer
        elif numer == 0:
            return 0
        else:
            return str(int(numer / abs(gcd(numer, denom)))) + ' / ' + str(int(denom / abs(gcd(numer, denom))))

    def __sub__(self, other):
        numer = self.numerator * other.denominator - \
            self.denominator * other.numerator
        denom = self.denominator * other.denominator
        if denom == 1:
            return numer
        elif numer == 0:
            return 0
        else:
            return str(int(numer / abs(gcd(numer, denom)))) + ' / ' + str(int(denom / abs(gcd(numer, denom))))

    def __mul__(self, other):
        numer = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        if denom == 1:
            return numer
        elif numer == 0:
            return 0
        else:
            return str(int(numer / abs(gcd(numer, denom)))) + " / " + str(int(denom / abs(gcd(numer, denom))))

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator


f1 = Fraction(1, 2)
f2 = Fraction(2, 4)
f3 = Fraction(2, 2)
print (f3)
print (f1 - f2)
print (f1 * f2)
print (f1 == f2)
