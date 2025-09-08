from stanfordkarel import *

#Varrer o mundo com um padrão de varredura horizontal

def mover_disquete():
    move()
    move()
    move()
    move()
    move()
    move()
    move()

def subir_linha():
    turn_left()
    move()
    turn_left()

def ajeitar_disquete():
    turn_left()
    turn_left()
    turn_left()

def sequencia():
    mover_disquete()
    subir_linha()
    mover_disquete()
    ajeitar_disquete()
    move()
    ajeitar_disquete()

def fim():
    mover_disquete()
    subir_linha()
    mover_disquete()
    turn_left()
    turn_left()

def main():  
    sequencia()
    sequencia()
    sequencia()
    fim()

if __name__ == "__main__":
    run_karel_program()