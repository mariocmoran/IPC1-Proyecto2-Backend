class Receta:
    #CONSTRUCTOR
    def __init__(self, nombrePaciente, fecha, padecimiento, descripcion):
        self.nombrePaciente = nombrePaciente
        self.fecha = fecha
        self.padecimiento = padecimiento
        self.descripcion = descripcion
    
    #GETTERS Y SETTERS
    def getNombrePaciente(self):
        return self.nombrePaciente
    def serNombrePaciente(self, nombrePaciente):
        self.nombrePaciente = nombrePaciente
    
    def getFecha(self):
        return self.fecha
    def serFecha(self, fecha):
        self.fecha = fecha
    
    def getPadecimiento(self):
        return self.padecimiento
    def serPadecimiento(self, padecimiento):
        self.padecimiento = padecimiento
    
    def getDescripcion(self):
        return self.descripcion
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    