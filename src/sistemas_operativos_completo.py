# Importe de las librerias implicadas.
import clutter
import os

# Clase que manipula al boton VOLVER.
class Volver(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (113,113)
        	self.set_position (458,325)
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
		self.set_size (113,34)
        	self.set_position (68,100)
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
		self.set_size (113,34)
        	self.set_position (197,100)
        	self.set_cogl_texture(fedora)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' fedora 0")
		
# Clase que manipula al boton ARCHLINUX.
class ArchLinux(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (327,100)
        	self.set_cogl_texture(archlinux)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' archlinux 0")
		
# Clase que manipula al boton CAELINUX.
class CaeLinux(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (458,100)
        	self.set_cogl_texture(caelinux)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' caelinux 0")
	
# Clase que manipula al boton DEBIAN.
class Debian(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (68,155)
        	self.set_cogl_texture(debian)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' debian 0")
		
# Clase que manipula al boton EDUBUNTU.
class Edubuntu(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (197,155)
        	self.set_cogl_texture(edubuntu)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' edubuntu 0")
		
# Clase que manipula al boton EDUCANIX.
class Educanix(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (327,210)
        	self.set_cogl_texture(educanix)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' educanix 0")
		
# Clase que manipula al boton GENTOO.
class Gentoo(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (458,210)
        	self.set_cogl_texture(gentoo)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' gentoo 0")
		
# Clase que manipula al boton GUADALINEX.
class GuadaLinex(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (68,210)
        	self.set_cogl_texture(guadalinex)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' guadalinex 0")
		
# Clase que manipula al boton KUBUNTU.
class Kubuntu(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (197,265)
        	self.set_cogl_texture(kubuntu)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' kubuntu 0")
		
# Clase que manipula al boton LINEX.
class Linex(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (327,265)
        	self.set_cogl_texture(linex)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' linex 0")
		
# Clase que manipula al boton LINUX MINT.
class LinuxMint(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (458,265)
        	self.set_cogl_texture(linuxmint)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' linuxmint 0")
		
# Clase que manipula al boton MANDRIVA.
class Mandriva(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (68,320)
        	self.set_cogl_texture(mandriva)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' mandriva 0")
		
# Clase que manipula al boton MUSIX.
class Musix(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (197,320)
        	self.set_cogl_texture(musix)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' musix 0")
		
# Clase que manipula al boton OPENSUSE.
class OpenSUSE(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (197,210)
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
		self.set_size (113,34)
        	self.set_position (458,155)
        	self.set_cogl_texture(pclinuxos)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' pclinuxos 0")
		
# Clase que manipula al boton SABAYON.
class Sabayon(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (68,375)
        	self.set_cogl_texture(sabayon)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' sabayon 0")
		
# Clase que manipula al boton SCIENTIFICLINUX.
class ScientificLinux(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (327,320)
        	self.set_cogl_texture(scientificlinux)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' scientificlinux 0")

# Clase que manipula al boton SKOLELINUX.
class Skolelinux(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (327,155)
        	self.set_cogl_texture(skolelinux)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' skolelinux 0")

# Clase que manipula al boton VENENUX.
class Venenux(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (458,212)
        	self.set_cogl_texture(venenux)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' venenux 0")

# Clase que manipula al boton UTUTO.
class Ututo(clutter.Texture):
	def __init__(self):		
		clutter.Texture.__init__(self)
		self.set_size (113,34)
        	self.set_position (68,265)
        	self.set_cogl_texture(ututo)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self, stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' ututo 0")

# Desarrollo de la ventana principal.
escenario = clutter.Stage()
escenario.set_title("TOQUIN - La libertad en un toque")
escenario.set_size(640,520)

# Importe de las texturas de los botones y mensajes.
volver = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnVolver.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
ubuntu = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnubuntu2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
archlinux = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnarchlinux2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
caelinux = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btncaelinux2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
debian = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btndebian2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
edubuntu = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnedubuntu2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
educanix = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btneducanix2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
fedora = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnfedora2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
gentoo = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btngentoo2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
guadalinex = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnguadalinex2.jpg',clutter.cogl.TEXTURE_NO_SLICING,clutter.cogl.PIXEL_FORMAT_ANY)
kubuntu = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnkubuntu2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
linex = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnlinex2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
linuxmint = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnlinuxmint2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
mandriva = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnmandriva2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
musix = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnmusix2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
opensuse = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnopensuse2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
pclinuxos = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnpclinuxos2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
sabayon = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnsabayon2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
scientificlinux = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnscientificlinux2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
skolelinux = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnskolelinux2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
ututo = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnututo2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
venenux = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnvenenux2.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)

# Importe del fondo de la ventana principal.
fondo = clutter.Texture(filename="/home/potty/Toquin/img/sistemas_operativos_2.jpg")
fondo.set_size(640,520)

# Instancias de las clases de los agregados.
btnVolver = Volver()
imgUbuntu = Ubuntu()
imgFedora = Fedora()
imgLinuxMint = LinuxMint()
imgOpenSUSE = OpenSUSE()
imgPCLinuxOS = PCLinuxOS()
imgDebian = Debian()
imgMandriva = Mandriva()
imgEdubuntu = Edubuntu()
imgSkolelinux = Skolelinux()
imgVenenux = Venenux()
imgLinex = Linex()
imgGuadaLinex = GuadaLinex()
imgEducanix = Educanix()
imgMusix = Musix()
imgUtuto = Ututo()
imgKubuntu = Kubuntu()
imgSabayon = Sabayon()
imgScientificLinux = ScientificLinux()
imgGentoo = Gentoo()
imgArchLinux = ArchLinux()
imgCaeLinux = CaeLinux()

# Agregar los botones a la ventana principal.
escenario.add(fondo, btnVolver, imgUbuntu, imgFedora, imgLinuxMint, imgOpenSUSE, imgPCLinuxOS, imgDebian, imgMandriva, imgEdubuntu, imgSkolelinux, imgVenenux, imgLinex, imgGuadaLinex, imgEducanix, imgMusix, imgUtuto, imgKubuntu, imgSabayon, imgScientificLinux, imgGentoo, imgArchLinux, imgCaeLinux)

# Mostrar la ventana principal.
escenario.show_all()
escenario.connect('destroy', clutter.main_quit)
clutter.main()
