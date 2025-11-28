# Mão na massa! Vamos abrir o editor de código.

import enum

class TipoToken(enum.Enum):
    # Palavras-chave
    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"
    FOR = "FOR"
    INT = "INT"
    FLOAT = "FLOAT"
    VOID = "VOID"
    RETURN = "RETURN"
    
    # Identificadores e Literais
    IDENTIFICADOR = "IDENTIFICADOR"
    NUMERO_INTEIRO = "NUMERO_INTEIRO"
    NUMERO_FLOAT = "NUMERO_FLOAT"
    STRING = "STRING"
    
    # Operadores
    ATRIBUICAO = "ATRIBUICAO"       # =
    IGUALDADE = "IGUALDADE"         # ==
    DIFERENCA = "DIFERENCA"         # !=
    MAIOR = "MAIOR"                 # >
    MENOR = "MENOR"                 # <
    MAIOR_IGUAL = "MAIOR_IGUAL"     # >=
    MENOR_IGUAL = "MENOR_IGUAL"     # <=
    SOMA = "SOMA"                   # +
    SUBTRACAO = "SUBTRACAO"         # -
    MULTIPLICACAO = "MULTIPLICACAO" # *
    DIVISAO = "DIVISAO"             # /
    MODULO = "MODULO"               # %
    E_LOGICO = "E_LOGICO"           # &&
    OU_LOGICO = "OU_LOGICO"         # ||
    NEGACAO = "NEGACAO"             # !
    
    # Pontuação e Delimitadores
    PONTO_VIRGULA = "PONTO_VIRGULA" # ;
    CHAVE_ABERTA = "CHAVE_ABERTA"   # {
    CHAVE_FECHADA = "CHAVE_FECHADA" # }
    PARENTESE_ABERTA = "PARENTESE_ABERTA"     # (
    PARENTESE_FECHADA = "PARENTESE_FECHADA"   # )
    COLCHETE_ABERTO = "COLCHETE_ABERTO"       # [
    COLCHETE_FECHADO = "COLCHETE_FECHADO"     # ]
    VIRGULA = "VIRGULA"             # ,
    
    # Fim do arquivo
    EOF = "EOF" # End of File