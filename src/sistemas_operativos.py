# Importe de las librerias implicadas.
import clutter
import os

# Clase que manipula al boton VOLVER.
class Volver(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (130,130)
        	self.set_position (435,315)
        	self.set_cogl_texture(volver)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		exit()

# Clase que manipula al boton UBUNTU.
class Ubuntu(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (105,105)
        	self.set_position (60,150)
        	self.set_cogl_texture(ubuntu)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' ubuntu 0")

# Clase que manipula al boton FEDORA.
class Fedora(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (105,105)
        	self.set_position (165,150)
        	self.set_cogl_texture(fedora)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' fedora 0")
		
# Clase que manipula al boton OPENSUSE.
class OpenSUSE(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (105,105)
        	self.set_position (270,150)
        	self.set_cogl_texture(opensuse)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' opensuse 0")
		
# Clase que manipula al boton PCLINUXOS.
class PCLinuxOS(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (105,105)
        	self.set_position (375,150)
        	self.set_cogl_texture(pclinuxos)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' pclinuxos 0")
		
# Clase que manipula al boton MANDRIVA.
class Mandriva(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (105,105)
        	self.set_position (480,150)
        	self.set_cogl_texture(mandriva)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' mandriva 0")
		
# Clase que manipula al boton OTROS SISTEMAS OPERATIVOS.
class OtrosSistemasOperativos(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (280,115)
        	self.set_position (77,345)
        	self.set_cogl_texture(otros_sistemas_operativos)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/sistemas_operativos_completo.py'")
		
# Desarrollo de la ventana principal.
escenario = clutter.Stage()
escenario.set_title("TOQUIN - La libertad en un toque")
escenario.set_size(640,520)

# Importe de las texturas de los botones y mensajes.
ubuntu = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnubuntu.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
fedora = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnfedora.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
opensuse = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnopensuse.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
pclinuxos = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnpclinuxos.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
mandriva = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnmandriva.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
otros_sistemas_operativos = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnVerCompleta.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
volver = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnVolver.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)

# Importe del fondo de la ventana principal.
fondo = clutter.Texture(filename="/home/potty/Toquin/img/sistemas_operativos_1.jpg")
fondo.set_size(640,520)

# Instancias de las clases de los agregados.
btnVolver = Volver()
btnUbuntu = Ubuntu()
btnFedora = Fedora()
btnOpenSUSE = OpenSUSE()
btnPCLinuxOS = PCLinuxOS()
btnMandriva = Mandriva()
btnOtros = OtrosSistemasOperativos()

# Agregar los botones a la ventana principal.
escenario.add(fondo, btnVolver, btnUbuntu, btnFedora, btnOpenSUSE, btnPCLinuxOS, btnMandriva, btnOtros)

# Mostrar la ventana principal.
escenario.show_all()
escenario.connect('destroy', clutter.main_quit)
clutter.main()
