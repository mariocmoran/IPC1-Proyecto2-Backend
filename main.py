from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from Usuario import Usuario
from Medicamento import Medicamento
from Medicina import Medicina
from Cita import Cita
from Pedido import Pedido
from Receta import Receta

Usuarios = []
Medicamentos = []
Pedidos = []
Citas = [] 
Recetas = []

idMedicamentos = 1000
idCitas = 2000
idPedidos = 3000
app = Flask(__name__)
CORS(app)

Usuarios.append(Usuario('admin', 'Carlos', 'Jimenez', 'null', True, '1234', 'null', 3, 'Null'))
Usuarios.append(Usuario('mariopaciente', 'Mario', 'Moran', '11-01-2002', True, '12345678', '5462 4892', 0, ''))
Usuarios.append(Usuario('mariodoctor', 'Mario', 'Moran', '11-01-2002', True, '12345678', '5462 4892', 1, 'Cirujano'))
Usuarios.append(Usuario('marioenfermera', 'Angela', 'Hernandez', '20-05-2001', False, '12345678', '4562 8391', 2, ''))

Medicamentos.append(Medicamento(1000, 'Aspirina', 50.00, 'Pastillas para el dolor', 50))
Medicamentos.append(Medicamento(999, 'Aspirina 2', 60.00, 'Pastillas para el dolor', 80))
Medicamentos.append(Medicamento(998, 'Aspirina 3', 15.00, 'Pastillas para el dolor', 10))
Medicamentos.append(Medicamento(997, 'Aspirina 4', 15.00, 'Pastillas para el dolor', 10))
Medicamentos.append(Medicamento(996, 'Aspirina 5', 15.00, 'Pastillas para el dolor', 10))

MedicinasP = []
medici = {
    'idMedicina': 999,
    'nombre': 'Aspirina',
    'precio': 50.00,
    'cantidad': 2,
    'subtotal': 100.00
}
MedicinasP.append(medici)
medici = {
    'idMedicina': 1000,
    'nombre': 'Aspirina 2',
    'precio': 60.00,
    'cantidad': 5,
    'subtotal': 350.00
}
MedicinasP.append(medici)
Pedido(3000, 'mariopaciente', MedicinasP, 450)
Pedidos.append(Pedido)

Citas.append(Cita(2000, 'mariopaciente', '06-11-2021', '14:00', 'Dolores de cuerpo serveros. Cansancio y presión alta', 'Pendiente', ''))

#======================================================= USUARIOS ==============================================================

#MANDAR EL ARREGLO DE USUARIOS
@app.route('/Usuarios', methods=['GET'])
def getUsarios():
    global Usuarios
    Datos = []
    for Usuario in Usuarios:
        objetoJson = {
            "Username": Usuario.getUsername(),
            "Nombre": Usuario.getNombre(),
            "Apellido": Usuario.getApellido(),
            "Nacimiento": Usuario.getNacimiento(),
            "Sexo": Usuario.getSexo(),
            "Password": Usuario.getPassword(),
            "Telefono": Usuario.getTelefono(),
            "Tipo": Usuario.getTipoUsuario(),
            "Especialidad": Usuario.getEspecialidad()
        }
        Datos.append(objetoJson)
    return (jsonify(Datos))

#ENCONTRAR UN USUARIO POR SU NOMBRE 
@app.route('/Usuarios/<string:user>', methods = ['GET'])
def obtenerUsuario(user):
    global Usuarios
    for Usuario in Usuarios:
        if (Usuario.getUsername() == user):
            objetoJson = {
                "Username": Usuario.getUsername(),
                "Nombre": Usuario.getNombre(),
                "Apellido": Usuario.getApellido(),
                "Nacimiento": Usuario.getNacimiento(),
                "Sexo": Usuario.getSexo(),
                "Password": Usuario.getPassword(),
                "Telefono": Usuario.getTelefono(),
                "Tipo": Usuario.getTipoUsuario(),
                "Especialidad": Usuario.getEspecialidad()
            }
            return (jsonify(objetoJson))
    salida = {"Mensaje": "ERROR: El usuario no existe."}
    return (jsonify(salida))

