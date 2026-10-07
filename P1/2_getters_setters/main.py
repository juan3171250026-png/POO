from coches import Coches

coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)

coche1.acelerar()
coche1.acelerar()

print(coche1.getVelocidad())

coche1.setVelocidad(400)

print(coche1.getVelocidad())