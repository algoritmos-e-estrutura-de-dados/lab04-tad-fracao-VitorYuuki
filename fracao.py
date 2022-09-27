import math

class Fracao:
    numerador = 1
    denominador = 1

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def add(self, fracao):
        num = (self.numerador * fracao.denominador) + (self.denominador *
                                                       fracao.numerador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def sub(self, fracao):
        num = (self.numerador * fracao.denominador) - (self.denominador *
                                                       fracao.numerador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def mul(self, fracao):
        num = self.numerador * fracao.numerador
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def solve(self):
        return self.numerador / self.denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def simplify(self):
        common_divisor = math.gcd(self.numerador, self.denominador)
        numerador = self.numerador / common_divisor
        denominador = self.denominador / common_divisor
        return Fracao(numerador, denominador)


fracao1 = Fracao(10, 5)
fracao2 = Fracao(1, 7)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.mul(fracao2)
fracao6 = fracao1.simplify()
fracao7 = fracao2.simplify()

print(f"fracao1: {fracao1}")
print(f"fracao1: {fracao1.solve()}")
print(f"fracao2: {fracao2}")
print(f"fracao2: {fracao2.solve()}")
print(f"fracao3: {fracao3}")
print(f"fracao4: {fracao4}")
print(f"fracao5: {fracao5}")
print(f"fracao6: {fracao6}")
print(f"fracao7: {fracao7}")