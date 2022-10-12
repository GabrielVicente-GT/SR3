#Gabriel Alejandro Vicente Lorenzo
#SR1 UVG

#Se importan los metodos solicitados por el ejercicios
import gl
import Creando

gl.glInit()
#Se crea la Ventana (Que renderiza a.bmp)
gl.glCreateWindow(1024,1024)

#Cambia el color con el que trabaja Clear
gl.glClearColor(0,0,0)

#Pinta TODOELMAPA de bits de un mismo color
gl.glClear()

#Llama a la funcion que permite a la funcion crear iniciar con el proceso de lineas
Creando.crear()

#Escribe el archivo .bmp
gl.glFinish()
