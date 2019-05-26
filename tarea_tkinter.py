# Se importan las librerias necesarias

from tkinter import *
import tkinter.messagebox
import time
import winsound
from threading import Thread

llamadas_pila = 0          # variable global para cantidad de llamadas recursivas de fibonacci en pila
llamadas_cola = 0          # variable global para cantidad de llamadas recursivas de fibonacci en cola
flag_nieve = True          # variable global para controlar hilos de animacion

# Se definen todas las funciones

"""
E: ninguna, se utiliza el valor ingresado en la entry1
S: el elemento de la sucesion de fibonacci correspondiente al numero ingresado
R: entero positivo
"""


def fibonacci_pila():
    try:
        num = int(entry1.get())
        if isinstance(num, int) and num >= 0:
            global llamadas_pila      # reconocer la variable global
            llamadas_pila = 0         # reinicio de la variable
            return fibonacci_pila_aux(num)
        else:
            tkinter.messagebox.showerror("Error", "Ingrese un elemento válido")
    except:
        tkinter.messagebox.showerror("Error", "Ingrese un elemento válido")


def fibonacci_pila_aux(num):
    global llamadas_pila
    llamadas_pila += 1     # cada vez que se es llamada la funcion auxiliar
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_pila_aux(num - 1) + fibonacci_pila_aux(num - 2)


"""
E: ninguna, se ejecuta al clickear el button1
S: un mensaje en una messagebox
R: fibonacci_pila debe retornar un integer
"""


def tocar_boton1():
    if isinstance(fibonacci_pila(), int):    # evita tener un mensaje sin sentido si al no ingresar un int
        start = time.time()
        fibonacci = fibonacci_pila()
        end = time.time()
        tiempo_final = end - start
        tkinter.messagebox.showinfo("Sucesión de Fibonnaci de Pila", "El número de Fibonacci es %s, se hicieron %s "
                                                                     "llamadas recursivas y tomó %s segundos."
                                    % (fibonacci, llamadas_pila, tiempo_final))


"""
E: ninguna, se utiliza el valor ingresado en la entry2
S: el elemento de la sucesion de fibonacci correspondiente al numero ingresado
R: entero positivo
"""


def fibonacci_cola():
    try:
        num = int(entry2.get())
        if isinstance(num, int) and num >= 0:
            global llamadas_cola
            llamadas_cola = 0
            return fibonacci_cola_aux(num, 0, 1)
        else:
            tkinter.messagebox.showerror("Error", "Ingrese un elemento válido")
    except:
        tkinter.messagebox.showerror("Error", "Ingrese un elemento válido")


def fibonacci_cola_aux(num, a, b):
    global llamadas_cola
    llamadas_cola += 1
    if num == 0:
        return a
    elif num == 1:
        return b
    else:
        return fibonacci_cola_aux(num - 1, b, a + b)


"""
E: ninguna, se ejecuta al clickear el button2
S: un mensaje en una messagebox
R: fibonacci_cola debe retornar un integer
"""


def tocar_boton2():
    if isinstance(fibonacci_cola(), int):
        start = time.time()
        fibonacci = fibonacci_cola()
        end = time.time()
        tiempo_final = end - start
        tkinter.messagebox.showinfo("Sucesión de Fibonnaci de Cola", "El número de Fibonacci es %s, se hicieron %s "
                                                                     "llamadas recursivas y tomó %s segundos."
                                    % (fibonacci, llamadas_cola, tiempo_final))


"""
E: ninguna, se utilizan los valores ingresado en las entry3 y entry4
S: un boolean indicando si el digito es menor o igual que todas las cifras del numero
R: enteros positivos y el digito menor o igual que 9
"""


def menorque():
    try:
        dig = int(entry3.get())
        num = int(entry4.get())
        if dig >= 0 and dig <= 9 and num > 0:
            if dig == 0:      # evita llamar a la funcion auxiliar innecesariamente
                return True
            else:
                return menorque_aux(dig, num)
        else:
            tkinter.messagebox.showerror("Error", "Ingrese elementos válidos.")
    except:
        tkinter.messagebox.showerror("Error", "Ingrese elementos válidos.")


