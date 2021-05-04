class Usuario:

    #CONSTRUCTOR
    def __init__(self, username, nombre, apellido, nacimiento, sexo, password, telefono, tipoUsuario, especialidad):
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.sexo = sexo
        self.password = password
        self.telefono = telefono
        self.tipoUsuario = tipoUsuario
        self.especialidad = especialidad

    #GETTERS Y SETTERS
    def getUsername(self):
        return self.username
    def setUsername(self, username):
        self.username = username

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getApellido(self):
        return self.apellido
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def getNacimiento(self):
        return self.nacimiento
    def setNacimiento(self, nacimiento):
        self.nacimiento = nacimiento
    
    def getSexo(self):
        return self.sexo
    def setSexo(self, sexo):
        self.sexo = sexo
    
    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password
    
    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono = telefono
    
    def getTipoUsuario(self):
        return self.tipoUsuario
    def setTipoUsuario(self, tipoUsuario):
        self.tipoUsuario = tipoUsuario
    
    def getEspecialidad(self):
        return self.especialidad
    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad

    
    