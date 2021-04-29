class Email:
    __idCuenta= ''
    __dominio= ''
    __tipo_dominio= ''
    __contrasena= ''
    def __init__(self,id=None,dom=None,tipo=None,con=None):
        self.__idCuenta=id
        self.__dominio=dom
        self.__tipo_dominio=tipo
        self.__contrasena=con
    def retornaEmail(self):
        return self.__idCuenta + "@" + self.__dominio + "." + self.__tipo_dominio
    def getDominio(self):
        return self.__dominio
    def mod_contrasena(self):
        actual=input('Ingrese contraseña actual: ')
        while actual != self.__contrasena:
            actual=input('contraseña incorrecta, vuelva a ingresar contraseña actual: ')
        self.__contrasena=input('ingrese nueva contraseña: ')
        print (self.__contrasena)
    def crearCuenta(self,dir):
        if (dir.find("@") != -1) & (dir.find(".") != -1):
            idC= dir[:dir.find("@")]
            domin=dir[dir.find("@") + 1: dir.find(".")]
            tipoDom=dir[dir.find(".") + 1:]
            passw=input('ingrese contraseña para el nuevo correo: ')
            nuevoEmail= Email(idC,domin,tipoDom,passw)
            print("El objeto de clase Email fue creado correctamente")
            return nuevoEmail
        else:
            print("ERROR: el formato del mail es invalido")