def menorque_aux(dig, num):
    if num == 0:
        return True
    elif dig <= num % 10:
        return menorque_aux(dig, num // 10)
    else:
        return False


"""
E: ninguna, se ejecuta al clickear el button3
S: un mensaje en una messagebox
R: menorque debe retornar un boolean
"""


def tocar_boton3():
    if menorque():
        tkinter.messagebox.showinfo("Resultado", "Es cierto que el dígito es menor o igual a todas las cifras del "
                                                 "número.")
    elif menorque() == False:
        tkinter.messagebox.showinfo("Resultado", "No es cierto que el dígito es menor o igual a todas las cifras del "
                                                 "número.")


"""
E: ninguna, se ejecuta al clickear el button4
S: reproduccion de un audio
R: -
"""


def music():
    winsound.PlaySound("monster_in_me.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


"""
Se crea y configura la ventana de la animacion, al igual que su imagen de fondo
E: ninguna, se ejecuta al clickear el button5
S: creación de una nueva ventana
R: -
"""


def tocar_boton5():
    root.withdraw()
    ventana2 = Toplevel()
    ventana2.title("Animación")
    ventana2.minsize(900, 500)
    ventana2.resizable(width=NO,height=NO)

    canvas_animacion = Canvas(ventana2, width=900, height=500)
    canvas_animacion.place(x=0, y=0)

    fondo_animacion = PhotoImage(file="fondo_animacion.png")
    canvas.image = fondo_animacion     # PhotoImage garbage collection bug
    canvas_animacion.create_image(0, 0, image=fondo_animacion, anchor=NW)


    """
    Se crea la animacion en si
    E: ninguna, se ejecuta cuando el thread se inicia
    S: movimiento de la imagen nieve
    R: -
    """


    def animacion():
        x1 = 150
        y1 = 0
        nieve = PhotoImage(file="nieve.png")
        nieve_reducida = nieve.subsample(2, 2)
        nevar = canvas_animacion.create_image(x1, y1, image=nieve_reducida, anchor=NW)
        while flag_nieve:
            try:
                canvas_animacion.move(nevar, 0, 5)
                time.sleep(0.1)

            except:
                detener_nieve()


    """
    Se ejecuta el hilo
    E: ninguna, se ejecuta al clickear el button6
    S: ejecucion del hilo
    R: -
    """


    def iniciar_nieve():
        global flag_nieve
        flag_nieve = True
        hilo = Thread(target=animacion)
        hilo.daemon = True
        hilo.start()


    """
    Se detiene el hilo
    E: ninguna, se ejecuta  al clickear el button7
    S: se para de correr el hilo
    R: -
    """


    def detener_nieve():
        global flag_nieve
        flag_nieve = False


    """
    Se vuelve a la ventana principal, y se detienen hilos
    E: ninguna, se ejecuta  al clickear el button8
    S: se destruye la ventana2 y se abre la root, y se detienen hilos
    R: -
    """


    def regresar():
        global flag_nieve
        flag_nieve = False
        ventana2.destroy()
        root.deiconify()


    button6 = Button(ventana2, text="Iniciar", bg="navy", fg="snow", font=("Arial", "11"), command = iniciar_nieve)
    button6.place(x=569, y=465)

    button7 = Button(ventana2, text="Detener", bg="navy", fg="snow", font=("Arial", "11"), command = detener_nieve)
    button7.place(x=628, y=465)

    button8 = Button(ventana2, text="Regresar a ventana principal", bg="navy", fg="snow", font=("Arial", "11"),
                     command=regresar)
    button8.place(x=698, y=465)

    ventana2.mainloop()


# Construccion de la interfaz

# Creacion y configuracion de ventana principal

root = Tk()

root.title("Tarea Corta de Interfaz Gráfica")
root.minsize(1000, 600)
root.resizable(width=NO,height=NO)
root.configure(bg="powderblue")


# Se define el canvas y sus figuras

canvas = Canvas(root, width=1000, height=600, bg="powderblue")
canvas.place(x=0, y=0)

canvas.create_line(0, 213, 1000, 213, dash=(4,4))
canvas.create_rectangle(745, 38, 910, 90, fill="slateblue1")


# Se definen las imagenes

dani = PhotoImage(file="dani.png")
dani_reducida = dani.subsample(x=8, y=8)
canvas.create_image(260, 225, anchor=NW, image=dani_reducida)

mapa= PhotoImage(file="mapa.png")
canvas.create_image(50, 425, anchor=NW, image=mapa)

little_mix = PhotoImage(file="littlemix.png")
canvas.create_image(500, 335, anchor=NW, image=little_mix)


# Se definen las labels

label1 = Label(root, text="Sucesión de Fibonacci ", font="Arial 11 bold", bg="dodgerblue")
label2 = Label(root, text="Ingrese un número entero positivo para obtener el elemento en la sucesión de Fibonacci.",
               font="Arial 11", bg="powderblue")
label3 = Label(root, text="Número (utilizando recursividad de pila)", font="Arial 11", bg="powderblue")
label4 = Label(root, text="Número (utilizando recursividad de cola)", font="Arial 11", bg="powderblue")
label5 = Label(root, text="", bg="powderblue")
label6 = Label(root, text="Función menorque ", font="Arial 11 bold", bg="dodgerblue")
label7 = Label(root, text="Se verifica si cierto dígito es menor o igual a todas las cifras de un número específico",
               font="Arial 11", bg="powderblue")
label8 = Label(root, text="Ingrese el dígito y el número (entero postivo)", font="Arial 11", bg="powderblue")
label9 = Label(root, text="", bg="powderblue")
label10 = Label(root, text="Ficha Personal", font="Arial 11 bold", bg="dodgerblue")
label11 = Label(root, text="Nombre: Daniela Brenes Otárola", font="Arial 11", bg="powderblue")
label12 = Label(root, text="Carnet: 2019042386", font="Arial 11", bg="powderblue")
label13 = Label(root, text="Género: Femenino", font="Arial 11", bg="powderblue")
label14 = Label(root, text="Edad: 17 años", font="Arial 11", bg="powderblue")
label15 = Label(root, text="Dirección: San Rafael Abajo de Desamparados, Urbanización Treviso", font="Arial 11",
                bg="powderblue")
label16 = Label(root, text=" - Descripción: lo más destacable son los asaltos 24/7.", font="Arial 11", bg="powderblue")
label17 = Label(root, text=" - Mapa representativo:", font="Arial 11", bg="powderblue")
label18 = Label(root, text="Identificación musical:", font="Arial 11", bg="powderblue")
label19 = Label(root, text="-  Grupo favorito: Little Mix", font="Arial 11", bg="powderblue")
label20 = Label(root, text="              -   Género: Pop:", font="Arial 11", bg="powderblue")


# Se definen las entradas

entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)


# Se definen los botones

button1 = Button(root, text="Obtener resultado", bg="mediumaquamarine", font=("Arial", "11"), command=tocar_boton1)
button2 = Button(root, text="Obtener resultado", bg="mediumaquamarine", font=("Arial", "11"), command=tocar_boton2)
button3 = Button(root, text="Obtener resultado", bg="mediumaquamarine", font=("Arial", "11"), command=tocar_boton3)
button4 = Button(root, text="Reproducir canción", bg="mediumaquamarine", font=("Arial", "11"), command=music)
button5 = Button(root, text="Ir a la animación", bg="lightseagreen", font=("Arial", "13"), command=tocar_boton5)


# Se colocan las labels

label1.grid(row=0, column=0, sticky=W)
label2.grid(row=1, column=0, columnspan=3, sticky=W)
label3.grid(row=2, sticky=W)
label4.grid(row=3, sticky=W)
label5.grid(row=4, sticky=W)
label6.grid(row=5, sticky=W)
label7.grid(row=6, column=0, columnspan=3, sticky=W)
label8.grid(row=7, sticky=W)
label9.grid(row=8, sticky=W)
label10.grid(row=9, sticky=W)
label11.grid(row=10, sticky=W)
label12.grid(row=11, sticky=W)
label13.grid(row=12, sticky=W)
label14.grid(row=13, sticky=W)
label15.grid(row=14, columnspan=2, sticky=W)
label16.grid(row=15, columnspan=2, sticky=W)
label17.grid(row=16, sticky=W)
label18.grid(row=10, column=2)
label19.grid(row=11, columnspan=2, column=2)
label20.grid(row=12, column=2)


# Se colocan las entradas

entry1.grid(row=2, column=1, sticky=W)
entry2.grid(row=3, column=1, sticky=W)
entry3.grid(row=7, column=1, sticky=W)
entry4.grid(row=7, column=2, sticky=W)


# Se colocan los botones

button1.grid(row=2, column=2, sticky=W)
button2.grid(row=3, column=2, sticky=W)
button3.grid(row=7, column=3, sticky=W)
button4.grid(row=12, column=4, sticky=W)
button5.grid(row=2, column=4, sticky=E)


root.mainloop()
