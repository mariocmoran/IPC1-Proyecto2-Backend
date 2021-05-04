class Medicina:

    #CONSTRUCTOR
    def __init__(self, idMedicina, nombre, precio, cantidad, subtotal):
        self.idMedicina = idMedicina
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.subtotal = subtotal
    
    #GETTERS Y SETTERS
    def getIdMedicina(self):
        return self.idMedicina
    def setIdMedicina(self, idMedicina):
        self.idMedicina = idMedicina
    
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio

    def getCantidad(self):
        return self.total
    def setCantidad(self, total):
        self.total = total
    
    def getSubtotal(self):
        return self.subtotal
    def setSubtotal(self, subtotal):
        self.subtotal = subtotal