# Classes para os Nós da Árvore Sintática Abstrata (AST - Abstract Syntax Tree)

class NoAST:
    pass

class NoAtribuicao(NoAST):
    def __init__(self, var, valor):
        self.var = var
        self.valor = valor

class NoVariavel(NoAST):
    def __init__(self, token):
        self.token = token
        self.valor = token.valor

class NoNumero(NoAST):
    def __init__(self, token):
        self.token = token
        self.valor = token.valor

class NoOperacaoBinaria(NoAST):
    def __init__(self, esquerda, op, direita):
        self.esquerda = esquerda
        self.op = op
        self.direita = direita

class NoBloco(NoAST):
    def __init__(self):
        self.declaracoes = []

class NoIf(NoAST):
    def __init__(self, condicao, corpo_if, corpo_else=None):
        self.condicao = condicao
        self.corpo_if = corpo_if
        self.corpo_else = corpo_else # Simplificado sem elif por enquanto

class NoWhile(NoAST):
    def __init__(self, condicao, corpo):
        self.condicao = condicao
        self.corpo = corpo