#AGREGAR UN USUARIO
@app.route('/Usuarios', methods=['POST'])
def agregarUsuario():
    global Usuarios
    username = request.json['Username']
    
    if (unico(username, "")):
        nombre = request.json['Nombre']
        apellido = request.json['Apellido']
        nacimiento = request.json['Nacimiento']
        sexo = request.json['Sexo']
        password = request.json['Password']
        telefono = request.json['Telefono']
        tipo = request.json['Tipo']
        especialidad = request.json['Especialidad']
        nuevo = Usuario(username, nombre, apellido, nacimiento, sexo, password, telefono, tipo, especialidad)
        Usuarios.append(nuevo)
        return jsonify({'Mensaje': 'Se agregó al usuario correctamente.'})
    else:
        return jsonify({'Mensaje': 'Error: El usuario ya existe'})

#ACTUALIZAR UN USUARIO BUSCANDOLO POR SU USERNAME
@app.route('/Usuarios/<string:username>', methods=['PUT'])
def actualizarUsuario(username):
    global Usuarios
    user = request.json['Username']
    if unico(user, username):
        for i in range(len(Usuarios)):
            if username == Usuarios[i].getUsername():
                Usuarios[i].setUsername(request.json['Username'])
                Usuarios[i].setNombre(request.json['Nombre'])
                Usuarios[i].setApellido(request.json['Apellido'])
                Usuarios[i].setNacimiento(request.json['Nacimiento'])
                Usuarios[i].setSexo(request.json['Sexo'])
                Usuarios[i].setPassword(request.json['Password'])
                Usuarios[i].setTelefono(request.json['Telefono'])
                Usuarios[i].setTipoUsuario(request.json['Tipo'])
                Usuarios[i].setEspecialidad(request.json['Especialidad'])

                return jsonify({"Mensaje": "Se modificó correctamente."})
        return jsonify({"Mensaje": "ERROR: El usuario a modificar no existe."})
    else:
        return jsonify({"Mensaje": "ERROR: Ya existe un usuario con este nombre de usuario"})

#ELIMINAR USUARIO BUSCANDOLO POR EL USERNAME
@app.route('/Usuarios/<string:username>', methods=['DELETE'])
def eliminarUsuario(username):
    for i in range(len(Usuarios)):
        if username == Usuarios[i].getUsername():
            del Usuarios[i]
            return jsonify({"Mensaje": "Se eliminó el usuario correctamente"})
    return jsonify({"Mensaje": "ERROR: El usuario no existe."})

#VERIFICAR SI EL USUARIO EXISTE
def unico(user, username):
    global Usuarios
    contador = 0
    for Usuario in Usuarios:
        if user == Usuario.getUsername():
            contador+=0
        else:
            contador+=1
    if contador == len(Usuarios):
        return True
    else:
        if user == username:
            return True
        else:
            return False

#======================================================= MEDICAMENTOS ==============================================================
#MANDAR EL ARREGLO DE MEDICAMENTOS
@app.route('/Medicamentos', methods=['GET'])
def getMedicamentos():
    global Medicamentos
    Datos = []
    for Medicamento in Medicamentos:
        objetoJson = {
            "Codigo": Medicamento.getCodigo(),
            "Nombre": Medicamento.getNombre(),
            "Precio": Medicamento.getPrecio(),
            "Descripcion": Medicamento.getDescripcion(),
            "Cantidad": Medicamento.getCantidad()
        }
        Datos.append(objetoJson)
    return (jsonify(Datos))

#ENCONTRAR UN MEDICAMENTO POR SU CODIGO 
@app.route('/Medicamentos/<string:codigo>', methods = ['GET'])
def obtenerMedicamento(codigo):
    global Medicamentos
    for Medicamento in Medicamentos:
        if (Medicamento.getCodigo() == int(codigo)):
            objetoJson = {
                "Codigo": Medicamento.getCodigo(),
                "Nombre": Medicamento.getNombre(),
                "Precio": Medicamento.getPrecio(),
                "Descripcion": Medicamento.getDescripcion(),
                "Cantidad": Medicamento.getCantidad()
            }
            return (jsonify(objetoJson))
    salida = {"Mensaje": "ERROR: El usuario no existe."}
    return (jsonify(salida))

