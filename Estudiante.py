class Estudiante:
    def __init__(self, firstname="Nombre", lastname = "Apellido", mail="correo", phone="telefono",id="cedula"):
        self.firstname = firstname
        self.lastname = lastname
        self.mail = mail
        self.phone = phone
        self.id = id

    def Obtenerinfo(self):
        print("My name is", self.firstname, "My last name is", self.lastname, "My mail is",self.mail, "My phone is", self.phone, "my id is", self.id)








