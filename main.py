#Juego del cachipun
import random

cachipun = ('piedra', 'papel', 'tijera') 
print("*"*50)
rondas_max = int(input("Ingrese el numero de rondas que quiere jugar: "))
computer_option = random.choice(cachipun)
turnos_ganados_user = 0
turnos_ganados_computer = 0
rondas = 0

while rondas <= rondas_max:
    user_option = input("Eliga, piedra, papel o tijera => ")
    user_option = user_option.lower() 
    
    rondas += 1
    if not user_option in cachipun:
        print("Opcion invalida, recuerde solo puede elegir piedra, papel o tijera")
        continue
    
    
    print("*"*50)
    print("user_option =>", user_option)
    print("computer_option =>", computer_option)
    print("*"*50)
    print("rondas totales =>", rondas)
    print("rondas ganadas por el usuario =>", turnos_ganados_user)
    print("rondas ganadas por la computadora =>", turnos_ganados_computer)
    
    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera")
            print("user wins")
            turnos_ganados_user += 1
        else:
            computer_option == "papel"
            print("papel gana a piedra")
            print("computer wins") 
            turnos_ganados_computer += 1
        
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra")
            print("user wins")
            turnos_ganados_user += 1
        else:
           computer_option == "tijera"
           print("tijera gana a papel")
           print("computer wins")
           turnos_ganados_computer += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("user wins")
            turnos_ganados_user += 1
        else:
           computer_option == "piedra"
           print("piedra gana a tijera")
           print("computer wins") 
           turnos_ganados_computer += 1 

    if rondas == rondas_max and turnos_ganados_user > turnos_ganados_computer:
        print("juego finalizado")
        print("El usuario gano el juego")
        break
    elif rondas == rondas_max and turnos_ganados_computer > turnos_ganados_user:
        print("juego finalizado")
        print("La computadora gano el juego")
        break
    elif rondas == rondas_max and turnos_ganados_computer == turnos_ganados_user:
        print("juego finalizado")
        print("El juego termino en empate")
        break

       

    

    
        
        
        
    
        


           