#AGREGAR UN MEDICAMENTO
@app.route('/Medicamentos', methods=['POST'])
def agregarMedicamento():
    global Medicamentos
    global idMedicamentos
    idMedicamentos+=1
    codigo = idMedicamentos
    nombre = request.json['Nombre']
    precio = request.json['Precio']
    descripcion = request.json['Descripcion']
    cantidad = request.json['Cantidad']
    nuevo = Medicamento(codigo, nombre, precio, descripcion, cantidad)
    Medicamentos.append(nuevo)
    return jsonify({'Mensaje': 'Se agregó al usuario correctamente.'})

#ACTUALIZAR UN MEDICAMENTO BUSCANDOLO POR SU CODIGO
@app.route('/Medicamentos/<string:codigo>', methods=['PUT'])
def actualizarMedicamento(codigo):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if int(codigo) == Medicamentos[i].getCodigo():
            Medicamentos[i].setNombre(request.json['Nombre'])
            Medicamentos[i].setPrecio(request.json['Precio'])
            Medicamentos[i].setDescripcion(request.json['Descripcion'])
            Medicamentos[i].setCantidad(request.json['Cantidad'])

            return jsonify({"Mensaje": "Se modificó correctamente."})
    return jsonify({"Mensaje": "ERROR: El Medicamento a modificar no existe."})

#ELIMINAR MEDICAMENTO BUSCANDOLO POR EL CODIGO
@app.route('/Medicamentos/<string:codigo>', methods=['DELETE'])
def eliminarCodigo(codigo):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if int(codigo) == Medicamentos[i].getCodigo():
            del Medicamentos[i]
            return jsonify({"Mensaje": "Se eliminó el medicamento correctamente"})
    return jsonify({"Mensaje": "ERROR: El medicamento no existe."})

#================================================ CITAS DE PACIENTES ======================================================

#MANDAR EL ARREGLO DE CITAS
@app.route('/Citas', methods=['GET'])
def getCitas():
    global Citas
    Datos = []
    for Cita in Citas:
        objetoJson = {
            "IdCita": Cita.getIdCita(),
            "IdPaciente": Cita.getIdPaciente(),
            "Fecha": Cita.getFecha(),
            "Hora": Cita.getHora(),
            "Motivo": Cita.getMotivo(),
            "Estado": Cita.getEstado(),
            "IdDoctor": Cita.getIdDoctor()
        }
        Datos.append(objetoJson)
    return (jsonify(Datos))

#ENCONTRAR UNA CITA POR SU ID 
@app.route('/Citas/<string:codigo>', methods = ['GET'])
def obtenerCita(codigo):
    global Citas
    for Cita in Citas:
        if (Cita.getIdCita() == int(codigo)):
            objetoJson = {
                "IdCita": Cita.getIdCita(),
                "IdPaciente": Cita.getIdPaciente(),
                "Fecha": Cita.getFecha(),
                "Hora": Cita.getHora(),
                "Motivo": Cita.getMotivo(),
                "Estado": Cita.getEstado(),
                "IdDoctor": Cita.getIdDoctor()
            }
            return (jsonify(objetoJson))
    salida = {"Mensaje": "ERROR: La cita no existe."}
    return (jsonify(salida))

#AGREGAR UNA CITA
@app.route('/Citas', methods=['POST'])
def agregarCita():
    global Citas
    global idCitas
    idCitas+=1
    if citaUnica(request.json['IdPaciente']):
        idc = idCitas
        idp = request.json['IdPaciente']
        fecha = request.json['Fecha']
        hora = request.json['Hora']
        motivo = request.json['Motivo']
        estado = request.json['Estado']
        idd = request.json['IdDoctor']
        nuevo = Cita(idc, idp, fecha, hora, motivo, estado, idd)
        Citas.append(nuevo)
        return jsonify({'Mensaje': 'La cita se agregó correctamente.'})
    return jsonify({'Mensaje': 'Usted tiene una cita pendiente o Aceptada. No puede solicitar una nueva.'})

