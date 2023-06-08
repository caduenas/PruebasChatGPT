# Modelo
class ParqueaderoModelo:
    def __init__(self):
        self.espacios = 10
        self.ocupados = 0

    def verificar_disponibilidad(self):
        return self.espacios - self.ocupados

    def ingresar_vehiculo(self):
        if self.ocupados < self.espacios:
            self.ocupados += 1
            return True
        else:
            return False

    def sacar_vehiculo(self):
        if self.ocupados > 0:
            self.ocupados -= 1
            return True
        else:
            return False


# Vista
class ParqueaderoVista:
    def mostrar_menu(self):
        print("== PARQUEADERO ==")
        print("1. Verificar disponibilidad")
        print("2. Ingresar vehículo")
        print("3. Sacar vehículo")
        print("4. Salir")

    def obtener_opcion(self):
        return int(input("Ingrese una opción: "))

    def mostrar_disponibilidad(self, disponibilidad):
        print("Espacios disponibles:", disponibilidad)

    def mostrar_resultado_ingreso(self, exito):
        if exito:
            print("Ingreso exitoso.")
        else:
            print("El parqueadero está lleno. No se puede ingresar más vehículos.")

    def mostrar_resultado_salida(self, exito):
        if exito:
            print("Salida exitosa.")
        else:
            print("El parqueadero está vacío. No hay vehículos para sacar.")


# Controlador
class ParqueaderoControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def iniciar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.obtener_opcion()

            if opcion == 1:
                disponibilidad = self.modelo.verificar_disponibilidad()
                self.vista.mostrar_disponibilidad(disponibilidad)
            elif opcion == 2:
                exito = self.modelo.ingresar_vehiculo()
                self.vista.mostrar_resultado_ingreso(exito)
            elif opcion == 3:
                exito = self.modelo.sacar_vehiculo()
                self.vista.mostrar_resultado_salida(exito)
            elif opcion == 4:
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.")


# Programa principal
modelo = ParqueaderoModelo()
vista = ParqueaderoVista()
controlador = ParqueaderoControlador(modelo, vista)
controlador.iniciar()
