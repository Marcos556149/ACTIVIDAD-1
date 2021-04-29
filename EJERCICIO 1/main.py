import csv
from ClaseEmail import Email
def test():
    testPrueba=Email()
    correo1= 'yuri1120@gmail.com'  #Email valido
    correo2= 'bellamy789'          #Email no valido
    print("Verifiquemos si correo1 es valido")
    testPrueba.crearCuenta(correo1)
    print("Verifiquemos si correo2 es valido")
    testPrueba.crearCuenta(correo2)
if __name__ == '__main__':
    test()
    nom=input('ingrese su nombre: ')
    print("procederemos a ingresar su direccion de e-mail")
    id=input('ingrese la id de su cuenta: ')
    dom=input('ingrese el dominio: ')
    tipo=input('ingrese el tipo de dominio: ')
    con=input('ingrese la contrasena: ')
    mail=Email(id,dom,tipo,con)
    print("Estimado {} te enviaremos tus mensajes a la direccion {}".format(nom,mail.retornaEmail()))
    mail.mod_contrasena()
    dir=input('ingrese direccion de correo para crear objeto: ')
    mail1=Email()
    mail1=mail.crearCuenta(dir)
    cont = 0
    archivo = open('Correo.csv')
    reader = csv.reader(archivo,delimiter=',')
    dominio=input('ingrese dominio: ')
    for fila in reader:
        if fila[1] == dominio:
            cont += 1
    print("la cantidad de personas con el dominio ingresado es: ",cont)
    archivo.close()
