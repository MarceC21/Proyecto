from funciones import * 


op = ""
while op != '3':
    print("\nMenu de Registro/Inicio de Sesion.")
    print("1. Registrarse.")
    print("2. Iniciar Sesion.")
    print("3. Salir")
    op = input(" Eleccion: ")
    if op == '3':
        print("Gracias por usar el Programa!")
    elif op == '1':
        registro()
    elif op == '2':
        inicio()
    else:
        print("ESA OPCION NO ESTA DISPONIBLE!")
        
# def imprimir_clases(csv_file):
#     repetidas = set()
#     with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             repetidas.add(row[0])
#     i = 1
#     for clase in repetidas:
#         print(f"{i}. {clase}")
#         i += 1
    

