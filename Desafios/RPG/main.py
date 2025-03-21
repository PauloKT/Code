from Class.personagem import Personagem
from Function.função import exibir_status, batalha

p1 = Personagem("Heitor", "Guerrero", 20, 10)
p2 = Personagem("Gotica", "Mago", 25, 5)

exibir_status(p1)
exibir_status(p2)

batalha(p1, p2)