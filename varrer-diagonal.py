from stanfordkarel import *

#Varrer o mundo com um padrão de varredura diagonal


def mover_disquete():
    move()
    move()
    move()
    move()
    move()
    move()
    move()

def ajeitar_disquete():
    turn_left()
    turn_left()
    turn_left()

def um():
    move()
    ajeitar_disquete()

def dois():
    move()
    move()
    ajeitar_disquete()

def tres():
    move()
    move()
    move()
    ajeitar_disquete()

def quatro():
    move()
    move()
    move()
    move()
    ajeitar_disquete()

def cinco():
    move()
    move()
    move()
    move()
    move()
    ajeitar_disquete()

def seis():
    move()
    move()
    move()
    move()
    move()
    move()
    ajeitar_disquete()

def sete():
    mover_disquete()
    ajeitar_disquete()

def primeira_sequencia():
    um()
    um()
    um()
    um()

def segunda_sequencia():
    dois()
    dois()
    dois()
    dois()

def terceira_sequencia():
    tres()
    tres()
    tres()
    tres()

def quarta_sequencia():
    quatro()
    quatro()
    quatro()
    quatro()

def quinta_sequencia():
    cinco()
    cinco()
    cinco()
    cinco()

def sexta_sequencia():
    seis()
    seis()
    seis()
    seis()

def setima_sequencia():
    sete()
    sete()
    sete()
    ajeitar_disquete()

def main():  
    turn_left()
    mover_disquete()
    ajeitar_disquete()

    primeira_sequencia()
    segunda_sequencia()
    terceira_sequencia()
    quarta_sequencia()
    quinta_sequencia()
    sexta_sequencia()
    setima_sequencia()

if __name__ == "__main__":
    run_karel_program()