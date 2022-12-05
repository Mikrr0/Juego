from enano import Enano
from elfo import Elfo
from humano import Humano
import random
import os

lista_pj = []
lista_enemy = []


def mostrar(lista):
    for i in range(len(lista)):
        print(lista[i])

def golpe():
    nombre_player = lista_pj[0].GetNombre()
    vida_player = lista_pj[0].GetVida()
    dmg_player = lista_pj[0].GetDamage()
    nombre_enemigo = lista_enemy[0].GetNombre()
    vida_enemigo = lista_enemy[0].GetVida()
    dmg_enemigo = lista_enemy[0].GetDamage()

    x = 0
    cont = 0
    while x == 0:
        vida_enemigo = vida_enemigo - dmg_player
        vida_player = vida_player - dmg_enemigo
        cont = cont+1
        print(f'----------------Ronda Nº{cont}----------------')
        if vida_player <= 0 and vida_enemigo <= 0:
            print("AMBOS PARTICIPANTES SE HAN AGOTADO, SE HA\n     DECLARADO EMPATE, BUEN COMBATE")
            x=1
        else:
            if vida_enemigo >= 0:
                print(f'{nombre_player} ha realizado {dmg_player} de daño a {nombre_enemigo}\nA {nombre_enemigo} le queda {vida_enemigo} de vida restante') 
            else:
                vida_enemigo = 0
                if raza == "Enano":
                    player = Enano(nombre_player, raza, arma, vida_player, dmg_player, bonificacion, clan)
                if raza == "Elfo":
                    player = Elfo(nombre_player, raza, arma, vida_player, dmg_player, bonificacion, reino)
                if raza == "Humano":
                    player = Humano(nombre_player, raza, arma, vida_player, dmg_player, bonificacion, familia)
                if elegir == "Enano":
                    enemigo = Enano(nombre_enemigo, "Enano", "Catalizador", vida_enemigo, dmg_enemigo, 0, "Ered Luin")
                if elegir == "Elfo":
                    enemigo = Elfo(nombre_enemigo, "Elfo", "Arco", vida_enemigo, dmg_enemigo, 0, "Bosque Negro")
                if elegir == "Humano":
                    enemigo = Humano(nombre_enemigo, "Humano", "Espada", vida_enemigo, dmg_enemigo, 0, "Dúnedain")
                print(player.Victoria(nombre_player))
                print(enemigo.Derrota(nombre_enemigo))
                x = 1
                
            if vida_player >= 0:
                print(f'{nombre_enemigo} ha realizado {dmg_enemigo} de daño a {nombre_player}\nA {nombre_player} queda {vida_player} de vida restante')
            else:
                vida_player = 0
                if raza == "Enano":
                    player = Enano(nombre, raza, arma, vida_player, dmg_player, bonificacion, clan)
                if raza == "Elfo":
                    player = Elfo(nombre, raza, arma, vida_player, dmg_player, bonificacion, reino)
                    player.Historia()
                if raza == "Humano":
                    player = Humano(nombre, raza, arma, vida_player, dmg_player, bonificacion, familia)
                    player.Historia()
                if elegir == "Enano":
                    enemigo = Enano(nombre_enemigo, "Enano", "Catalizador", vida_enemigo, dmg_enemigo, 0, "Ered Luin")
                if elegir == "Elfo":
                    enemigo = Elfo(nombre_enemigo, "Elfo", "Arco", vida_enemigo, dmg_enemigo, 0, "Bosque Negro")
                if elegir == "Humano":
                    enemigo = Humano(nombre_enemigo, "Humano", "Espada", vida_enemigo, dmg_enemigo, 0, "Dúnedain")
                print(enemigo.Victoria(nombre_enemigo))
                print(player.Derrota(nombre_player))
                x = 1
            
