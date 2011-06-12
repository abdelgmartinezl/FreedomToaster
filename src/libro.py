# Importe de las librerias implicadas.
import clutter
import os

# Clase que manipula al boton VOLVER.
class Volver(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (130,130)
        	self.set_position (335,315)
        	self.set_cogl_texture(volver)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		exit()

# Clase que manipula al boton TIPO 1.
class Tipo1(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (130,130)
        	self.set_position (98,147)
        	self.set_cogl_texture(tipo1)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/libro1.py'")

# Clase que manipula al boton TIPO 2.
class Tipo2(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (130,130)
        	self.set_position (253,147)
        	self.set_cogl_texture(tipo2)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/libro2.py'")
		
# Clase que manipula al boton TIPO 3.
class Tipo3(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (130,130)
        	self.set_position (408,147)
        	self.set_cogl_texture(tipo3)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/libro3.py'")

# Clase que manipula al boton TIPO 4.
class Tipo4(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (130,130)
        	self.set_position (180,315)
        	self.set_cogl_texture(tipo4)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/libro4.py'")

# Desarrollo de la ventana principal.
escenario = clutter.Stage()
escenario.set_title("TOQUIN - La libertad en un toque")
escenario.set_size(640,520)

# Importe de las texturas de los botones y mensajes.
tipo1 = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/tipo1.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
tipo2 = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/tipo2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
tipo3 = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/tipo3.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
tipo4 = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/tipo4.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
volver = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnVolver.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)

# Importe del fondo de la ventana principal.
fondo = clutter.Texture(filename="/home/potty/Toquin/img/libro.jpg")
fondo.set_size(640,520)

# Instancias de las clases de los agregados.
btnVolver = Volver()
btnTipo1 = Tipo1()
btnTipo2 = Tipo2()
btnTipo3 = Tipo3()
btnTipo4 = Tipo4()

# Agregar los botones a la ventana principal.
escenario.add(fondo, btnVolver, btnTipo1, btnTipo2, btnTipo3, btnTipo4)

# Mostrar la ventana principal.
escenario.show_all()
escenario.connect('destroy', clutter.main_quit)
clutter.main()
