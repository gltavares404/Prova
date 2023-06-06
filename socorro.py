class Saida:
    def enviar(self, texto):
        print(texto)

class Arquivo(Saida):

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def enviar(self, texto):
        with open(self.arquivo, 'a+') as arquivo:
            arquivo.write(texto + "\n")

saida = Saida()
saida.enviar("Hello world")
saida = Arquivo("teste.txt")
saida.enviar("Hello world")
saidas = [ Saida(), Arquivo('a.txt'), Arquivo('b.txt'), Saida()]
for saida in saidas:
    saida.enviar('Olá')
