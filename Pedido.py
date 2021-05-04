class Pedido:

    #CONSTRUCTOR
    def __init__(self, idPedido, idPaciente, Medicinas, total):
        self.idPedido = idPedido
        self.idPaciente = idPaciente
        self.Medicinas = Medicinas
        self.total = total
    
    #GETTERS Y SETTERS
    def getIdPedido(self):
        return self.idPedido
    def setIdPedido(self, idPedido):
        self.idPedido = idPedido
    
    def getIdPaciente(self):
        return self.idPaciente
    def setIdPaciente(self, idPaciente):
        self.idPaciente = idPaciente
    
    def getMedicinas(self):
        return self.Medicinas
    def setMedicinas(self, Medicinas):
        self.Medicinas = Medicinas
    
    def getTotal(self):
        return self.total
    def setTotal(self, total):
        self.total = total