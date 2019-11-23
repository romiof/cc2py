class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"
        elif (self.a == self.b and self.b != self.c) or (self.c == self.b and self.b != self.a) or (self.a == self.c and self.a != self.b):
            return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            return self.calc_hipotenusa(self.a, self.b, self.c) #self.a ** 2 == self.b ** 2 + self.c ** 2:
        elif self.b > self.a and self.b > self.c:
            return self.calc_hipotenusa(self.b, self.a, self.c)
        else:
            return self.calc_hipotenusa(self.c, self.a, self.b)

    def calc_hipotenusa(self, h, x, y):
        if h ** 2 == x ** 2 + y ** 2:
            return True
        else:
            return False
    
    def semelhantes(self, t):
        t1 = []
        t2 = []
        t3 = []
        t1 = list((self.a, self.b, self.c))
        t2 = list((t.a, t.b, t.c))
        for i in len(t1 - 1):
            # Testa ordem que vai aplicar o operador % MOD
            if t1[i] > t2[i]:
                # Aplica operador % MOD para procurar similaridade
                if t1[i] % t2[i] == 0:
                    t3.append(True)
                else:
                    t3.append(False)
            else:
                # Aplica operador % MOD para procurar similaridade
                if t2[i] % t1[i] == 0:
                    t3.append(True)
                else:
                    t3.append(False)
        t3.sort()
        if t3[0]:
            return True
        else:
            return False

def main():
    t1 = Triangulo(2, 2, 2)
    t2 = Triangulo(4, 4, 4)
    t1.semelhantes(t2)

main()

#t = Triangulo(2, 1, 1)
#t.a
#t.b
#t.c
