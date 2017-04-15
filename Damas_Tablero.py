import Damas
from tkinter import*
from tkinter import ttk



root= Tk()
root.geometry("800x600")
root.resizable(0,0)
tableroGUI = Canvas(root,width=600,height=600)
tableroGUI.pack(side=LEFT,fill=Y)
diccionarioJugadorColor = {"j1":"yellow","j2":"black"}
movimientos=[]
turnoJugadorLabel=ttk.Label(root,text="")
turnoJugadorLabel.place(x="625", y="50")
labelFichaSeleccionada = None

labelMovimientoInvalido= ttk.Label(root,text="Movimiento Inválido",foreground="red",font="Helvetica")


def pintarTurno():
    turno="Turno de: "
    if Damas.turno=="j1":
        turno+=Damas.nombreJugador1
    else:
        turno+=Damas.nombreJugador2
    turnoJugadorLabel.config(text=turno)
    




def clickFicha(event):
    
    fila = (8*event.y)//600
    columna =(8*event.x)//600
    global movimientos
    global labelFichaSeleccionada
    movimientos.append([fila,columna])
    if len(movimientos)==1:
        labelMovimientoInvalido.place_forget()
        x = columna*75+32
        y = fila*75+32
        x1 = x+10
        y1= y+10
        labelFichaSeleccionada = tableroGUI.create_oval(x,y,x1,y1,fill="blue")
    if len(movimientos)==2:
        tableroGUI.delete(labelFichaSeleccionada)
        valor = Damas.validarMovimiento(movimientos[0],movimientos[1])
        movimientos = []
        if valor==True:
            pintarTablero()
            pintarTableroFichas(Damas.tablero)
        else:
            labelMovimientoInvalido.place(x="625",y="250")
        
        
 
def pintarTablero():
    tableroGUI.delete("all")
    listaColores =  ["white","red"]
    x=0
    y=0
    x1=75
    y1=75
    for fila in range(0,8):
        for casilla in range(0,8):
            color = listaColores[0]
            if casilla%2!=0:
                color=listaColores[1]
            casilla= tableroGUI.create_rectangle(x,y,x1,y1,fill=color)
            tableroGUI.tag_bind(casilla,"<ButtonPress-1>",clickFicha)
            x+=75
            x1+=75
        x=0
        x1=75
        y+=75
        y1+=75
        listaColores.reverse()
    pintarTurno()



def pintarFicha(pX,pY,pX1,pY1,jugador,esDama):
    ficha = tableroGUI.create_oval(pX,pY,pX1,pY1,fill=diccionarioJugadorColor.get(jugador))
    return ficha
    
    
def pintarTableroFichas(pTablero):
    x=0
    y=0
    x1=75
    y1=75
    for fila in pTablero:
        for casilla in fila:
            if casilla!=0:
                ficha = pintarFicha(x,y,x1,y1,casilla[0],casilla[1])
                tableroGUI.tag_bind(ficha,"<ButtonPress-1>",clickFicha)

            x+=75
            x1+=75
        x=0
        x1=75
        y+=75
        y1+=75





pintarTablero()
pintarTableroFichas(Damas.tablero)



    
            
            
            




