# Importe de las librerias implicadas.
import clutter
import os
import sys

x = sys.argv[1]

# Clase que manipula al boton REGRESAR.
class Volver(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (120,120)
        	self.set_position (450,323)
        	self.set_cogl_texture(volver)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		exit()

# Clase que manipula al boton GUARDAR.
class Guardar(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (120,120)
        	self.set_position (315,323)
        	self.set_cogl_texture(guardar)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		if (sys.argv[2] == "1"):
			os.system("python /home/potty/Toquin/src/elegir_sistema_operativo.py "+x)
		elif (sys.argv[2] == "2"):
			os.system("python /home/potty/Toquin/src/medio_pdf.py "+x)
		else:
			os.system("python /home/potty/Toquin/src/medio_iso.py "+x)
		
# Desarrollo de la ventana principal.
escenario = clutter.Stage()
escenario.set_title("TOQUIN - La libertad en un toque")
escenario.set_size(640,520)

# Importe de las texturas de los botones y mensajes.
guardar = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnGuardar.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
volver = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnVolver.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)

# Importe del fondo de la ventana principal.
fondo = clutter.Texture(filename="/home/potty/Toquin/img/"+x+".jpg")
fondo.set_size(640,520)

# Instancias de las clases de los agregados.
btnVolver = Volver()
btnGuardar = Guardar()

# Agregar los botones a la ventana principal.
escenario.add(fondo, btnVolver, btnGuardar)

# Mostrar la ventana principal.
escenario.show_all()
escenario.connect('destroy', clutter.main_quit)
clutter.main()