#ACTUALIZAR UNA CITA BUSCANDOLO POR SU ID
@app.route('/Citas/<string:codigo>', methods=['PUT'])
def actualizarCita(codigo):
    global Citas
    for i in range(len(Citas)):
        if (int(codigo) == Citas[i].getIdCita()):
            Citas[i].setIdPaciente(request.json['IdPaciente'])
            Citas[i].setFecha(request.json['Fecha'])
            Citas[i].setHora(request.json['Hora'])
            Citas[i].setMotivo(request.json['Motivo'])
            Citas[i].setEstado(request.json['Estado'])
            Citas[i].setIdDoctor(request.json['IdDoctor'])
            return jsonify({"Mensaje": "Se modificó correctamente."})
    else:    
        return jsonify({"Mensaje": "ERROR: La cita a modificar no existe."})


#VERIFICAR SI EL PACIENTE YA HIZO UNA CITA
def citaUnica(idPaciente):
    global Citas
    contador = 0  
    for Cita in Citas:
        if (idPaciente == Cita.getIdPaciente() and Cita.getEstado() != "Completada" and Cita.getEstado() != "Rechazada"):
            contador+=0
        else:
            contador+=1
    if contador == len(Citas):
        return True
    else:
        return False

#================================================ PEDIDOS DE PACIENTES ======================================================

#MANDAR EL ARREGLO DE PEDIDOS
@app.route('/Pedidos', methods=['GET'])
def getPedidos():
    global Pedidos
    Datos = []
    for Pedido in Pedidos:
        Medicinas = Pedido.getMedicinas()
        objeto = {
            "IdPedido": Pedido.getIdPedido(),
            "IdPaciente": Pedido.getIdPaciente(),
            "Medicinas": Medicinas,
            "Total": Pedido.getTotal()
        }
        Datos.append(objeto)
    return (jsonify(Datos))

#GUARDAR UN PEDIDO EN EL ARREGLO DE PEDIDOS
@app.route('/Pedidos', methods=['POST'])
def agregarPedido():
    global Pedidos
    global idPedidos
    idPedidos+=1
    idpedido = idPedidos
    idpaciente = request.json['IdPaciente']
    total = request.json['Total']
    medicinas = request.json['Medicinas']
    nuevo = Pedido(idpedido, idpaciente, medicinas, total)
    Pedidos.append(nuevo)
    return ({"Mensaje": "Pedido recibido correctamente."})

#ENCONTRAR UN PEDIDO POR EL ID DEL PACIENTE 
@app.route('/Pedidos/<string:codigo>', methods = ['GET'])
def obtenerPedido(codigo):
    global Pedidos
    for Pedido in Pedidos:
        if (Pedido.getIdPaciente() == codigo and Pedido.getIdPedido() == idPedidos):
            objetoJson = {
                "IdPedido": Pedido.getIdPedido(),
                "IdPaciente": Pedido.getIdPaciente(),
                "Medicinas": Pedido.getMedicinas(),
                "Total": Pedido.getTotal()
            }
            return (jsonify(objetoJson))
    salida = {"Mensaje": "ERROR: El pedido no existe."}
    return (jsonify(salida))

#======================================================= RECETAS ==========================================================

#MANDAR EL ARREGLO DE RECETAS
@app.route('/Recetas', methods=['GET'])
def getRecetas():
    global Recetas
    Datos = []
    for Receta in Recetas:
        objeto = {
            "NombrePaciente": Receta.getNombrePaciente(),
            "Fecha": Receta.getFecha(),
            "Padecimiento": Receta.getPadecimiento(),
            "Descripcion": Receta.getDescripcion()
        }
        Datos.append(objeto)
    return (jsonify(Datos))

#GUARDAR UNA RECETA EN EL ARREGLO DE RECETAS
@app.route('/Recetas', methods=['POST'])
def agregarReceta():
    global Recetas
    nombrePaciente = request.json['NombrePaciente']
    fecha = request.json['Fecha']
    padecimiento = request.json['Padecimiento']
    descripcion = request.json['Descripcion']
    nuevo = Receta(nombrePaciente, fecha, padecimiento, descripcion)
    Recetas.append(nuevo)  

    return ({"Mensaje": "Receta recibida correctamente."})
#==========================================================================================================================
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 3000, debug = True)
