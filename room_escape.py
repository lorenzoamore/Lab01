def stampa_griglia(n, pos, uscita):
    """Stampa la griglia con G = giocatore, U = uscita, . = spazio vuoto"""
    """definisco la griglia"""
    tabella = []
    for d in range(n):
        tabella.append(["."]*n)
    "aggiungo l'uscita e il giocatore"
    tabella[pos[0]][pos[1]] = "G"
    tabella[uscita[0]][uscita[1]] = "U"
    "stampo la tabella"
    for s in range(n):
        riga = ""
        for a in range(n):
            riga = riga + tabella[s][a] + " "
        print(riga)
    # TODO

def muovi(pos, mossa):
    """Aggiorna la posizione in base alla mossa"""
    if mossa == "e":
        pos[1] += 1
    if mossa == "o":
        pos[1] += -1
    if mossa == "n":
        pos[0] += -1
    if mossa == "s":
        pos[0] -= -1
    return pos
    # TODO


def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco
    Ritorna:
    * True se il giocatore raggiunge l'uscita
    * False se il giocatore va oltre i limiti della griglia.

    NB: Le funzioni stampa_griglia() e muovi() vanno chiamate dentro questa funzione
    """
    # Inizializzazioni
    n = livello + 2
    uscita = [n - 1, n - 1]  # posizione uscita

    from random import randint
    pos= [randint(0,n-1),randint(0,n-1)]
    while pos == uscita:
        pos = [randint(0, n - 1), randint(0, n - 1)]

    stampa_griglia(n,pos,uscita)
    a = True
    while a:
        mossa = input("Mossa (n/s/e/o): ")
        pos = muovi(pos,mossa)
        if pos == uscita:
            print("Hai raggiunto l'uscita, hai vinto")
            return True
            a = False
        elif (pos[0] or pos[1])>n-1 or (pos[0] or pos[1])<0:
            print("Sei andato fuori dalla griglia, hai perso ")
            return False
            a = False
        else:
            stampa_griglia(n,pos,uscita)
            a = True

    # TODO

def main():
    print("=== Benvenuto in Room Escape ===")
    livello = 0
    max_livello = 5


    while livello <= max_livello:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            print("Hai completato tutti i livelli")
            break


if __name__ == "__main__":
    main()
