class Cita:
    #CONSTRUCTOR
    def __init__(self, idCita, idPaciente, fecha, hora, motivo, estado, idDoctor):
        self.idCita = idCita
        self.idPaciente = idPaciente
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
        self.idDoctor = idDoctor
    
    #GETTERS Y SETTERS
    def getIdCita(self):
        return self.idCita
    def setIdCita(self, idCita):
        self.idCita = idCita
    
    def getIdPaciente(self):
        return self.idPaciente
    def setIdPaciente(self, idPaciente):
        self.idPaciente = idPaciente
    
    def getFecha(self):
        return self.fecha
    def setFecha(self, fecha):
        self.fecha = fecha
    
    def getHora(self):
        return self.hora
    def setHora(self, hora):
        self.hora = hora
    
    def getMotivo(self):
        return self.motivo
    def setMotivo(self, motivo):
        self.motivo = motivo
    
    def getEstado(self):
        return self.estado
    def setEstado(self, estado):
        self.estado = estado
    
    def getIdDoctor(self):
        return self.idDoctor
    def setIdDoctor(self, idDoctor):
        self.idDoctor = idDoctor
    