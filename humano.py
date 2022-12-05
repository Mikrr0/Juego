from personaje import Personaje

class Humano(Personaje):
    def __init__(self, nombre, raza, arma, vida, dmg, bonificacion, familia):
        super().__init__(nombre, raza, arma, vida, dmg, bonificacion)
        self.__familia = familia
    
    def __str__(self):
        return super().__str__()+"Familia: {}".format(self.__familia)

    def Getfamilia(self):
        return self.__familia
    def SetFamilia(self, familia):
        self.__familia = familia
    
    def Historia(self):
        return f'Como ya dijimos, nuestra especie, Homo sapiens, pertenece al grupo de los primates, que han estado asociados con las selvas de tipo tropical casi desde su origen en el Cretácico, hace más de 65 millones de años, donde aparecieron algunos pequeños mamíferos que vivían en los árboles.'

    def Victoria(self, nombre):
        return f'{nombre} HA GANADO'

    def Derrota(self, nombre):
        return f'{nombre} ha sido derrotado'

        
    def SuperBono(self, dmg):
        while True:
            try:
                bono = int(input("Elija un número del 5al 15\n"))
                if bono >=50 and bono <=100:
                    print("El artefacto le implementa ",bono," puntos de ataque")
                    break
                else:
                    print("El artefacto se ha roto")
                    bono = 0
                    break
            except:
                print("Se ha roto el artefacto")
        return dmg + bono
