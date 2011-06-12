# Importe de las librerias implicadas.
import clutter
import os
import sys

x = sys.argv[1]
lcd = os.system("df -h -m | grep /dev/sr0 | cut -c 45-51")
lusb = os.system("df -h -m | grep /dev/sdb | cut -c 47-50")
t = os.system("du -h -m /home/potty/Toquin/libros/"+x+".pdf | cut -c 1-4")

# Desarrollo de la ventana principal.
escenario = clutter.Stage()
escenario.set_title("TOQUIN - La libertad en un toque")
escenario.set_size(375,250)
escenario.set_position(132,135)

# Importe de las texturas de los botones.
usb = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnusb.png',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
cd = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btncd.png',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)

# Importe del fondo de la ventana principal.
fondo = clutter.Texture(filename="/home/potty/Toquin/img/medios.jpg")
fondo.set_size(375,250)

# Clase que manipula al boton USB.
class USB(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (115,115)
        	self.set_position (210,70)
        	self.set_cogl_texture(usb)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
		if lusb > t:
			os.system("cp /home/potty/Toquin/libros/"+x+".pdf /dev/sdb/")
			exit()
		else:
			print " - NO SE PUEDE - "
			exit()

# Clase que manipula al boton CD.
class CD(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (115,115)
        	self.set_position (50,70)
        	self.set_cogl_texture(cd)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
		if lcd > t:
			os.system("cdrecord -eject /home/potty/Toquin/libros/"+x+".pdf")
			exit()
		else:
			print " - NO SE PUEDE - "
			exit()
		
# Instancias de las clases de los agregados.
btnUSB = USB()
btnCD = CD()

# Agregar los botones a la ventana principal.
escenario.add(fondo, btnUSB, btnCD)
# Mostrar la ventana principal.
escenario.show_all()
escenario.connect('destroy', clutter.main_quit)
clutter.main()
