from guifre import book
from guifre import user
from guifre import university

b1 = book.book(1998, "Guifré", 20, 957, "L'antramat", "terror")
b1.info()
b1.setAny(2008)
b1.setTitol("VIGILA")
b1.info()

b2 = book.book(5486, "Jaime", 55, 23000, "L'història", "fantasia")
b2.info()
b2.setAny(666666)
b2.setTitol("Emancipats")
b2.info()

u1 = user.user("masculí", "Ivan", "Parra", "Estrada", "gilbertu", 45)
u1.info()
u1.setGenere("No-binari")
u1.setEdat(46)
u1.info()

u1 = user.user("femení", "Ivana", "Parri", "Estrado", "manelina", 24)
u1.info()
u1.setGenere("masculí")
u1.setEdat(38)
u1.info()

un1 = university.university(1234, "autonoma", "barroc", "espanya", "barcelona", "08012")
un1.info()
un1.setNom("UPC")
un1.setCodiPostal(66666)
un1.info()

un1 = university.university(569, "UV", "modernista", "espanya", "vic", "27618")
un1.info()
un1.setAnyCreacio(2013)
un1.setNom("Unviversitat de Vic")
un1.info()
