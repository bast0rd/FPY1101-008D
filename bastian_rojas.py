import os
import time

os.system("cls")
contador = 0
contador2 = 0
contador3 = 0
contador4 = 0
cant_total = 0
pikachu_roll = 4500
otaku_roll = 5000
pulpo_roll = 5200
anquila_roll = 4800
descuento = 0.1
descuento_aceptado = 0
cant_anguila = 0
cant_otaku = 0
cant_pika = 0
cant_pulpo = 0
while contador2 == 0:
    contador4 = 0
    while contador == 0:
        while contador == 0:
            try:
                print("bienvenido a la tineda de sushi. \nestan son las opciones del menu")
                print("1)pikachu roll \t\t\t$4500 \n2)otaku roll \t\t\t$5000 \n3)pulpo venenoso roll \t\t$5200 \n4)Anguila electrica roll \t$4800 \n5)terminar pedido")
                opcion1 = int(input("ingrese su opcion: "))
            except ValueError:
                print("porfavor solo ingrese la opcion no una palabra.")
                time.sleep(2)
                os.system("cls")
            else:
                print(f"opcion eleguida {opcion1} espere")
                time.sleep(1)
                os.system("cls")
                break
        if opcion1 == 1:
            while contador == 0:
                try:
                    print("cuantos pikachu roll va a llevar?")
                    cant_pika = int(input("ingrese cantidad: "))
                except ValueError:
                    print("no es una cantidad.")
                    time.sleep(1)
                    os.system("cls")
                else:
                    time.sleep(1)
                    os.system("cls")
                    break
        elif opcion1 == 2:
            while contador == 0:
                try:
                    print("cuantos otaku roll va a llevar?")
                    cant_otaku = int(input("ingrese cantidad: "))
                except ValueError:
                    print("no es una cantidad.")
                    time.sleep(1)
                    os.system("cls")
                else:
                    time.sleep(1)
                    os.system("cls")
                    break
        elif opcion1 == 3:
            while contador == 0:
                try:
                    print("cuantos pulpo venenoso roll va a llevar?")
                    cant_pulpo = int(input("ingrese cantidad: "))
                except ValueError:
                    print("no es una cantidad.")
                    time.sleep(1)
                    os.system("cls")
                else:
                    time.sleep(1)
                    os.system("cls")
                    break
        elif opcion1 == 4:
            while contador == 0:
                try:
                    print("cuantos Anguila electrica roll va a llevar?")
                    cant_anguila = int(input("ingrese cantidad: "))
                except ValueError:
                    print("no es una cantidad.")
                    time.sleep(1)
                    os.system("cls")
                else:
                    time.sleep(1)
                    os.system("cls")
                    break
        elif opcion1 == 5:
            while contador == 0:
                try:
                    salir = int(input("esta seguro que quiere salir de comprar? \n1) salir \n2) seguir comprando \ndiga la opcion: "))
                except ValueError:
                    print("no es una opcion valida.")
                    time.sleep(1)
                    os.system("cls")
                else:
                    if salir == 1:
                        print("saliendo de comprar, aqui esta su boleta.")
                        contador = 1
                        time.sleep(1)
                        os.system("cls")
                    elif salir == 2:
                        print("volviendo a comprar.")
                        time.sleep(1)
                        os.system("cls")
                        break
        else:
            print("no es una opcion valida.")
            time.sleep(1)
            os.system("cls")
    while contador == 1:
        while contador3 == 0:
            try:
                print("tiene un codigo de descuento? \n1) si \n2) no")
                codigo1 = int(input("ingrese la opcion: "))
            except ValueError:
                print("porfavor no ingresar palabras")
                time.sleep(1)
                os.system("cls")
            else:
                contador3 = 1
                time.sleep(1)
                os.system("cls")
                break
        if codigo1 == 1:
            codigo_des = input("ingrese codigo de descuento: ")
            if codigo_des == "soyotaku":
                print("codigo ingresado.")
                descuento_aceptado = descuento
                contador = 2
                time.sleep(1)
                os.system("cls")
            else:
                try:
                    print("codigo no valido, desea volver a intentar? \n1) si \n2) no (imprimir boleta)")
                    intentar = int(input("ingrese la opcion: "))
                except ValueError:
                    print("no ingresar palabras.")
                    time.sleep(1)
                    os.system("cls")
                if intentar == 1:
                    time.sleep(1)
                    os.system("cls")
                elif intentar == 2:
                    contador = 2
                    time.sleep(1)
                    os.system("cls")
        elif codigo1 == 2:
            contador = 2
            time.sleep(1)
            os.system("cls")
    if descuento_aceptado == 0.1:
        cant_total = (cant_pulpo * pulpo_roll) + (cant_anguila * anquila_roll) + (cant_pika * pikachu_roll) + (otaku_roll * cant_otaku)
        print("******************************")
        print(f"TOTAL PRODUCTOS \t{cant_anguila + cant_otaku + cant_pika + cant_pulpo}")
        print("******************************")
        print(f"pikachu roll: \t{cant_pika} \notaku roll \t{cant_otaku} \npulpo venenoso roll \t{cant_pulpo} \nanguila electrica roll \t{cant_anguila}")
        print("******************************")
        print(f"subtotal a pagar: {(cant_pulpo * pulpo_roll) + (cant_anguila * anquila_roll) + (cant_pika * pikachu_roll) + (otaku_roll * cant_otaku)}")
        print(f"descuento por codgio: {cant_total * descuento}")
        restades = cant_total * descuento
        print(f"TOTAL: {cant_total - restades}")
        print("\n\ndesea vovler a comprar? \n1) si \n2) no")
        while contador4 == 0:
            try:
                volver = int(input("ingresar opcion: "))
            except ValueError:
                print("no es una opcion valida")
            else:
                if volver == 1:
                    contador = 0
                    contador2 = 0
                    contador3 = 0
                    contador4 = 1
                    cant_total = 0
                    descuento = 0.1
                    descuento_aceptado = 0
                    cant_anguila = 0
                    cant_otaku = 0
                    cant_pika = 0
                    cant_pulpo = 0
                    time.sleep(1)
                    os.system("cls")
                    break
                elif volver == 2:
                    print("gracias por comprar.")
                    time.sleep(1)
                    contador4 = 1
                    contador2 = 1
                else:
                    print("no es niguna opcion")
    elif descuento_aceptado == 0:
        cant_total = (cant_pulpo * pulpo_roll) + (cant_anguila * anquila_roll) + (cant_pika * pikachu_roll) + (otaku_roll * cant_otaku)
        print("******************************")
        print(f"TOTAL PRODUCTOS \t{cant_anguila + cant_otaku + cant_pika + cant_pulpo}")
        print("******************************")
        print(f"pikachu roll: \t{cant_pika} \notaku roll \t{cant_otaku} \npulpo venenoso roll \t{cant_pulpo} \nanguila electrica roll \t{cant_anguila}")
        print("******************************")
        print(f"subtotal a pagar: {(cant_pulpo * pulpo_roll) + (cant_anguila * anquila_roll) + (cant_pika * pikachu_roll) + (otaku_roll * cant_otaku)}")
        print(f"TOTAL: {cant_total}")
        print("\n\ndesea vovler a comprar? \n1) si \n2) no")
        while contador4 == 0:
            try:
                volver = int(input("ingresar opcion: "))
            except ValueError:
                print("no es una opcion valida")
            else:
                if volver == 1:
                    contador = 0
                    contador2 = 0
                    contador3 = 0
                    contador4 = 1
                    cant_total = 0
                    descuento = 0.1
                    descuento_aceptado = 0
                    cant_anguila = 0
                    cant_otaku = 0
                    cant_pika = 0
                    cant_pulpo = 0
                    time.sleep(1)
                    os.system("cls")
                    break
                elif volver == 2:
                    print("gracias por comprar.")
                    time.sleep(1)
                    contador2 = 1
                    contador4 = 1
                else:
                    print("no es niguna opcion")