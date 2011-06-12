# Importe de las librerias implicadas.
import clutter
import os
import sys

kit = sys.argv[1]

# Desarrollo de la ventana principal.
escenario = clutter.Stage()
escenario.set_title("TOQUIN - La libertad en un toque")
escenario.set_size(425,250)

# Importe de las texturas de los botones.
linux = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnlinux.png',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
mac = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnmac.png',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
windows = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnwindows.png',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)

# Importe del fondo de la ventana principal.
fondo = clutter.Texture(filename="/home/potty/Toquin/img/sistemaoperativo.jpg")
fondo.set_size(425,250)

# Clase que manipula al boton LINUX.
class Linux(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (100,100)
        	self.set_position (164,70)
        	self.set_cogl_texture(linux)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
		os.system("python '/home/potty/Toquin/src/medio_iso.py' "+kit+"_l")
		exit()

# Clase que manipula al boton MAC.
class Mac(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (100,100)
        	self.set_position (287,70)
        	self.set_cogl_texture(mac)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
		os.system("python '/home/potty/Toquin/src/medio_iso.py' "+kit+"_m")
		exit()

# Clase que manipula al boton WINDOWS.
class Windows(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (100,100)
        	self.set_position (42,70)
        	self.set_cogl_texture(windows)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
		os.system("python '/home/potty/Toquin/src/medio_iso.py' "+kit+"_w")
		exit()

# Instancias de las clases de los agregados.
btnLinux = Linux()
btnMac = Mac()
btnWindows = Windows()

# Agregar los botones a la ventana principal.
escenario.add(fondo, btnLinux, btnMac, btnWindows)

# Mostrar la ventana principal.
escenario.show_all()
escenario.connect('destroy', clutter.main_quit)
clutter.main()
