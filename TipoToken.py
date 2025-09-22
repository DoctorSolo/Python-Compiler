# Mão na massa! Vamos abrir o editor de código.

import enum

class TipoToken(enum.Enum):
    # Palavras-chave
    IF = "IF"
    ELIF = "ELIF"
    ELSE = "ELSE"
    WHILE = "WHILE"
    TRUE = "TRUE"
    FALSE = "FALSE"
    
    # Identificadores e Literais
    IDENTIFICADOR = "IDENTIFICADOR"
    NUMERO_INTEIRO = "NUMERO_INTEIRO"
    STRING = "STRING"
    
    # Operadores
    ATRIBUICAO = "ATRIBUICAO"       # =
    IGUALDADE = "IGUALDADE"         # ==
    MAIOR = "MAIOR"                 # >
    MENOR = "MENOR"                 # <
    MAIOR_IGUAL = "MAIOR_IGUAL"     # >=
    MENOR_IGUAL = "MENOR_IGUAL"     # <=
    SOMA = "SOMA"                   # +
    SUBTRACAO = "SUBTRACAO"         # -
    MULTIPLICACAO = "MULTIPLICACAO" # *
    DIVISAO = "DIVISAO"             # /
    
    # Pontuação e Delimitadores
    DOIS_PONTOS = "DOIS_PONTOS"    # :
    
    # Fim do arquivo
    EOF = "EOF" # End of File