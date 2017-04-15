import math
turno= "j1"
nombreJugador1 = "Jugador 1"
nombreJugador2 = "Jugador 2"


jugador1=[nombreJugador1,12,0]
jugador2=[nombreJugador2,12,0]

tablero= [[1,0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0,1],
          [1,0,1,0,1,0,1,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,1,0,1,0,1,0,1],
          [1,0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0,1]]

ficha = 0

for fila in range(0,8):
    for casilla in range(0,8):
        if tablero[fila][casilla]==1:
            jugador = "j1"
            if ficha >=12:
                jugador = "j2"
            tablero[fila][casilla] = [jugador,False]
            ficha+=1

def moverFicha(coordenadasOr,coordenadasNuevas):
    global turno
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    ficha=tablero[filaOriginal][columnaOriginal]
    tablero[filaOriginal][columnaOriginal]=0
    tablero[filaNueva][columnaNueva]=ficha
    if turno=="j1":
        turno="j2"
    else:
        turno="j1"
    return True
def eliminarFichas(listaFichas):
    for ficha in listaFichas:
        fila=ficha[0]
        columna=ficha[1]
        tablero[fila][columna]=0
        
def comerDDA(coordenadasOr,coordenadasNuevas):
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    fichasEliminadas=[]
    sePuedeMover = False
    columna = columnaNueva
    for fila in range(filaNueva,filaOriginal):
        if tablero[fila][columna]!=0:
            ficha= tablero[fila][columna]
            if ficha[0]!=turno:
                fichasEliminadas.append([fila,columna])
                sePuedeMover = True
            elif ficha[0]==turno:
                sePuedeMover=False
                break
        columna-=1
    if sePuedeMover==True:
        eliminarFichas(fichasEliminadas)
        return True
    else:
        return False
def comerDIA(coordenadasOr,coordenadasNuevas):
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    fichasEliminadas=[]
    sePuedeMover = False
    columna = columnaNueva
    for fila in range(filaNueva,filaOriginal):
        if tablero[fila][columna]!=0:
            ficha= tablero[fila][columna]
            if ficha[0]!=turno:
                fichasEliminadas.append([fila,columna])
                sePuedeMover = True
            elif ficha[0]==turno:
                sePuedeMover=False
                break
        columna+=1
    if sePuedeMover==True:
        eliminarFichas(fichasEliminadas)
        return True
    else:
        return False
def comerDDAb(coordenadasOr,coordenadasNuevas):
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    fichasEliminadas=[]
    sePuedeMover = False
    columna = columnaOriginal+1
    print (filaOriginal,columnaOriginal,filaNueva,columnaOriginal)
    for fila in range(filaOriginal+1,filaNueva):
        print (fila,columna)
        if tablero[fila][columna]!=0:
            ficha= tablero[fila][columna]
            if ficha[0]!=turno:
                fichasEliminadas.append([fila,columna])
                sePuedeMover = True
            elif ficha[0]==turno:
                sePuedeMover=False
                break
        columna+=1
    if sePuedeMover==True:
        eliminarFichas(fichasEliminadas)
        return True
    else:
        return False
            
def comerDIAb(coordenadasOr,coordenadasNuevas):
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    fichasEliminadas=[]
    sePuedeMover = False
    columna = columnaOriginal-1
    for fila in range(filaOriginal+1,filaNueva):
        if tablero[fila][columna]!=0:
            ficha= tablero[fila][columna]
            if ficha[0]!=turno:
                fichasEliminadas.append([fila,columna])
                sePuedeMover = True
            elif ficha[0]==turno:
                sePuedeMover=False
                break
        columna-=1
    if sePuedeMover==True:
        eliminarFichas(fichasEliminadas)
        return True
    else:
        return False

def validarComida(coordenadasOr,coordenadasNuevas):
    global turno
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    ficha=tablero[filaNueva][columnaNueva]
    if ficha!=0:
        return False
    else:
        valor = False
        if filaOriginal>filaNueva and columnaOriginal<columnaNueva:
            valor = comerDDA(coordenadasOr,coordenadasNuevas)
        elif filaOriginal>filaNueva and columnaOriginal>columnaNueva:
            valor = comerDIA(coordenadasOr,coordenadasNuevas)
        elif filaOriginal<filaNueva and columnaOriginal<columnaNueva:
            valor = comerDDAb(coordenadasOr,coordenadasNuevas)
        else:
            valor = comerDIAb(coordenadasOr,coordenadasNuevas)
        if valor==True:
            moverFicha(coordenadasOr,coordenadasNuevas)
        if valor ==True:
            if turno == "j1":
                turno="j2"
            else:
                turno="j1"
        return valor
        
        
    

    

def validarMovimientoJ1Normal(coordenadasOr,coordenadasNuevas):
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    ficha=tablero[filaOriginal][columnaOriginal]
    if filaOriginal<filaNueva:
        restaFila=abs(filaOriginal-filaNueva)
        restaColumna=abs(columnaOriginal-columnaNueva)
        if restaFila==restaColumna:
            if restaFila==2:
                return validarComida(coordenadasOr,coordenadasNuevas)
            elif restaFila==1:
                if tablero[filaNueva][columnaNueva]!=0:
                    return False
                return moverFicha(coordenadasOr,coordenadasNuevas)
            return False

    else:
        return False

    

def validarMovimientoJ1(coordenadasOr,coordenadasNuevas):
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    ficha=tablero[filaOriginal][columnaOriginal]
    if ficha==0:
        return False
    elif ficha[0]!= "j1":
        return False
    else:
        if ficha[1]==True:
            return validarMovimientoJ1Dama(coordenadasOr,coordenadasNuevas)
        else:
            return validarMovimientoJ1Normal(coordenadasOr,coordenadasNuevas)
    


def validarMovimientoJ2Normal(coordenadasOr,coordenadasNuevas):
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    ficha=tablero[filaOriginal][columnaOriginal]
    if filaOriginal>filaNueva:
        restaFila=abs(filaOriginal-filaNueva)
        restaColumna=abs(columnaOriginal-columnaNueva)
        if restaFila==restaColumna:
            if restaFila==2:
                return validarComida(coordenadasOr,coordenadasNuevas)
            elif restaFila==1:
                if tablero[filaNueva][columnaNueva]!=0:
                    return False
                return moverFicha(coordenadasOr,coordenadasNuevas)
            return False
    else:
        return False




def validarMovimientoJ2(coordenadasOr,coordenadasNuevas):
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    ficha=tablero[filaOriginal][columnaOriginal]
    if ficha==0:
        return False
    elif ficha[0]!="j2":
        return False
    else:
        if ficha[1]==True:
            return validarMovimientoJ2Dama(coordenadasOr,coordenadasNuevas)
        else:
            return validarMovimientoJ2Normal(coordenadasOr,coordenadasNuevas)

            
        
def validarMovimiento(coordenadasOr,coordenadasNuevas):
    if turno=="j1":
        resultado=validarMovimientoJ1(coordenadasOr,coordenadasNuevas)
    elif turno=="j2":
        resultado= validarMovimientoJ2(coordenadasOr,coordenadasNuevas)
    return resultado
