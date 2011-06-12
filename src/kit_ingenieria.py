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

# Clase que manipula al boton INGENIERA CIVIL.
class IngCivil(clutter.Texture):
	def __init__(self):
		clutter.Texture.__init__(self)
		self.set_size (105,105)
        	self.set_position (165,150)
        	self.set_cogl_texture(ing_civil)
        	self.set_reactive(True)
        	# Llamada al metodo que controla el evento click.
        	self.connect("button-press-event",self.clicked)

	def clicked(self,stage, event):
		os.system("python '/home/potty/Toquin/src/ficha.py' kit_ingenieria_civil 1")
		
# Desarrollo de la ventana principal.
escenario = clutter.Stage()
escenario.set_title("TOQUIN - La libertad en un toque")
escenario.set_size(640,520)

# Importe de las texturas de los botones y mensajes.
ing_civil = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/ing_civil.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)
volver = clutter.cogl.texture_new_from_file('/home/potty/Toquin/img/btnVolver.jpg',clutter.cogl.TEXTURE_NO_SLICING, clutter.cogl.PIXEL_FORMAT_ANY)

# Importe del fondo de la ventana principal.
fondo = clutter.Texture(filename="/home/potty/Toquin/img/sistemas_operativos_1.jpg")
fondo.set_size(640,520)

# Instancias de las clases de los agregados.
btnVolver = Volver()
btnIngCivil = IngCivil()

# Agregar los botones a la ventana principal.
escenario.add(fondo, btnVolver, btnIngCivil)

# Mostrar la ventana principal.
escenario.show_all()
escenario.connect('destroy', clutter.main_quit)
clutter.main()
