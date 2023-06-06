from dataclasses import dataclass

@dataclass
class Personagem:
    nome: str
    golpe: str
    vida: int = 100

    def diz_oi(self):
        print(f'Oi, eu sou o {self.nome}')

    def ataca(self, oponente):
        print(f'{self.nome} ataca {oponente.nome} com um {self.golpe}')
        oponente.tirar_vida(40)

    def tirar_vida(self, vida):
        self.vida -= vida
        if self.vida <= 0:
            print(f'morreu, foi jogar no vasco.')        


luffy = Personagem('Luffy', 'Elephant Gun')
luffy.diz_oi()
kaido = Personagem('Kaido buxa', 'Haime Hakke')
luffy.ataca(kaido)
luffy.ataca(kaido)
luffy.ataca(kaido)
luffy.ataca(kaido)
luffy.ataca(kaido)
luffy.ataca(kaido)

