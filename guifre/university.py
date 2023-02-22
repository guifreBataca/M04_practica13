class university():
    def __init__(self, anyCreacio, nom, estil, pais, ciutat, codiPostal):
        self.anyCreacio = anyCreacio
        self.nom = nom
        self.estil = estil
        self.pais = pais
        self.ciutat = ciutat
        self.codiPostal = codiPostal

    def setAnyCreacio(self, anyCreacioNou):
        self.anyCreacio = anyCreacioNou

    def setNom(self, nomNou):
        self.nom = nomNou

    def setEstil(self, estilNou):
        self.estil = estilNou

    def setPais(self, paisNou):
        self.pais = paisNou
    def setCiutat(self, ciutatNou):
        self.ciutat = ciutatNou

    def setCodiPostal(self, codiPostalNou):
        self.codiPostal = codiPostalNou

    def getAnyCreacio(self):
        return self.anyCreacio

    def getNom(self):
        return self.nom

    def getEstil(self):
        return self.estil

    def getPais(self):
        return self.pais

    def getCiutat(self):
        return self.ciutat

    def getCodiPostal(self):
        return self.codiPostal

    def info(self):
        print("L'any de creació de la universistat és: " + str(self.anyCreacio))
        print("El nom de la universistat és: " + self.nom)
        print("L'estil de la universistat és: " + self.estil)
        print("El país de la universistat és: " + self.pais)
        print("La ciutat de la universistat és: " + self.ciutat)
        print("El codi postal de la universistat és: " + str(self.codiPostal) + "\n")