def IngresaDatos():
    global player, enemigo, elegir, arma, raza, bonificacion, clan, familia, reino, nombre

    nombre = str(input("Ingrese su nombre:\n")).capitalize()

    while True:
        try:
            raza = str(input("Elige tu raza:\n[Enano]\n[Elfo]\n[Humano]\n")).capitalize()
            if raza == "Enano" or raza == "Elfo" or raza == "Humano":
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Ha ingresado un número")

    while True:
        try:
            arma = str(input("Elige tu arma:\n[Espada]\n[Mandoble]\n[Arco]\n[Catalizador]\n")).capitalize()
            if arma == "Espada" or arma == "Mandoble" or arma == "Arco" or arma == "Catalizador":
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Ha ingresado un número")

    if raza == "Enano":
        vida = 500
        base_enano = 6
        bonificacion = 0
        clan = input("Escriba nombre para su clan:\n")
        if arma == "Espada":
            espada = 10
            dmg = base_enano*espada
        if arma == "Mandoble":
            espada = 8
            dmg = base_enano*mandoble
        if arma == "Arco":
            arco = 11
            dmg = base_enano*arco
        if arma == "Catalizador":
            catalizador = 12
            dmg = base_enano*catalizador
        player = Enano(nombre, raza, arma, vida, dmg, bonificacion, clan)
        while True:
            try :
                preg_bono = str(input("Ha encontrado un artefacto de AUMENTO DE VIDA, ¿Desea equiparlo?\n[SI]\n[NO]\n")).capitalize()
                if preg_bono == "Si":
                    vida = player.AumentaVida(vida)
                    player = Enano(nombre, raza, arma, vida, dmg, bonificacion, clan)
                    break
                if preg_bono == "No":
                    break
                if preg_bono != "Si" or preg_bono != "No":
                    print("Se ha roto el artefacto")
                    break
            except ValueError:
                print("Ha ingresado un número")


    if raza == "Elfo":
        vida = 500
        base_elfo = 8
        bonificacion = 0
        reino = input("Escriba nombre para su reino:\n")
        if arma == "Espada":
            espada = 9
            dmg = base_elfo*espada
        if arma == "Mandoble":
            mandoble = 7
            dmg = base_elfo*mandoble
        if arma == "Arco":
            arco = 12
            dmg = base_elfo*arco
        if arma == "Catalizador":
            catalizador = 10
            dmg = base_elfo*catalizador
        player = Elfo(nombre, raza, arma, vida, dmg, bonificacion, reino)
        while True:
            try :
                preg_bono = str(input("Ha encontrado un artefacto MISTERIOSO ¿Desea equiparlo?\n[SI]\n[NO]\n")).capitalize()
                if preg_bono == "Si":
                    vida = player.QuitaVida(vida)
                    player = Elfo(nombre, raza, arma, vida, dmg, bonificacion, reino)
                    print(vida)
                    break
                if preg_bono == "No":
                    break
                if preg_bono != "Si" or preg_bono != "No":
                    print("Se ha roto el artefacto")
                    break
            except ValueError:
                print("Ha ingresado un número")

    if raza == "Humano":
        vida =500
        base_humano = 7
        bonificacion = 0
        familia = input("Escriba el nombre para su familia:\n")
        if arma == "Espada":
            espada = 12 
            dmg = base_humano*espada
        if arma == "Mandoble":
            mandoble = 11
            dmg = base_humano*mandoble
        if arma == "Arco":
            arco = 9
            dmg = base_humano*arco
        if arma == "Catalizador":
            catalizador = 8
            dmg = base_humano*catalizador
        player = Humano(nombre, raza, arma, vida, dmg, bonificacion, familia)
        while True:
            try :
                preg_bono = str(input("Ha encontrado un artefacto de SUPER BONO ¿Desea equiparlo?\n[SI]\n[NO]\n")).capitalize()
                if preg_bono == "Si":
                    dmg = player.SuperBono(dmg)
                    player = Humano(nombre, raza, arma, vida, dmg, bonificacion, familia)
                    break
                if preg_bono == "No":
                    break
                if preg_bono != "Si" or preg_bono != "No":
                    print("Se ha roto el artefacto")
                    break
            except ValueError:
                print("Ha ingresado un número")

    while True:
        try:
            elegir = str(input("Seleccione su enemigo:\n[Enano]\n[Elfo]\n[Humano]\n")).capitalize()
            if elegir == "Enano" or elegir == "Elfo" or elegir == "Humano":
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Ha ingresado un número")

    if elegir == "Enano":
        enemigo = Enano("Gimli", "Enano", "Catalizador", 500, 72, 0, "Ered Luin")
    if elegir == "Elfo":
        enemigo = Elfo("Legolas", "Elfo", "Arco", 500, 96, 0, "Bosque Negro")
    if elegir == "Humano":
        enemigo = Humano("Aragorn", "Humano", "Espada", 500, 84, 0, "Dúnedain")
    
    lista_pj.append(player)
    lista_enemy.append(enemigo)

def main():
    x = 0
    while x == 0:
        IngresaDatos()
        golpe()

        x = int(input("\n¿Desea comenzar otra partida?\n  PRESIONE [0] PARA SEGUIR JUGANDO\npresione cualquier tecla para salir"))
main()