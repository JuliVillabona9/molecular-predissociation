from tkinter import *
from tkinter import ttk
import math
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
from tkinter import messagebox

xpotC,ypotC = np.loadtxt("Data\\e-Cstate.dat", unpack=True)
xpotB,ypotB = np.loadtxt("Data\\e-Bstate.dat", unpack=True)
wvfC=np.loadtxt("Data\\wvf-e-Cstate.dat-0.dat", unpack=True)

class app:

  #Básico
  def __init__(self):
    try:
      self.inform.destroy()
    except:
      print("")
    try:
      self.infnitro.destroy()
    except:
      print("")
    try:
      self.ayuda.destroy()
    except:
      print("")
    try:
      self.Vquiz.destroy()
    except:
      print("")
      
    self.root = Tk()
    self.root.iconbitmap("Data\\ENE.ico")
    self.root.title("Predisociación")
    self.root.geometry("820x600+300+10")
    self.root.resizable(0,0)

    # Variables to be specified
    self.T = DoubleVar(value=1.0)
    self.J = IntVar(value=0)
    self.v = IntVar(value=0)
    
    self.Isotope = StringVar(value='Title')
    self.xmol = BooleanVar(value='False') #Fracción molar
    self.type = StringVar(value='null')  #Lleva la información sobre que opción se quiere graficar
    self.image=PhotoImage(file="Data\\8.png") #Imagen de inicio
    self.imbot=PhotoImage(file="Data/botoncito.gif")


 
    # Widgets (Buttons and commands)

    #Etiquetas fijas 
    self.title=Label(self.root,text="PREDISOCIACIÓN MOLECULAR",font=("Yu gothic",30,"bold"), fg="#33B8FF")
    self.labeimg=Label(self.root,image=self.image) #Un label que contiene una imágen
    self.labelISO = Label(self.root,text="Selecciona un isótopo para iniciar",font=("Yu gothic",13,"bold"))
    self.conditions = Label(self.root,text="Condiciones Iniciales",font=("Yu gothic",13, "bold"))
    self.select = Label(self.root,text="¿Qué gráfica te gustaría observar?",font=("Yu gothic",13, "bold"))
    self.labelT = Label(self.root,text="Temperatura (K), T:", font=("Yu gothic",10))
    self.labelJ = Label(self.root,text="Número cuántico rotacional, J:", font=("Yu gothic",10))
    self.labelv = Label(self.root,text="Número cuántico vibracional, v:", font=("Yu gothic",10))
    #Etiquetas de entrada
    self.temp = ttk.Entry(self.root, textvariable=self.T, width=20)

    #Botones de selección para graficar

    #Selección del isótopo
    self.Iso1414 = Radiobutton(self.root, text="¹⁴N¹⁴N⁺",font=("Yu gothic",16, "bold"),variable=self.Isotope,value='¹⁴N¹⁴N⁺', cursor= "hand2")
    self.Iso1415 = Radiobutton(self.root, text="¹⁴N¹⁵N⁺",font=("Yu gothic",16, "bold"), variable=self.Isotope,value='¹⁴N¹⁵N⁺', cursor= "hand2")
    self.Iso1515 = Radiobutton(self.root, text="¹⁵N¹⁵N⁺",font=("Yu gothic",16, "bold"), variable=self.Isotope,value='¹⁵N¹⁵N⁺', cursor= "hand2")
    #línea divisoria
    self.labelP1 = Label(self.root,text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _", fg="#33B8FF")
    self.labelP2 = Label(self.root,text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _", fg="#33B8FF")
    self.labelP3 = Label(self.root,text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _", fg="#33B8FF")

    #Selección de la gráfica
    self.kpredT = Radiobutton(self.root, text="Constantes de predisociación para una T dada", font=("Yu gothic",10),
                  variable=self.type,value='a', cursor= "hand2")
    self.kpredJ = Radiobutton(self.root, text="Constantes de predisociación para un J dado", font=("Yu gothic",10),
                  variable=self.type,value='b', cursor= "hand2")
    self.kpredv = Radiobutton(self.root, text="Constantes de predisociación para un v dado", font=("Yu gothic",10),
                  variable=self.type,value='c', cursor= "hand2")
    self.wvf = Radiobutton(self.root, text="Función de onda", font=("Yu gothic",10),
                  variable=self.type,value='d', cursor= "hand2")
    self.molar = Radiobutton(self.root, text="Fracción Molar", font=("Yu gothic",10),
                  variable=self.type,value='e', cursor= "hand2")              
    #Botones de selección para información de v y J              
    self.valueJ = Spinbox(self.root,from_=0,to=30,wrap=False,textvariable=self.J,state='readonly')
    self.valuev = Spinbox(self.root,from_=0, to=9,wrap=False,textvariable=self.v,state='readonly')
    #Botón para obtener la gráfica
    self.plotT = Button(self.root,text="Graficar",command=self.pltT, font=("Yu gothic",10, "bold"), cursor= "hand2")
    self.plotv = Button(self.root,text="Graficar",command=self.pltv, font=("Yu gothic",10, "bold"), cursor= "hand2")
    self.plotJ = Button(self.root,text="Graficar",command=self.pltJ, font=("Yu gothic",10, "bold"), cursor= "hand2")

    def back():
        self.root.destroy()
    
    #Salir de la app
    self.exit = Button(self.root,text="Salir",command=back, font=("Yu gothic",10, "bold"), cursor = "hand2")
    
    #Empaquetamientos (Posicionamiento)
    #Etiquetas texto fijo
    self.title.place( x = 55, y = 10)
    self.labeimg.place( x = 80, y = 70)
    self.labelISO.place( x = 470 , y = 80) 
    self.labelP1.place( x =10 , y = 280)
    self.labelP2.place( x =10 , y = 395)
    self.labelP3.place( x =10 , y = 470)
    self.conditions.place( x = 30 , y = 310)
    self.select.place( x = 370, y = 310 )
    self.labelT.place( x = 40 , y = 340)
    self.labelv.place( x= 40 , y = 420)
    self.labelJ.place( x = 40, y = 500)
    #Etiquetas texto de entrada
    self.temp.place( x = 50, y = 370)
    #Botones RadioBotton
    self.Iso1414.place( x = 520 , y = 140)
    self.Iso1415.place( x = 520 , y = 180)
    self.Iso1515.place( x = 520 , y = 220)
    self.kpredT.place( x = 370 , y = 340) 
    self.molar.place( x = 370 , y = 370)
    self.kpredv.place( x = 370, y = 420)
    self.wvf.place( x = 370, y = 450)
    self.kpredJ.place( x = 370, y = 510 )
    #Botones SpinBox
    self.valuev.place( x = 50 , y = 450) 
    self.valueJ.place( x = 50, y = 530)
    #Botones para obtener gráficas
    self.plotT.place( x = 720, y = 350)
    self.plotv.place( x = 720, y = 430)
    self.plotJ.place( x = 720, y = 515)
    #Botón de salida de la app
    self.exit.place( x = 385, y = 560)
##############Adicionales
    self.botinfor = Button(self.root,text="Más\nInformación",command=self.info, font=("Yu gothic",10, "bold"), cursor= "hand2")
    self.botinfor.place(x=690,y=10)
    self.botN = Button(self.root,image = self.imbot,command=self.NITROGENO, font=("Yu gothic",10, "bold"), cursor= "hand2")
    self.botN.place(x=410,y=80)
    self.bothelp = Button(self.root,text="Ayuda",command=self.help, font=("Yu gothic",10, "bold"), cursor= "hand2")
    self.bothelp.place(x=540,y=560)
    self.botquiz = Button(self.root,text="Quiz",command=self.quiz, font=("Yu gothic",10, "bold"),fg="#33B8FF", cursor= "hand2")
    self.botquiz.place(x=240,y=560)
############  
    self.root.mainloop()
  ########  FUNCION PANTALLA ###############
  def quiz(self):
    
    self.root.destroy()
    self.Vquiz= Tk()
    self.Vquiz.geometry("200x280+300+10")
    self.Vquiz.iconbitmap("Data\\ENE.ico")
    self.Vquiz.resizable(0,0)
    self.Vquiz.title("Predisociación")
    
    self.Nombre = StringVar()
    self.Apellido = StringVar()
  
    def back():
      self.Vquiz.destroy()
      self.__init__()
    def Ingresar():
      global Nombre,Apellido,Nivel1,Calificacion1,Nivel2,Calificacion2,Nivel3,Calificacion3
      Nombre = self.Nombre.get()
      Apellido = self.Apellido.get()
      
      Nombre = Nombre.upper()##convertir en mayusculas
      Apellido = Apellido.upper()

    #  print(Nombre,Apellido)
      if Nombre == "" and Apellido == "":
        self.labelERROR = Label(self.Vquiz,text="INGRESO INVÁLIDO", font=("Yu gothic",12, "bold"), fg="red")
        self.labelERROR.place( x = 20, y = 249)
      else:
        try:
          self.Vquiz.destroy()
        except:
          print("")
        
        
        
        H = open("Data\Historico.dat","r")
        Data = H.readlines()
        H.close()
    
        Nivel1 = '0'
        Calificacion1 = '0'
        Nivel2 = '0'
        Calificacion2 = '0'
        Nivel3 = '0'
        Calificacion3 = '0'
        Existe = '0'
        posfila = len(Data)
        
        for i in range (1,len(Data)):
          
          fila = Data[i].strip()
          Datos = fila.split(";") ## SEPARAR COMPONENTES DEL VECTOR 
          if Datos[0] == Nombre and Datos[1] == Apellido:
            
            Existe = '1'
            posfila = i
            
            Nivel1 = Datos[2]
            Calificacion1 = Datos[3]
            Nivel2 = Datos[4]
            Calificacion2 = Datos[5]
            Nivel3 = Datos[6]
            Calificacion3 = Datos[7]
            
        if Existe == '0' :
          informacion=Nombre+';'+Apellido+';'+Nivel1+';'+Calificacion1+';'+Nivel2+';'+Calificacion2+';'+Nivel3+';'+Calificacion3+'\n'
          Data.append(informacion)
          


        self.Vquiz1 = Tk()
        self.Vquiz1.iconbitmap("Data\\ENE.ico")
        self.Vquiz1.geometry("650x620+200+10")
        self.Vquiz1.title("Predisociación")

        self.P1 = StringVar()
        self.P2 = StringVar()
        self.P3 = StringVar()
        
        def volver():
          self.Vquiz1.destroy()
          self.__init__()
        def evaluar():
          global Nombre,Apellido,Nivel1,Calificacion1,Nivel2,Calificacion2,Nivel3,Calificacion3

          
          
          R1 =  str(self.P1.get())
          R2 =  str(self.P2.get())
          R3 =  str(self.P3.get())

          nota = 0
          if Nivel1 == '1' and Nivel2 == '1' and Nivel3 == '0':
            if R1 == "D":
              nota = nota + 33
            if R2 == "A":
              nota = nota + 33
            if R3 == "B":
              nota = nota + 34
            if int(Calificacion3)<int(nota):
              Calificacion3 = str(nota)
            if nota >= 66:
              Nivel3 = '1'
            if nota < 66:
              messagebox.showinfo("INTENTA DE NUEVO","Tu calificación es muy\nbaja para continuar \n ¡Intenta de nuevo!")
              
          if Nivel1 == '1' and Nivel2 == '0':
            if R1 == "B":
              nota = nota + 33
            if R2 == "C":
              nota = nota + 33
            if R3 == "A":
              nota = nota + 34
            if int(Calificacion2)<int(nota):
              Calificacion2 = str(nota)
            if nota >= 66:
              Nivel2 = '1'
              messagebox.showinfo("FELICITACIONES","¡PASASTE DE NIVEL!\n Puedes continuar con \n un nivel de mayor \n dificultad")
            if nota < 66:
              messagebox.showinfo("INTENTA DE NUEVO","Tu calificación es muy\nbaja para continuar \n ¡Intenta de nuevo!")
          
          if Nivel1 == '0':
            if R1 == "A":
              nota = nota + 33
            if R2 == "B":
              nota = nota + 33
            if R3 == "C":
              nota = nota + 34
            if int(Calificacion1)<int(nota):
              Calificacion1 = str(nota)
            if nota >= 66:
              Nivel1 = '1'
              messagebox.showinfo("FELICITACIONES","¡PASASTE DE NIVEL!\n Puedes continuar con \n un nivel de mayor \n dificultad")
            if nota < 66:
              messagebox.showinfo("INTENTA DE NUEVO","Tu calificación es muy\nbaja para continuar \n ¡Intenta de nuevo!")
              
          
              
          self.Vquiz1.destroy()
            
          #print(nota)
          #print(Data)
          informacion=Nombre+';'+Apellido+';'+Nivel1+';'+Calificacion1+';'+Nivel2+';'+Calificacion2+';'+Nivel3+';'+Calificacion3+'\n'
          Data[posfila] = informacion
          #print(Data)
          
          H = open("Data\\Historico.dat","w")
          for f in range(len(Data)):
            H.write(Data[f])
          H.flush()
          H.close()

          Ingresar()
        
        if Nivel1 == '0':

          self.labelUSUARIO = Label(self.Vquiz1,text=Nombre+" "+Apellido+" Nivel actual: 1 "+" Mejor nota: "+Calificacion1, font=("Yu gothic",13, "bold"))
          
          self.labelNIVEL = Label(self.Vquiz1,text="NIVEL 1", font=("Yu gothic",13, "bold"), fg="#33B8FF")
          self.labelP1 = Label(self.Vquiz1,text="La predisociación se presenta como mecanismo de relajación del sistema.\n¿Cuál proceso compite con la predisociación? ", justify=LEFT, font=("Yu gothic",12, "bold"))

          self.P1A = Radiobutton(self.Vquiz1, text="Decaimiento radiativo o fotoemisión",font=("Yu gothic",10, "bold"), variable=self.P1,value='A', cursor= "hand2")
          self.P1B = Radiobutton(self.Vquiz1, text="Disociación molecular",font=("Yu gothic",10, "bold"), variable=self.P1,value='B', cursor= "hand2")
          self.P1C = Radiobutton(self.Vquiz1, text="Entrecruzamiento entre estados electrónicos",font=("Yu gothic",10, "bold"), variable=self.P1,value='C', cursor= "hand2")
          self.P1D = Radiobutton(self.Vquiz1, text="Excitación molecular",font=("Yu gothic",10, "bold"), variable=self.P1,value='D', cursor= "hand2")

          self.labelP2 = Label(self.Vquiz1,text="En el desarrollo mecanico-cuántico, las energías y funciones de onda\nfueron obtenidas por medio de:", justify=LEFT, font=("Yu gothic",12, "bold"))

          self.P2A = Radiobutton(self.Vquiz1, text="La regla de Oro de Fermi",font=("Yu gothic",10, "bold"), variable=self.P2,value='A', cursor= "hand2")
          self.P2B = Radiobutton(self.Vquiz1, text="La resolución de la ecuación de Shrödinger",font=("Yu gothic",10, "bold"), variable=self.P2,value='B', cursor= "hand2")
          self.P2C = Radiobutton(self.Vquiz1, text="La distribución estadística de Maxwell-Boltzmann",font=("Yu gothic",10, "bold"), variable=self.P2,value='C', cursor= "hand2")
          self.P2D = Radiobutton(self.Vquiz1, text="El estudio de los mecanismos de relajación del sistema",font=("Yu gothic",10, "bold"), variable=self.P2,value='D', cursor= "hand2")

          self.labelP3 = Label(self.Vquiz1,text="Según reportes experimentales, la excitación rotacional puede afectar\nlas tasas de predisociación.¿Cuál de los siguientes isotopómeros\npresenta menor efecto rotacional?",justify=LEFT, font=("Yu gothic",12, "bold"))

          self.P3A = Radiobutton(self.Vquiz1, text="Todos presentan el mismo efecto rotacional",font=("Yu gothic",10, "bold"), variable=self.P3,value='A', cursor= "hand2")
          self.P3B = Radiobutton(self.Vquiz1, text="¹⁴N¹⁵N⁺",font=("Yu gothic",10,"bold"), variable=self.P3,value='B', cursor= "hand2")
          self.P3C = Radiobutton(self.Vquiz1, text="¹⁴N¹⁴N⁺",font=("Yu gothic",10, "bold"), variable=self.P3,value='C', cursor= "hand2")
          self.P3D = Radiobutton(self.Vquiz1, text="¹⁵N¹⁵N⁺",font=("Yu gothic",10, "bold"), variable=self.P3,value='D', cursor= "hand2")


        if Nivel1 == '1' and Nivel2 == '0':
          
          self.labelUSUARIO = Label(self.Vquiz1,text=Nombre+" "+Apellido+" Nivel: 2 "+" Mejor nota: "+Calificacion2, font=("Yu gothic",13, "bold"), fg="#33B8FF")

          self.labelNIVEL = Label(self.Vquiz1,text="NIVEL 2", font=("Yu gothic",13, "bold"))
          self.labelP1 = Label(self.Vquiz1,text="A las mismas condiciones termodinámicas, ¿cuál ion molecular de\nnitrógeno tiene más probabilidad de presentar predisociación?",justify=LEFT, font=("Yu gothic",12, "bold"))

          self.P1A = Radiobutton(self.Vquiz1, text="Todos los isotopómeros tienen la misma probabilidad",font=("Yu gothic",10, "bold"),variable=self.P1,value='A', cursor= "hand2")
          self.P1B = Radiobutton(self.Vquiz1, text="¹⁴N¹⁴N⁺",font=("Yu gothic",10, "bold"), variable=self.P1,value='B', cursor= "hand2")
          self.P1C = Radiobutton(self.Vquiz1, text="¹⁴N¹⁵N⁺",font=("Yu gothic",10, "bold"), variable=self.P1,value='C', cursor= "hand2")
          self.P1D = Radiobutton(self.Vquiz1, text="¹⁵N¹⁵N⁺",font=("Yu gothic",10, "bold"), variable=self.P1,value='D', cursor= "hand2")

          self.labelP2 = Label(self.Vquiz1,text="¿Es la predisociación molecular del N-N⁺ un posible mecanismo de\nrelajación para cualquier estado rotovibracional?", justify=LEFT,font=("Yu gothic",12, "bold"))

          self.P2A = Radiobutton(self.Vquiz1, text="Sí, no existe una restricción para ninguno de los niveles rotovibracionales",font=("Yu gothic",10, "bold"), variable=self.P2,value='A', cursor= "hand2")
          self.P2B = Radiobutton(self.Vquiz1, text="No, existen restricciones energéticas para algunos niveles rotacionales",font=("Yu gothic",10, "bold"), variable=self.P2,value='B', cursor= "hand2")
          self.P2C = Radiobutton(self.Vquiz1, text="No, solo es posible a partir del tercer estado vibracional",font=("Yu gothic",10, "bold"), variable=self.P2,value='C', cursor= "hand2")
          self.P2D = Radiobutton(self.Vquiz1, text="No, existen diferentes restricciones rotovibracionales",font=("Yu gothic",10, "bold"), variable=self.P2,value='D', cursor= "hand2")

          self.labelP3 = Label(self.Vquiz1,text="No olvides tener en cuenta que estas son preguntas de única respuesta.\n\nEn la predisociación molecular existe un evidente efecto:",justify=LEFT, font=("Yu gothic",12, "bold"))

          self.P3A = Radiobutton(self.Vquiz1, text="Isotópico",font=("Yu gothic",10, "bold"), variable=self.P3,value='A', cursor= "hand2")
          self.P3B = Radiobutton(self.Vquiz1, text="Térmico",font=("Yu gothic",10, "bold"), variable=self.P3,value='B', cursor= "hand2")
          self.P3C = Radiobutton(self.Vquiz1, text="Tunel",font=("Yu gothic",10, "bold"), variable=self.P3,value='C', cursor= "hand2")
          self.P3D = Radiobutton(self.Vquiz1, text="Molecular",font=("Yu gothic",10, "bold"), variable=self.P3,value='D', cursor= "hand2")

        if Nivel1 == '1' and Nivel2 == '1' and Nivel3 == '0':

          self.labelUSUARIO = Label(self.Vquiz1,text=Nombre+" "+Apellido+" Nivel: 3 "+" Mejor nota: "+Calificacion3, font=("Yu gothic",13, "bold"), fg="#33B8FF")
          
          self.labelNIVEL = Label(self.Vquiz1,text="NIVEL 3", font=("Yu gothic",13, "bold"))
          self.labelP1 = Label(self.Vquiz1,text="¿Por qué no ocurre predisociación molecular antes del tercer estado\nvibracional del ion N-N⁺?", justify=LEFT,font=("Yu gothic",12, "bold"))

          self.P1A = Radiobutton(self.Vquiz1, text="En los niveles de menor energía ocurre disociación sin pasar por la predisociación",font=("Yu gothic",10, "bold"),variable=self.P1,value='A', cursor= "hand2")
          self.P1B = Radiobutton(self.Vquiz1, text="La predisociación conlleva restricciones rotacionales que influyen",font=("Yu gothic",10, "bold"), variable=self.P1,value='B', cursor= "hand2")
          self.P1C = Radiobutton(self.Vquiz1, text="Son necesarias menores energías de excitación para que ocurra la predisociación",font=("Yu gothic",10, "bold"), variable=self.P1,value='C', cursor= "hand2")
          self.P1D = Radiobutton(self.Vquiz1, text="Las energías de los anteriores estados no superan la energía de disociación",font=("Yu gothic",10, "bold"), variable=self.P1,value='D', cursor= "hand2")
          
          self.labelP2 = Label(self.Vquiz1,text="A mayores energías vibracionales la frecuencia de predisociación exhibe:", justify=LEFT,font=("Yu gothic",12, "bold"))

          self.P2A = Radiobutton(self.Vquiz1, text="Tendencia creciente debido al aumento de energía cinética",font=("Yu gothic",10, "bold"), variable=self.P2,value='A', cursor= "hand2")
          self.P2B = Radiobutton(self.Vquiz1, text="Tendencia creciente ya que el sistema tendrá menor energía total",font=("Yu gothic",10, "bold"), variable=self.P2,value='B', cursor= "hand2")
          self.P2C = Radiobutton(self.Vquiz1, text="Tendencia decreciente ya que el sistema tendrá mayor energía total",font=("Yu gothic",10, "bold"), variable=self.P2,value='C', cursor= "hand2")
          self.P2D = Radiobutton(self.Vquiz1, text="Un compartamiento periódico",font=("Yu gothic",10, "bold"), variable=self.P2,value='D', cursor= "hand2")

          self.labelP3 = Label(self.Vquiz1,text="El efecto isotópico presentado en la predisociación molecular puede\nser justificado principalmente por:",justify=LEFT, font=("Yu gothic",12, "bold"))

          self.P3A = Radiobutton(self.Vquiz1, text="El efeto de excitación rotacional sobre las masas de cada isotopómero",font=("Yu gothic",10, "bold"), variable=self.P3,value='A', cursor= "hand2")
          self.P3B = Radiobutton(self.Vquiz1, text="El efecto de excitación vibracional sobre las masas de cada isotopómero",font=("Yu gothic",10, "bold"), variable=self.P3,value='B', cursor= "hand2")
          self.P3C = Radiobutton(self.Vquiz1, text="Las diferencias energéticas entre el estado inicial y final de la transición",font=("Yu gothic",10, "bold"), variable=self.P3,value='C', cursor= "hand2")
          self.P3D = Radiobutton(self.Vquiz1, text="La temperatura",font=("Yu gothic",10, "bold"), variable=self.P3,value='D', cursor= "hand2")

        if Nivel1 == '1' and Nivel2 == '1' and Nivel3 == '1':
          
          self.labelCONGRATS = Label(self.Vquiz1,text="¡FELICITACIONES!", font=("Yu gothic",25, "bold"), fg="#33B8FF")
          self.labelFINAL = Label(self.Vquiz1,text="Culminaste los tres niveles\n sobre predisociación molecular", font=("Yu gothic",25, "bold"), fg="#33B8FF")    
          self.botFINALIZAR = Button(self.Vquiz1,text="FINALIZAR",command=volver, font=("Yu gothic",13, "bold"), cursor= "hand2")

          self.botFINALIZAR.place( x = 275 , y = 550)
          self.labelCONGRATS.place( x = 150 , y = 180)
          self.labelFINAL.place( x = 50, y = 240 )     

        if Nivel1 != '1' or Nivel2 != '1' or Nivel3 != '1':
          self.botevaluar = Button(self.Vquiz1,text="EVALUAR",command=evaluar, font=("Yu gothic",8, "bold"), cursor= "hand2")
          self.botvolver = Button(self.Vquiz1,text="VOLVER",command=volver, font=("Yu gothic",8, "bold"), cursor= "hand2")
          self.labelUSUARIO.place( x = 80, y = 10)

          self.labelP3.place( x = 20 , y = 70)
        
          self.P3A.place( x = 40 , y = 140)
          self.P3B.place( x = 40 , y = 165)
          self.P3C.place( x = 40 , y = 190)
          self.P3D.place( x = 40 , y = 215)

          self.labelP1.place( x = 20 , y = 245)
          
          self.P1A.place( x = 40 , y = 305)
          self.P1B.place( x = 40 , y = 330)
          self.P1C.place( x = 40 , y = 355)
          self.P1D.place( x = 40 , y = 380)

          self.labelP2.place( x = 20 , y = 410)
          
          self.P2A.place( x = 40 , y = 460)
          self.P2B.place( x = 40 , y = 485)
          self.P2C.place( x = 40 , y = 510)
          self.P2D.place( x = 40 , y = 535)             

          self.botevaluar.place( x = 250 , y = 580)
          self.botvolver.place( x = 350 , y = 580)
          self.labelNIVEL.place(x = 50, y = 45)
        self.Vquiz1.mainloop()
      
      
    self.labelN = Label(self.Vquiz,text="Nombre:", font=("Yu gothic",13, "bold"))
    self.labelA = Label(self.Vquiz,text="Apellido:", font=("Yu gothic",13, "bold"))
    self.QUIZ = Label(self.Vquiz,text="QUIZ\n¡PONTE A PRUEBA!", font=("Yu gothic",13, "bold"),fg = "#33B8FF")
    
    self.ENombre = ttk.Entry(self.Vquiz, textvariable=self.Nombre, width=20)
    self.EApellido = ttk.Entry(self.Vquiz, textvariable=self.Apellido, width=20)

    self.botingresar = Button(self.Vquiz,text="Ingresar",command=Ingresar, font=("Yu gothic",13, "bold"), cursor= "hand2")
    self.back = Button(self.Vquiz,text="Volver",command=back, font=("Yu gothic",13, "bold"), cursor= "hand2")
    
    self.labelN.place(x=20,y=65)
    self.ENombre.place(x=22,y=100)
    self.QUIZ.place(x=16,y=5)
    self.labelA.place(x=20,y=135)
    self.EApellido.place(x=22,y=170)
    self.botingresar.place(x=100,y=210)
    self.back.place(x=20,y=210)
    
    self.Vquiz.mainloop()
   
  def help(self):
    
    self.root.destroy()
    self.ayuda= Tk()
    self.ayuda.geometry("820x600+300+10")
    self.ayuda.resizable(0,0)
    
    self.ayuda.iconbitmap("Data\\ENE.ico")
    self.ayuda.title("Predisociación")

    self.image5=PhotoImage(file="Data\\help.png") 
    self.labeimg5=Label(self.ayuda,image=self.image5)
    def callback(url):
      webbrowser.open_new(url)
      self.label = Label(self.ayuda,text="https://youtu.be/FqS3OpuzT-0", fg="#7C3B97", cursor="hand2")
      self.label.bind("<Button-1>", lambda e: callback("https://youtu.be/FqS3OpuzT-0"))
      self.label.place( x = 635, y = 580)
      
    self.label = Label(self.ayuda,text="www.youtube.com", fg="blue", cursor="hand2")
    self.label.bind("<Button-1>", lambda e: callback("https://youtu.be/FqS3OpuzT-0"))
    
    self.back = Button(self.ayuda,text="Atrás",command=self.__init__, font=("Yu gothic",10, "bold"), cursor= "hand2")
    
    self.labeimg5.place( x = 0, y = 0)
    self.back.place( x = 650, y = 20)
    self.label.place( x = 635, y = 580)
    
    self.ayuda.mainloop()
    
  def NITROGENO(self):
    
    self.root.destroy()
    self.infnitro= Tk()
    self.infnitro.geometry("820x600+300+10")
    self.infnitro.resizable(0,0)
    self.infnitro.iconbitmap("Data\ENE.ico")
    self.infnitro.title("Predisociación")

    self.image3=PhotoImage(file="Data/nitro.png") 
    self.labeimg3=Label(self.infnitro,image=self.image3)
        
    self.back = Button(self.infnitro,text="Atrás",command=self.__init__, font=("Yu gothic",10, "bold"), cursor= "hand2")
    
    self.labeimg3.place( x = 0, y = 0)
    self.back.place( x = 700, y = 560)
   # self.label.place( x = 0, y = 0)
    
    self.infnitro.mainloop()
    
  def info(self):
    
    self.root.destroy()
    self.inform= Tk()
    self.inform.geometry("820x600+300+10")
    self.inform.resizable(0,0)
    self.inform.iconbitmap("Data\ENE.ico")
    self.inform.title("Predisociación")

    self.image1=PhotoImage(file="Data\info.png") 
    self.labeimg1=Label(self.inform,image=self.image1)
   
    self.back= Button(self.inform,text="Atrás",command=self.__init__, font=("Yu gothic",10, "bold"), cursor= "hand2")
 
    
    
    self.labeimg1.place( x = 0, y = 0)
    self.back.place( x = 700, y = 550)
    self.inform.mainloop()

  ####################  
  def pltv(self):
    typeP = str(self.type.get())
    title = str(self.Isotope.get())
    v=int(self.v.get())

    

    if title == '¹⁴N¹⁴N⁺':
      E=np.loadtxt("Data\E-N1414.dat")
      C=np.loadtxt("Data\C-N1414.dat")
    if title == '¹⁴N¹⁵N⁺':
      E=np.loadtxt("Data\E-N1415.dat")
      C=np.loadtxt("Data\C-N1415.dat")
    if title == '¹⁵N¹⁵N⁺':
      E=np.loadtxt("Data\E-N1515.dat")
      C=np.loadtxt("Data\C-N1515.dat")


    if typeP == 'c':
      
      plt.plot(C[:,v],'bo', label= 'Teóricos')
      plt.title(title)
      plt.xlabel("Número cuántico rotacional J")
      plt.ylabel("Constantes de predisociación $[10^8$/s]")
      plt.xticks(np.arange(0,20,step=2))
      plt.legend()
      plt.show()

    if typeP == 'd':   
    
      x1, y1 = [0, 10], [-108.51, -108.51]
      plt.plot(x1, y1,  color='black', linestyle='dashed', linewidth=1)  
      plt.plot(wvfC[0,:],-0.005*wvfC[v+1,:]**1+E[0,v],'m',label='Función Onda')
      plt.plot(xpotC, ypotC,'r',label='$C^2\Sigma_u^+ estado$')
      plt.plot(xpotB, ypotB,'b',label='$B^2\Sigma_u^+ estado$' )
      plt.title("Curvas de Energía Potencial")
      plt.xlim(1,10)
      plt.ylim(-108.8,-108.2)
      plt.xlabel("Distancia Internuclear $[a_0]$")
      plt.ylabel("Energía $[E_h]$")
    
      plt.legend()
      plt.show()

  def pltT(self):
    typeP = str(self.type.get())
    title = str(self.Isotope.get())
    T = float(self.T.get())
    if title == '¹⁴N¹⁴N⁺':
      C=np.loadtxt("Data\C-N1414.dat")
      E=np.loadtxt("Data\E-N1414.dat")
      xk,yk,ykerr = np.loadtxt("Data\kE1414.dat", unpack=True)
    if title == '¹⁴N¹⁵N⁺':
      C=np.loadtxt("Data\C-N1415.dat")
      E=np.loadtxt("Data\E-N1415.dat")
      xk,yk,ykerr = np.loadtxt("Data\kE1415.dat", unpack=True)
    if title == '¹⁵N¹⁵N⁺':
      C=np.loadtxt("Data\C-N1515.dat")
      E=np.loadtxt("Data\E-N1515.dat")
      xk,yk,ykerr = np.loadtxt("Data\kE1515.dat", unpack=True)

    if T == 0.0:
      messagebox.showinfo("¡USA OTRA TEMPERATURA!","Utiliza una temperatura\ndiferente de cero")
    if typeP == 'a':
        
      kb=8.617e-5 # Boltzmann constant in eV/K
      kb=kb/27.211396 # Boltzmann constant in Eh/K
      beta=1.0/(kb*T)
      F=np.zeros(len(E[0])) # Number of columns, i.e. number of vibrational states 
      D=np.zeros(len(E[0]))
      X=np.zeros((len(E),len(E[0]))) # Number of rows (rotational states) and columns
      for v in range(len(E[0])):
          for J in range(len(E)):
              F[v] += (2*J+1)*math.exp(-(E[J,v]-E[0,v])*beta) # Partition function for each v
      for v in range(len(E[0])):
          for J in range(len(E)):
              X[J,v] = (2*J+1)*math.exp(-(E[J,v]-E[0,v])*beta)/F[v] # Molar fraction
      for v in range(len(E[0])):
          for J in range(20):
              D[v] += X[J,v]*C[J,v] # Weighted predissociation rates
      plt.plot(D[:],'bo', label= 'Teóricos')
      plt.errorbar(xk,yk,yerr=ykerr,fmt='rx', label= 'Experimental') 
      plt.title(title)
      plt.ylabel("Constantes de Predisociación $[10^8$/s]")
      plt.xlabel("Número Cuántico Vibracional $\\nu $")
      plt.xticks(np.arange(0,10,step=1)) 
      plt.text(-0.15,7.1,"Datos experimentales:")
      plt.text(-0.15,6.0,"Molecular Physics, 1979, Vol.38")
      plt.legend()
      plt.show()

    if typeP == 'e':
  
      kb=8.617e-5 # Boltzmann constant in eV/K
      kb=kb/27.211396 # Boltzmann constant in Eh/K
      beta=1.0/(kb*T)
      F=np.zeros(len(E[0])) # Number of columns, i.e. number of vibrational states 
      X=np.zeros((len(E),len(E[0]))) # Number of rows (rotational states) and columns
      for v in range(len(E[0])):
          for J in range(len(E)):
            F[v] += (2*J+1)*math.exp(-(E[J,v]-E[0,v])*beta) # Partition function for each v
      for v in range(len(E[0])):
          for J in range(len(E)):
            X[J,v] = (2*J+1)*math.exp(-(E[J,v]-E[0,v])*beta)/F[v] # Molar fraction

      plt.plot(X[:,0],'bo')
      plt.title(str(self.Isotope.get()))
      plt.xlabel("Número Cuántico Rotacional J")
      plt.ylabel("Fracción Molar")
      Jmax=int(len(E))
      plt.xticks(np.arange(0,Jmax,step=3))
      plt.legend()
      plt.show()

  def pltJ(self):
    typeP = str(self.type.get())
    title = str(self.Isotope.get())
    if title == '¹⁴N¹⁴N⁺':
      C=np.loadtxt("Data\C-N1414.dat")
      E=np.loadtxt("Data\E-N1414.dat")
      xk,yk,ykerr = np.loadtxt("Data\kE1414.dat", unpack=True)
    if title == '¹⁴N¹⁵N⁺':
      C=np.loadtxt("Data\C-N1415.dat")
      E=np.loadtxt("Data\E-N1415.dat")
      xk,yk,ykerr = np.loadtxt("Data\kE1415.dat", unpack=True)
    if title == '¹⁵N¹⁵N⁺':
      C=np.loadtxt("Data\C-N1515.dat")
      E=np.loadtxt("Data\E-N1515.dat")
      xk,yk,ykerr = np.loadtxt("Data\kE1515.dat", unpack=True)
    
    if typeP == 'b':
      J = self.J.get()
      if J <= len(E):
        plt.plot(C[J,:],'bo', label= 'Teóricos')
        plt.errorbar(xk,yk,yerr=ykerr,fmt='rx', label= 'Experimental')
        plt.title(title)
        plt.xlabel("Número Cuántico Vibracional $\\nu $")
        plt.ylabel("Constantes de predisociación $[10^8$/s]")
        plt.xticks(np.arange(0,10,step=1))
        plt.text(-0.15,7.1,"Datos experimentales:")
        plt.text(-0.15,6.0,"Molecular Physics, 1979, Vol.38")
        plt.legend()
        plt.show()
      else:
        print("Too large J value")
    if typeP == 'c':
      v=self.v.get()
      plt.plot(C[:,v],'bo', label= 'Teóricos')
      plt.title(title)
      plt.xlabel("Número Cuántico Rotacional J")
      plt.ylabel("Constantes de Predisociación $[10^8$/s]")
      plt.xticks(np.arange(0,20,step=2))
      plt.legend()
      plt.show()

def main():
    myapp = app()
    return 0

if __name__ == '__main__':
    main()

