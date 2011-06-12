# Importe de las librerias implicadas.
import clutter
import os

# Clase que manipula al boton VOLVER.
class Volver(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (60,60)
        	self.set_position (530,410)
        	self.set_cogl_texture(volver)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		exit()

# Clase que manipula al boton GUARDAR 1.
class Guardar1(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (90,90)
        	self.set_position (272,172)
        	self.set_cogl_texture(guardar)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha_libro.py' libro_1")

# Clase que manipula al boton GUARDAR 2.
class Guardar2(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (90,90)
        	self.set_position (272,350)
        	self.set_cogl_texture(guardar)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha_libro.py' libro_2")
		
# Desarrollo de la ventana principal.
escenario = clutter.Stage()
escenario.set_title("TOQUIN - La libertad en un toque")
escenario.set_size(640,520)

# Importe de las texturas de los botones y mensajes.
guardar = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnGuardar.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
volver = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnVolver.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)

# Importe del fondo de la ventana principal.
fondo = clutter.Texture(filename="/home/potty/Toquin/img/libro1.jpg")
fondo.set_size(640,520)

# Instancias de las clases de los agregados.
btnVolver = Volver()
btnGuardar1 = Guardar1()
btnGuardar2 = Guardar2()

# Agregar los botones a la ventana principal.
escenario.add(fondo, btnVolver, btnGuardar1, btnGuardar2)

# Mostrar la ventana principal.
escenario.show_all()
escenario.connect('destroy', clutter.main_quit)
clutter.main()
