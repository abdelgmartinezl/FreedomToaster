# Importe de las librerias implicadas.
import clutter
import os

# Desarrollo de la ventana principal.
escenario = clutter.Stage()
escenario.set_title("TOQUIN - La libertad en un toque")
escenario.set_size(640,520)
escenario.set_position(0,-16)

# Importe de las texturas de los botones y mensajes.
sistemas_operativos = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnSistemasOperativos.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
programas = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnProgramas.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
libros = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnLibros.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
musica = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnMusica.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
imagenes = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnImagenes.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
podcasts = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnPodcasts.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
kit_basico = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnKitBasico.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
kit_diseno = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnKitDiseno.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
kit_multimedia = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnKitMultimedia.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
kit_ingenieria = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnKitIngenieria.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
mas_kits = clutter.cogl.texture_new_from_file("/home/potty/Toquin/img/btnMas.jpg",clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)

# Importe del fondo de la ventana principal.
fondo = clutter.Texture(filename="/home/potty/Toquin/img/principal.jpg")
fondo.set_size(640,520)
fondo.set_position(0,0)

# Clase que manipula al boton SISTEMAS OPERATIVOS.
class SistemasOperativos(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (120,120)
        	self.set_position (105,170)
        	self.set_cogl_texture(sistemas_operativos)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	os.system("python '/home/potty/Toquin/src/sistemas_operativos.py'")

# Clase que manipula al boton PROGRAMAS.
class Programas(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (120,120)
        	self.set_position (255,170)
        	self.set_cogl_texture(programas)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	print " - EN ESPERA DE PROGRAMAS -"

# Clase que manipula al boton LIBROS.
class Libros(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (60,60)
        	self.set_position (405,170)
        	self.set_cogl_texture(libros)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	os.system("python '/home/potty/Toquin/src/libro.py'")

# Clase que manipula al boton MUSICA.
class Musica(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (60,60)
        	self.set_position (405,230)
        	self.set_cogl_texture(musica)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	print " - EN ESPERA DE MUSICA - "

# Clase que manipula al boton IMAGENES.
class Imagenes(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (60,60)
        	self.set_position (465,170)
        	self.set_cogl_texture(imagenes)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	os.system("python '/home/potty/Toquin/src/imagenes.py' imagenes")

# Clase que manipula al boton PODCASTS.
class Podcasts(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (60,60)
        	self.set_position (465,230)
        	self.set_cogl_texture(podcasts)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	print " - EN ESPERA DE PODCASTS - "

# Clase que manipula al boton KIT BASICO.
class KitBasico(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (100,100)
        	self.set_position (95,350)
        	self.set_cogl_texture(kit_basico)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	os.system("python '/home/potty/Toquin/src/ficha.py' kit_basico 1")
        	
# Clase que manipula al boton KIT DISENO.
class KitDiseno(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (100,100)
        	self.set_position (210,350)
        	self.set_cogl_texture(kit_diseno)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	os.system("python '/home/potty/Toquin/src/ficha.py' kit_diseno 1")

# Clase que manipula al boton KIT MULTIMEDIA.
class KitMultimedia(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (100,100)
        	self.set_position (325,350)
        	self.set_cogl_texture(kit_multimedia)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	os.system("python '/home/potty/Toquin/src/ficha.py' kit_multimedia 1")

# Clase que manipula al boton KIT INGENIERIA.
class KitIngenieria(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (100,100)
        	self.set_position (440,350)
        	self.set_cogl_texture(kit_ingenieria)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
        	os.system("python '/home/potty/Toquin/src/kit_ingenieria.py'")
	
# Instancias de las clases de los agregados.
btnSistemasOperativos = SistemasOperativos()
btnProgramas = Programas()
btnLibros = Libros()
btnMusica = Musica()
btnImagenes = Imagenes()
btnPodcasts = Podcasts()
btnKitBasico = KitBasico()
btnKitDiseno = KitDiseno()
btnKitMultimedia = KitMultimedia()
btnKitIngenieria = KitIngenieria()

# Agregar los botones a la ventana principal.
escenario.add(fondo, btnSistemasOperativos, btnProgramas, btnLibros, btnMusica, btnImagenes, btnPodcasts, btnKitBasico, btnKitDiseno, btnKitMultimedia, btnKitIngenieria)

# Mostrar la ventana principal.
escenario.show_all()
escenario.connect('destroy', clutter.main_quit)
clutter.main()
