import time
from cowsay import cowsay
from os import system

diccionari={}

def intro():
    from os import system
    from asciimatics.effects import Cycle, Stars
    from asciimatics.renderers import FigletText
    from asciimatics.scene import Scene
    from asciimatics.screen import Screen

    def demo(screen):
        effects = [
            Cycle(
                screen,
                FigletText("El llibre de les acceptacions", font='big'),
                int(screen.height / 2 - 8)),
            Cycle(
                screen,
                FigletText("by Israel", font='big'),
                int(screen.height / 2 + 3)),
            Stars(screen, 200)
        ]
        screen.play([Scene(effects, 500)])
    Screen.wrapper(demo)
    time.sleep(1)
def seleccion():
    opcio = 0
    while opcio < 1 or opcio > 5:
        system("cls")
        mensaje = """Selecciona una opció:
1) Añadir palabra
2) Mostrar palabra
3) Modificar palabra
4) Eliminar el contenido
5) Eliminar el mundo
            """
        print(mensaje)
        opcio = int(input("Selecciona tu opción: "))
        if opcio < 1 or opcio > 5:
            print("Introdueix una opcio valida")
            time.sleep(1)
    return opcio
def casosLibro(opcion):
    match opcion:
        case 1:
            system("cls")
            paraula = str(input("Introdueix una paraule: "))
            especificacioParaula = str(input("Introdueix una especificacio: "))
            definicionParaula = str(input("Introdueix la definicio: "))
            unionDefiEspe = {
                especificacioParaula: definicionParaula
            }
            if paraula in diccionari:
                if especificacioParaula in diccionari[paraula]:
                    print("Has de entrar a modificación per poder modificar el significar d'aquesta paraule.")
                else:
                    diccionari[paraula].update(unionDefiEspe)
            else:
                diccionari[paraula]={}
                if especificacioParaula in diccionari[paraula]:
                    print("Has de entrar a modificación per poder modificar el significar d'aquesta paraule.")
                else:
                    diccionari[paraula].update(unionDefiEspe)
            print(diccionari)
            time.sleep(1)
        case 2:
            system("cls")
            tamany = int(len(diccionari))
            if tamany == 0:
                print("No hi ha cap paraules per mostrar.")
                time.sleep(3)
            else:
                paraulaTrobar=""
                while not paraulaTrobar in diccionari:
                    print("Listat de las paraules per seleccionar: ")
                    for categoria in diccionari:
                        print(categoria)
                    paraulaTrobar = str(input("Introdueix quin paraule vols mostrar: "))
                    if not paraulaTrobar in diccionari:
                        print("Introdueix una paralaule per correcte")
                        time.sleep(3)
                        system("cls")
                    else:
                        system("cls")
                        print("Aqui tens la informacio de la paraule {}: ".format(paraulaTrobar))
                        for n in diccionari[paraulaTrobar].keys():
                            print(n)
                        especifi = str(input("Introdueix que especificacions vols consultar: "))
                        if especifi in diccionari[paraulaTrobar].keys():
                            for clave, valor in diccionari[paraulaTrobar].items():
                                if clave == especifi:
                                    outputMostrar = clave + ": " + valor
                            system("cls")
                            print("Aqui tens el concepte seleccionat amb la vaca: ")
                            print(cowsay(outputMostrar))
                            time.sleep(3)
                        else:
                            print("Introdueix una paraule correcte.")
                            time.sleep(3)
                        time.sleep(3)
        case 3:
            system("cls")
            tamany = int(len(diccionari))
            if tamany == 0:
                print("No hi ha cap paraules per modificar.")
                time.sleep(3)
            else:
                paraulaTrobar=""
                while not paraulaTrobar in diccionari:
                    print("Listat de las paraules per seleccionar: ")
                    for categoria in diccionari:
                        print(categoria)
                    paraulaTrobar = str(input("Introdueix quin paraule vols modificar: "))
                    if not paraulaTrobar in diccionari:
                        print("Introdueix una paralaule per correcte")
                        time.sleep(3)
                        system("cls")
                    else:
                        especificacio=""
                        while not especificacio in diccionari[paraulaTrobar].keys():
                            system("cls")
                            print("Llistat complet de les definicions de {}".format(paraulaTrobar))
                            for n in diccionari[paraulaTrobar].keys():
                                print(n)
                            especificacio = str(input("Introdueix que especificacions vols modificar: "))
                            if especificacio in diccionari[paraulaTrobar].keys():
                                system("cls")
                                canviEspecificacio = str(input("Introdueix la nova definicio de {}: ".format(especificacio)))
                                diccionari[paraulaTrobar][especificacio] = canviEspecificacio
                                system("cls")
                                print("S'ha actualizat, aquí la vaca para que veas: ")
                                for clave, valor in diccionari[paraulaTrobar].items():
                                    if clave == especificacio:
                                        outputMostrar = clave + ": " + valor
                                print(cowsay(outputMostrar))
                                time.sleep(3)
                            else:
                                print("Introdueix una paraule correcte.")
                                time.sleep(3)
        case 4:
            system("cls")
            tamany = int(len(diccionari))
            if tamany == 0:
                print("No hi ha cap paraules per esborrar.")
                time.sleep(3)
            else:
                paraulaTrobar=""
                while not paraulaTrobar in diccionari:
                    print("Listat de las paraules per seleccionar: ")
                    for categoria in diccionari:
                        print(categoria)
                    paraulaTrobar = str(input("Introdueix quin paraule vols accedir per esborrar: "))
                    if not paraulaTrobar in diccionari:
                        print("Introdueix una paralaule per correcte")
                        time.sleep(3)
                        system("cls")
                    else:
                        especificacioEsborrar = ""
                        while not especificacioEsborrar in diccionari[paraulaTrobar].keys():
                            system("cls")
                            print("Llistat complet de les definicions de {}".format(paraulaTrobar))
                            for n in diccionari[paraulaTrobar].keys():
                                print(n)
                            especificacioEsborrar = str(input("Introdueix que especificacions vols esborrar: "))
                            if especificacioEsborrar in diccionari[paraulaTrobar].keys():
                                system("cls")
                                print("S'ha esborrat la definicio {}, de la paraula {}".format(especificacioEsborrar, paraulaTrobar))
                                del diccionari[paraulaTrobar][especificacioEsborrar]
                                time.sleep(3)
                                break
                            else:
                                print("Introdueix una paraule correcte.")
                                time.sleep(3)

                        tamanyEsborrar = int(len(diccionari[paraulaTrobar]))

                if tamanyEsborrar == 0:
                            del diccionari[paraulaTrobar]    
                            
        case 5:
            system("cls")
            print(cowsay("Elegiste este camino."))
            time.sleep(1)
            n=10
            while n>=1:
                system("cls")
                print(cowsay(str(n)))
                time.sleep(1)
                n -= 1

intro()
system("cls")
opcion = 0
while opcion!=5:
    opcion = seleccion()
    casosLibro(opcion)

