from guifre import book
from guifre import user
from guifre import university
from Sebastian import animal
from Sebastian import vehicle
from Sebastian import school

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

a1 = animal.animal("Gatos", "adiestrado", "felino", "domestico", "4", "2")
a1.salutacio()
a1.setNombre("Perros")
a1.salutacio()
a1 = animal.animal("leon", "salvaje", "felino", "selva", "4", "2")
a1.salutacio()
a1.setNombre("Tigre")
a1.salutacio()

v1 = vehicle.vehicle("rojo" , "4", "gasolina", "2000", "NISSAN", "0")
v1.parts()
v1.setMotor("gas")
v1.parts()
v1 = vehicle.vehicle("azul", "4", "gas", "2010", "SUZUKI", "1000")
v1.parts()
v1.setMotor("gasolina")
v1.parts()

s1 = school.school("10", "20", "200", "5000", "5000", "10")
s1.info()
s1.setAulas("20")
s1.info()
s1 = school.school("7","10","100","2000","2000","5")
s1.info()
s1.setBaños("7")
s1.info()