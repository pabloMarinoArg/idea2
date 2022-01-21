import os
from pickle import FALSE, TRUE
from time import sleep

loginData=[]
miLista=[]
misTransacciones=[]

def screenCls():
    _ = os.system('cls')

screenCls()



def menuPrincipal():

    def transacciones():
        screenCls()
        print(misTransacciones)
        print("Cuenta Origen\t\t\tCuenta Destino\t\t\tMonto")
        for line in misTransacciones:
            print(line[0]+"\t\t"+line[1]+"\t\t"+line[2])
        sleep(5)
        return
                    
    def cerrarSesion():
        loginData.clear()
        return
    
    def error():
        print("Opcion Inexistente")
        sleep(2)
        return

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
        
            cambioCuenta(loginData[0],montoDes,"deb")
            cambioCuenta(ctaDes,montoDes,"cred")
            escribeLibro(loginData[0],ctaDes,montoDes)
            print("Transacción completa")
            sleep(3)
            return    
       
       def existeCuenta(cuentaDestino):
         if cuentaDestino in miLista and cuentaDestino != loginData[0]:
             return True
         else:
             return False

       def existeSaldo(montoDestino):
            for x in range(len(miLista)):
                if miLista[x]==loginData[0]:
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
           return
       if not existeSaldo(mtoDestino):
           sleep(3)
           return
       
       if input("Quiere confirmar la Transacción? (S/N)") == 'S':
           procesarTransaccion(ctaDestino,mtoDestino)
   
       sleep(3)
       return

    def saldo():
        for x in range(len(miLista)):
            if miLista[x]==loginData[0]:
               print("Saldo: "+miLista[x+2]) 
               sleep(5)
        return
    
    def printMenu():
        print("User Logged: "+loginData[0])
        print("Opciones:\n1.Saldo\n2.Transacciones\n3.Nueva Transacción\n4.Cerrar Sesión")
        
    switch_opciones = {
        "1": saldo,
        "2": transacciones,
        "3": nuevaTransaccion,
        "4": cerrarSesion
    }

    while(len(loginData)>0):
        screenCls()
        printMenu()
        eleccion = input("Ingrese su opción: ")
        switch_opciones.get(eleccion, error)()
    
    return


def login():

    def printLogin():
        print ("ingrese sus credenciales")
        print ("Bienvenido al Banco Central de Palmira")
    
    with open ('listado de tarjetas.txt', 'rt') as miArchivo:
       for misLineas in miArchivo:
           miLista.append(misLineas.rstrip('\n'))

    while len(loginData)==0:
        screenCls()
        printLogin()
        myUser = input("USER:\n")
        myPass = input("PASS:\n")    
    
        for x in range(len(miLista)):
            if miLista[x]==myUser and miLista[x+1].lstrip("PIN: ")==myPass:
                print("Credenciales Válidas") 
                loginData.append(miLista[x])
                print(loginData[0])
    
        if len(loginData)>0:
            sleep(5)
            screenCls()
            menuPrincipal()
    
login()


