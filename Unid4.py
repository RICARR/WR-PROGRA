"""EN ESTE PROGRAMA SE  MODELARA LA FUNCIÓN DE UN  GERENTE CON BASE EN
 EL PARADIGMA ORIENTADO A OBJETOS"""


class Persona:
    def __init__(self, nombre, estatura, ):
        self.nombre = nombre
        self.estatura = estatura


    def carac(self):
        print("El nombre de la persona es:", self.nombre)
        print("La estatura de la persona es de:", self.estatura)


class Empresa:
    def __init__(self, NomEmpresa):
        self.NomEmpresa = NomEmpresa

    def carac(self):
        print("El nombre de la empresa es:",self.NomEmpresa)



class Gerente(Persona,Empresa):
    def __init__(self,nombre,estatura):
        super().__init__(nombre,estatura)



