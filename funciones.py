#Funciones que conforman el CRUD

usuarios = []
id_act = 1

def crear_usuario():
        nombre = input("Escribe tu nombre: ").strip()   
        while nombre.isalpha() == False or nombre == "":
            print("Estas ingresando caracteres incorrectos")
            nombre = input("Escribe tu nombre: ").strip()     
        
        apellido = input("Escribe tu apellido paterno: ").strip()
        while apellido.isalpha() == False or apellido == "":
            print("Estas ingresando caracteres incorrectos")
            apellido = input("Escribe tu apellido paterno: ").strip() 
            
        edadT = input("Escribe tu edad: ")
        while edadT.isdigit() == False or int(edadT) > 100 or int(edadT) < 1:
            print("Valor o edad invalida, intentar nuevamente.")
            edadT = input("Escribe tu edad: ")
        
        
        global id_act
        edad = int(edadT)
        datos = {
            "id": id_act,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad
        }
        usuarios.append(datos)
        id_act += 1
        print("Usuario Agregado con Éxito")
    
    
      
def mostrar_usuario():
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        for i in usuarios:
            print(i["id"], "|", i["nombre"], "|", i["apellido"], "|", i["edad"])

def editar_usuario():
    mostrar_usuario()
    id_select = input("Digita el ID del usuario a modificar: ")
    while id_select.isdigit() == False:
        print("ID invalido, intente nuevamente.")
        mostrar_usuario()
        id_select = input("Digita el ID del usuario a modificar: ")
    
    id_select = int(id_select)
    id_encontrado = False
    
    for i in usuarios:
        if i["id"] == id_select:
            id_encontrado = True
            seguir = "s"
            print("Usuario Encontrado con Éxito")
            print(i["id"], "|", i["nombre"], "|", i["apellido"], "|", i["edad"])
            
            while seguir != "n":
                print("1. Nombre\n2. Apellido\n3. Edad") 
            
                modif = input("¿Que campo desea modificar?")
                while modif.isdigit() == False:
                    print("Valor incorrecto, prueba nuevamente.")
                    modif = input("¿Que campo desea modificar?")
                modif = int(modif)
            
                if modif == 1:
                    nombre = input("Nombre Corregido: ").strip()   
                    while nombre.isalpha() == False or nombre == "":
                        print("Estas ingresando caracteres incorrectos")
                        nombre = input("Nombre Corregido: ").strip() 
                
                    i["nombre"] = nombre
                    print("Cambio Exitoso")
                
                elif modif == 2:
                    apellido = input("Apellido Corregido: ").strip()
                    while apellido.isalpha() == False or apellido == "":
                        print("Estas ingresando caracteres incorrectos")
                        apellido = input("Apellido Corregido: ").strip()
                
                    i["apellido"] = apellido
                    print("Cambio Exitoso")
                    
                elif modif == 3:
                    edadT = input("Edad Corregida: ")
                    while edadT.isdigit() == False or int(edadT) > 100 or int(edadT) < 1:
                        print("Valor incorrecto, pruebe nuevamente.")
                        edadT = input("Edad Corregida: ")
                        
                    edadT = int(edadT)
                    i["edad"] = edadT
                    print("Cambio Exitoso")
                   
                else: 
                    print("Numero fuera de rango")
                    continue
            
                validacion_seguir = input("¿Desea Modificar Otro Campo? (s/n)").lower()
                while validacion_seguir not in ("s", "n"):
                    print("Valor invalido")
                    validacion_seguir = input("¿Desea Modificar Otro Campo? (s/n)").lower()
                seguir = validacion_seguir
                    
                
            
            print("\nDatos Actualizados: ")
            print(i["id"], "|", i["nombre"], "|", i["apellido"], "|", i["edad"])
            break
        
    if id_encontrado == False:
            print("ID no encontrado")
        

def eliminar_usuario():
    if len(usuarios) == 0:
        print("\nNo hay usuarios registrados")

    else:
        mostrar_usuario()
        id_select = input("Digita el ID del usuario a eliminar: ")
        while id_select.isdigit() == False:
            print("ID invalido, intente nuevamente.")
            mostrar_usuario()
            id_select = input("Digita el ID del usuario a eliminar: ")
    
        id_select = int(id_select)
        id_encontrado = False
        for i in usuarios:
            if i["id"] == id_select:
                id_encontrado = True
                print(i["id"], "|", i["nombre"], "|", i["apellido"], "|", i["edad"])
                validacion_eliminar = input("¿Esta seguro de eliminar éste usuario? (s/n)").lower()
                while validacion_eliminar not in ("s", "n"):
                    print("Valor invalido")
                    validacion_eliminar = input("¿Esta seguro de eliminar éste usuario? (s/n)").lower()
                if validacion_eliminar == "s":
                    usuarios.remove(i)
                    print("Usuario Eliminado Exitosamente")
                    break
                elif validacion_eliminar == "n":
                    print("Cancelando Eliminacion")
                    break
        if id_encontrado == False:
            print("ID no encontrado")