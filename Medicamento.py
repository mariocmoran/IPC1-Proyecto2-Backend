class Medicamento:

    #CONSTRUCTOR
    def __init__(self, codigo, nombre, precio, descripcion, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad

        #GETTERS Y SETTERS
    def getCodigo(self):
        return self.codigo
    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio

    def getDescripcion(self):
        return self.descripcion
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def getCantidad(self):
        return self.cantidad
    def setCantidad(self, cantidad):
        self.cantidad = cantidad