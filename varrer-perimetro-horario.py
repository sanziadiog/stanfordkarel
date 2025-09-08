from stanfordkarel import *

#Varrer o perímetro do mundo no sentido horário

def mover_disquete():
    move()
    move()
    move()
    move()
    move()
    move()
    move()

def orientacao():
    turn_left()
    turn_left()
    turn_left()

def movimento_completo():
    mover_disquete()
    orientacao()
    mover_disquete()
    orientacao()
    mover_disquete()
    orientacao()
    mover_disquete()

def fim():
    turn_left()
    turn_left()

def main():
    turn_left()
    movimento_completo()
    fim()

if __name__ == "__main__":
    run_karel_program()
