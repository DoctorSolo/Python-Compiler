from src.AnalisadorLexico import AnalisadorLexico
from src.AnalisadorSintatico import AnalisadorSintatico


lexer_final = AnalisadorLexico('exemplo_c.c')
lista_de_tokens = lexer_final.analisar()

# Imprimir o resultado
for token in lista_de_tokens:
    print(token)

# Agora, realizar a análise sintática
AnalisadorSintatico_final = AnalisadorSintatico(lista_de_tokens)
arvore_sintatica = AnalisadorSintatico_final.analisar()
print(arvore_sintatica)