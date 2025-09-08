from stanfordkarel import *

#Varrer o mundo com um padrão de varredura vertical


def mover_disquete():
    move()
    move()
    move()
    move()
    move()
    move()
    move()

def girar_disquete_cima():
    turn_left()
    turn_left()
    turn_left()

def girar_disquete_baixo():
    turn_left()
    move()
    turn_left()

def inicio():
    mover_disquete()
    girar_disquete_cima()
    move()

def meio():
    girar_disquete_cima()
    mover_disquete()
    girar_disquete_baixo()

def fim():
    girar_disquete_cima()
    mover_disquete()
    turn_left()

def main():  
    turn_left()
    inicio()
    meio()
    inicio()
    meio()
    inicio()
    meio()
    inicio()
    fim()

    #turn_left()
    #turn_left()
    #turn_left()
   # mover_disquete()
    #turn_left()
    #turn_left()
    
if __name__ == "__main__":
    run_karel_program()