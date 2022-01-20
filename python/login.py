import os
from pickle import FALSE, TRUE
from time import sleep

loginData=''
miLista=[]
misTransacciones=[]

def screenCls():
    _ = os.system('cls')

screenCls()



def menuPrincipal():

    def transacciones():
        screenCls()
        print(misTransacciones)
        sleep(5)
        menuPrincipal
                    
    def cerrarSesion():
        login()
    
    def error():
        print("Opcion Inexistente")
        sleep(2)
        screenCls()
        menuPrincipal()

    def nuevaTransaccion():

       def procesarTransaccion(ctaDes, montoDes):

            def cambioCuenta(cuenta,monto,tipo):
                for x in range(len(miLista)):
                    if miLista[x]==cuenta:
                        original = int(miLista[x+2].lstrip("SALDO INICIAL: $"))
                        if tipo == "deb":
                            final = original - int(monto)
                            miLista[x+2] = "SALDO INICIAL: $"+str(final)
                            print("Saldo final: "+ miLista[x+2].lstrip("SALDO INICIAL: $"))
                        elif tipo == "cred":
                            final = original + int(monto)
                            miLista[x+2] = "SALDO INICIAL: $"+str(final)
                            print("Saldo final: "+ miLista[x+2].lstrip("SALDO INICIAL: $"))
            
            def escribeLibro(origen, destino, monto):
                misTransacciones.append([origen,destino,monto])
        
            cambioCuenta(loginData,montoDes,"deb")
            cambioCuenta(ctaDes,montoDes,"cred")
            escribeLibro(loginData,ctaDes,montoDes)
            print("Transacción completa")
            sleep(3)
            screenCls()
            menuPrincipal()    
       
       def existeCuenta(cuentaDestino):
         if cuentaDestino in miLista and cuentaDestino != loginData:
             return True
         else:
             return False

       def existeSaldo(montoDestino):
            for x in range(len(miLista)):
                if miLista[x]==loginData:
                    valorSaldo = miLista[x+2].lstrip("SALDO INICIAL: $")
                    print("Saldo: "+valorSaldo) 
                    print("A debitar: "+montoDestino)
                    if int(montoDestino) < int(valorSaldo):
                        return True
                    else:
                        print("Saldo Insuficiente")
                        sleep(3)
                        return False
      
       screenCls()
       print("Nueva Transaccion")
       ctaDestino = input("Cuenta Destino: ")
       mtoDestino = input("Monto a Enviar: ")
   
       if not existeCuenta(ctaDestino):
           print("Cuenta Inexistente o mismo origen")
           sleep(3)
           screenCls()
           menuPrincipal()
       if not existeSaldo(mtoDestino):
           sleep(3)
           screenCls()
           menuPrincipal()
       
       if input("Quiere confirmar la Transacción? (S/N)") == 'S':
           procesarTransaccion(ctaDestino,mtoDestino)
   
       sleep(3)
       screenCls()
       menuPrincipal()

    def saldo():
        for x in range(len(miLista)):
            if miLista[x]==loginData:
               print("Saldo: "+miLista[x+2]) 
               sleep(5)
               return
    
        #screenCls()
        #menuPrincipal()


    switch_opciones = {
        "1": saldo,
        "2": transacciones,
        "3": nuevaTransaccion,
        "4": cerrarSesion
    }
    print("User Logged: "+loginData)
    print("Opciones:\n1.Saldo\n2.Transacciones\n3.Nueva Transacción\n4.Cerrar Sesión")
    eleccion = input("Ingrese su opción: ")
    print(eleccion)

    switch_opciones.get(eleccion, error)()


def login():
    print ("ingrese sus credenciales")
    print ("Bienvenido al Banco Central de Palmira")
    myUser = input("USER:\n")
    myPass = input("PASS:\n")
        
    with open ('listado de tarjetas.txt', 'rt') as miArchivo:
        for misLineas in miArchivo:
            miLista.append(misLineas.rstrip('\n'))

    for x in range(len(miLista)):
        if miLista[x]==myUser and miLista[x+1].lstrip("PIN: ")==myPass:
            print("Credenciales Válidas") 
            loginData = miLista[x]
    
    sleep(2)
    screenCls()
    menuPrincipal()

login()


