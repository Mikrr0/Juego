from personaje import Personaje

class Enano(Personaje):
    def __init__(self, nombre, raza, arma, vida, dmg, bonificacion, clan):
        super().__init__(nombre, raza, arma, vida, dmg, bonificacion)
        self.__clan = clan
    
    def __str__(self):
        return super().__str__()+"Clan: {} ".format(self.__clan)

    def GetClan(self):
        return self.__clan
    def SetClan(self, clan):
        self.__clan = clan
    
    def Historia(self):
        return f'Los Enanos sitúan el comienzo de su historia en el despertar de los primeros de su raza, gobernados directamente por un panteón de dioses que caminaban entre ellos. De estos, los más importantes son Grungni,Grimnir y Valaya, y los Enanos creen que descienden directamente de estos antepasados primigenios.'

    def Victoria(self, nombre):
        return f'{nombre} HA GANADO'

    def Derrota(self, nombre):
        return f'{nombre} ha sido derrotado'

    def AumentaVida(self, vida):
        while True:
            try:
                bono = int(input("Elija un número del 50 al 100\n"))
                if bono >=50 and bono >=100:
                    print("El artefacto le implementa ",bono," puntos de vida")
                    break
                else:
                    print("El artefacto se ha roto")
                    bono = 0
                    break
            except:
                print("Se ha roto el artefacto")

        return vida + bono