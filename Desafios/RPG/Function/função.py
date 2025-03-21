import time

def exibir_status(personagem):
    print(f"Nome: {personagem.nome} | Classe: {personagem.classe} | Vida: {personagem.vida} | Ataque: {personagem.ataque} | Defesa: {personagem.defesa}")

def batalha(p1, p2):
    while p1.vida > 0 and p2.vida > 0:
        p1.atacar(p2)
        exibir_status(p2)

        if p2.vida <= 0:
            print(f"{p2.nome} foi derrotado! {p1.nome} venceu!")
            break

        p2.defender()
        p2.atacar(p1)
        exibir_status(p1)

        if p1.vida <= 0:
            print(f"{p1.nome} foi derrotado! {p2.nome} venceu!")
            break

        print("-" * 40)
        time.sleep(2)