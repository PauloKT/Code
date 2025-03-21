class Personagem:
    def __init__(self, nome, classe, ataque, defesa):
        self.classe = classe
        self.ataque = ataque
        self.defesa = defesa
        self.nome = nome
        self.vida = 100

    def atacar(self, outro_personagem):
        dano = self.ataque  - outro_personagem.defesa
        if dano < 0:
            dano = 0
        outro_personagem.vida -= dano
        if outro_personagem.vida < 0:
            outro_personagem.vida = 0
        print(f"{self.nome} atacou {outro_personagem.nome} causando {dano} de dano!")
        print()

    def defender(self):
        self.defesa += 5
        print(f"{self.nome} está se defendendo! Defesa aumentou para {self.defesa}")
        print()