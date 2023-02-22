class vehicle:
    def __init__(self, color, ruedas, motor, año, marca, kilometraje):
        self.color = color
        self.ruedas = ruedas
        self.motor = motor
        self.año = año
        self.marca = marca
        self.kilometraje = kilometraje
    def getColor(self):
        return self.ruedas
    def setColor(self, color):
        self.color = color
    def getRuedas(self):
        return self.ruedas
    def setRuedas(self, ruedas):
        self.ruedas = ruedas
    def getMotor(self):
        return self.motor
    def setMotor(self, motor):
        self.motor = motor
    def getAño(self):
        return self.año
    def setAño(self, año):
        self.año = año
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca
    def getKilometraje(self):
        return self.kilometraje
    def setKilometraje(self, kilometraje):
        self.kilometraje = kilometraje
    def parts(self):
        print("Es de color : " + self.color)
        print("Tiene : " + self.ruedas)
        print("Tiene : " + self.motor)
        print("Es del año : " + self.año)
        print("Es de la marca : " + self.marca)
        print("Su kilometraje es : " + self.kilometraje + "\n")
