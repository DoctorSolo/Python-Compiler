# Mão na massa!
# (Cole o código do Analisador Léxico da aula anterior aqui em cima)

class TabelaDeSimbolos:
    def __init__(self):
        self.simbolos = {}

    def definir(self, nome):
        print(f"Definindo variável: {nome}")
        self.simbolos[nome] = None # Por enquanto, só guardamos o nome

    def obter(self, nome):
        print(f"Acessando variável: {nome}")
        if nome not in self.simbolos:
            raise NameError(f"Erro Semântico: Variável '{nome}' não definida.")
        return self.simbolos.get(nome)

    def __repr__(self):
        return f"TabelaDeSimbolos({self.simbolos})"