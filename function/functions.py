import time
import os



def maquina_de_escrever(texto):
    for letra in texto:
        print(letra, end='', flush=True) 
        time.sleep(0.10) 
    print() 

def limpaC():
    os.system('cls')


def logo(texto):
    for letra in texto:
        print(letra, end='', flush=True) 
        time.sleep(0.010) 
    print() 

def limpaC():
    os.system('cls')
limpaC()


import time

def loading():
    for i in range(101):
        barra_de_progresso = "[" + "█" * i + " " *(100 - i) + "]"
        print(f"\r{i}% {barra_de_progresso}", end="")
        time.sleep(0.05)  
    limpaC()




