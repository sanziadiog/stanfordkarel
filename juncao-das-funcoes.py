from stanfordkarel import *

#junção das varreduras

#funções gerais aplicadas nas varreduras
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

def ajeitar_passo_disquete():
    turn_left()
    move()
    turn_left()

#especifica da varredura no sentido horário
def movimento_completo_horario():
    mover_disquete()
    ajeitar_disquete()
    mover_disquete()
    ajeitar_disquete()
    mover_disquete()
    ajeitar_disquete()
    mover_disquete()

#especifica da varredura no sentido anti-horário
def movimento_completo_anti():
    mover_disquete()
    turn_left()
    mover_disquete()
    turn_left()
    mover_disquete()
    turn_left()
    mover_disquete()

#especifica da varredura na horizontal
def sequencia_horizontal():
    mover_disquete()
    ajeitar_passo_disquete()
    mover_disquete()
    ajeitar_disquete()
    move()
    ajeitar_disquete()

def fim_horizontal():
    mover_disquete()
    ajeitar_passo_disquete()
    mover_disquete()
    turn_left()
    mover_disquete()
    turn_left()

#especifica da varredura na vertical
def inicio_vertical():
    mover_disquete()
    ajeitar_disquete()
    move()

def meio_vertical():
    ajeitar_disquete()
    mover_disquete()
    ajeitar_passo_disquete()

def fim_vertical():
    ajeitar_disquete()
    mover_disquete()
    ajeitar_disquete()
    mover_disquete()
    turn_left()
    turn_left()


#especifica da varredura na diagonal
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


#codigo final
def main(): 

#varredura no sentido horário
    turn_left()
    movimento_completo_horario()
    turn_left()
    turn_left()

#varredura no sentido anti-horário
    movimento_completo_anti()
    turn_left()

#varredura na horizontal
    sequencia_horizontal()
    sequencia_horizontal()
    sequencia_horizontal()
    fim_horizontal()

#varredura na vertical
    turn_left()
    inicio_vertical()
    meio_vertical()
    inicio_vertical()
    meio_vertical()
    inicio_vertical()
    meio_vertical()
    inicio_vertical()
    fim_vertical()

#varredura na diagonal
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