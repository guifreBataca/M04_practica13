class book():
    def __init__(self, any, autor, segle, nPagines, titol, genere):
        self.any = any
        self.autor = autor
        self.segle = segle
        self.nPagines = nPagines
        self.titol = titol
        self.genere = genere

    def setAny(self, anyNou):
        self.any = anyNou

    def setAutor(self, autorNou):
        self.autor = autorNou

    def setSelge(self, selgeNou):
        self.segle = selgeNou

    def setNPagines(self, nPaginesNou):
        self.nPagines = nPaginesNou
    def setTitol(self, titolNou):
        self.titol = titolNou

    def setgenere(self, genereNou):
        self.genere = genereNou

    def getAny(self):
        return self.any

    def getAutor(self):
        return self.autor

    def getSelge(self):
        return self.segle

    def getNPagines(self):
        return self.nPagines

    def getTitol(self):
        return self.titol

    def getGenere(self):
        return self.genere

    def info(self):
        print("L'any del llibre és: " + str(self.any))
        print("L'autor del llibre és: " + str(self.autor))
        print("El segle del llibre és: " + str(self.segle))
        print("El nombre de pàgines del llibre és: " + str(self.nPagines))
        print("El títol del llibre és: " + str(self.titol))
        print("El gènere del llibre és: " + str(self.genere) + "\n")