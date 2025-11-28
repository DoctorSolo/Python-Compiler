from src.AnalisadorLexico import AnalisadorLexico


lexer_final = AnalisadorLexico('exemplo_c.c')
lista_de_tokens = lexer_final.analisar()

# Imprimir o resultado
for token in lista_de_tokens:
    print(token)