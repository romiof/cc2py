class Carro:
    """ IN --> modelo, ano, cor, velocidade máxima"""
    def __init__(self, m, a, c, vm):
        self.modelo     = m
        self.ano        = a
        self.cor        = c
        self.velocidade = 0
        self.velMax     = vm  #Velocidade Máxima

    def imprima(self):
        if self.velocidade == 0: #Parado podemos ver o ano
            print("%s %s %d" %(self.modelo, self.cor, self.ano) )
        elif self.velocidade < self.velMax:
            print("%s %s indo a %d Km/h" %(self.modelo, self.cor, self.velocidade) )
        else:
            print("%s %s indo muito raaaapiiiidoooo !" %(self.modelo, self.cor))

    def acelere(self, v):
        self.velocidade = v
        if self.velocidade > self.velMax: 
            self.velocidade = self.velMax #Velocidade não pode andar maior que o máximo
        self.imprima()
    
    def pare(self):
        self.velocidade = 0
        self.imprima()


def main():
    carro1 = Carro("Brasilia", 1968, 'amarela', 80)
    carro2 = Carro("Fuscao", 1981, 'preto', 95)
    carro3 = Carro("Uno", 1989, "vermelho", 85)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)
    carro3.acelere(45)
    carro3.pare()

main()
