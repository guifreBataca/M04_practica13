class animal:
    def __init__(self, patas, ojos, tipo, nombre, familia, habitad):
        self.patas = patas
        self.ojos = ojos
        self.tipo = tipo
        self.nombre = nombre
        self.familia = familia
        self.habitad = habitad
    def getPatas(self):
        return self.patas
    def setPatas(self, patas):
        self.patas = patas
    def getOjos(self):
        return self.ojos
    def setOjos(self, ojos):
        self.ojos = ojos
    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.corazon = tipo
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getFamilia(self):
        return self.familia
    def setFamilia(self, familia):
        self.familia = familia
    def getHabitad(self):
        return self.habitad
    def setHabitad(self, habitad):
        self.habitad = habitad
    def salutacio(self):
        print("Es un animal " + self.nombre)
        print("Es un animal de tipo " + self.tipo)
        print("Es de la familia" + self.familia)
        print("Su habitad es: " + self.habitad)
        print("Tiene : " + self.patas)
        print("Tiene : " + self.ojos + "\n")


