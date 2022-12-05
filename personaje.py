class Personaje():
    def __init__(self, nombre, raza, arma, vida, dmg, bonificacion):
        self.__nombre = nombre
        self.__raza = raza
        self.__arma = arma
        self.__vida = vida
        self.__dmg = dmg
        self.__bonificacion = bonificacion
    
    def __str__(self):
        return "Nombre: {}\nRaza: {}\nArma: {}\nVida: {}\nDaño: {}\nBonificación: {}\n".format(self.__nombre, self.__raza, self.__arma, self.__vida, self.__dmg, self.__bonificacion)
    
    def GetNombre(self):
        return self.__nombre
    def SetNombre(self, nombre):
        self.__nombre = nombre

    def GetRaza(self):
        return self.__raza
    def SetRaza(self, raza):
        self.__raza = raza
    
    def GetArma(self):
        return self.__arma
    def SetArma(self, arma):
        self.__arma = arma

    def GetVida(self):
        return self.__vida
    def SetVida(self, vida):
        self.__vida = vida
    
    def GetDamage(self):
        return self.__dmg
    def SetDamage(self, dmg):
        self.__dmg = dmg
    
    def GetBonificacion(self):
        return self.__bonificacion
    def SetBonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def Combate():
        pass

    def Historia():
        pass

    def Victoria(self):
        return f'{self.__nombre} HA GANADO'

    def Derrota(self):
        return f'{self.__nombre} ha sido derrotado'

    def MensajeInicial():
        pass