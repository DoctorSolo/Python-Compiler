class Token:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor
        
    def __repr__(self):
        # Esta representação ajuda na hora de imprimir a lista de tokens
        return f"Token({self.tipo.name}, {repr(self.valor)})"