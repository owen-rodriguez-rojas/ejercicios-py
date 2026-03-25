#Menu Principal del CRUD
from funciones import crear_usuario, mostrar_usuario, editar_usuario, eliminar_usuario



while True:
    print("\n- - - MENU - - -")
    print("1. Crear Usuario\n2. Mostrar Usuario\n3. Editar Usuario\n4. Eliminar Usuario\n5. Salir")
    opc = input("Digite la opción deseada: ")
    while opc.isdigit() == False or int(opc) < 1 or int(opc) > 5:
        print("Valor no valido o fuera de rango, intentar nuevamente.")
        opc = input("Digite la opción deseada: ")
    opc = int(opc)
    
    if opc == 1:
        crear_usuario()
    elif opc == 2:
        mostrar_usuario()
    elif opc == 3:
        editar_usuario()
    elif opc == 4:
        eliminar_usuario()
    elif opc == 5:
        print("Cerrando Menú")
        break        
        
    
