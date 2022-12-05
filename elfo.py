from personaje import Personaje

class Elfo(Personaje):
    def __init__(self, nombre, raza, arma, vida, dmg, bonificacion, reino):
        super().__init__(nombre, raza, arma, vida, dmg, bonificacion)
        self.__reino = reino

    def __str__(self):
        return super().__str__()+"Reino: {}".format(self.__reino)

    def GetReino(self):
        return self.__reino
    def SetReino(self, reino):
        self.__reino = reino
    
    def Historia(self):
        return f'Se les considera seres con poderes mágicos y belleza sobrenatural que pueden ayudar o molestar a los humanos. Originalmente se trataba de una deidad menor de la fertilidad y se les representaba como hombres y mujeres jóvenes, de gran belleza que viven en el bosque, cuevas o fuentes'
    
    def Victoria(self, nombre):
        return f'{nombre} HA GANADO'

    def Derrota(self, nombre):
        return f'{nombre} ha sido derrotado \n{Elfo.Historia(self)}'

    def QuitaVida(self, vida):
        vida = int((vida*90)/100)
        return vida