#Juego de piedra, papel o tijera
import random

opciones = ('piedra', 'papel', 'tijera') 

user_wins = 0
computer_wins = 0
rondas = 1

while True:
    
    print("*"*50)
    print('RONDAS', rondas)
    print("*"*50)
    print("victorias del usuario =>", user_wins)
    print("victorias de la computadora =>", computer_wins)
    print("*"*50)
    
    user_option = input("Eliga, piedra, papel o tijera => ")
    user_option = user_option.lower() 
    rondas += 1
    
    if not user_option in opciones:
        print("Opcion invalida, recuerde solo puede elegir piedra, papel o tijera")
        continue
    
    computer_option = random.choice(opciones)
    
    print("user_option =>", user_option)
    print("computer_option =>", computer_option)
    
    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera")
            print("user wins")
            user_wins += 1
        else:
            computer_option == "papel"
            print("papel gana a piedra")
            print("computer wins") 
            computer_wins += 1
        
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra")
            print("user wins")
            user_wins += 1
        else:
           computer_option == "tijera"
           print("tijera gana a papel")
           print("computer wins")
           computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("user wins")
            user_wins += 1
        else:
           computer_option == "piedra"
           print("piedra gana a tijera")
           print("computer wins") 
           computer_wins += 1 

    if user_wins == 2:
        print("juego finalizado")
        print("El usuario gano el juego")
        break
    if computer_wins == 2:
        print("juego finalizado")
        print("La computadora gano el juego")
        break
   

       