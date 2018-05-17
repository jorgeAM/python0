class Persona:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def miDatos(self):
        print('mi nombre es '+self.nombre+' '+self.apellidos)


jorge = Persona('71466210', 'Jorge', 'Alfaro')
jorge.miDatos()
