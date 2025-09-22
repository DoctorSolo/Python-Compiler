from AnalisadorLexico import AnalisadorLexico

lexer_final = AnalisadorLexico('codigo.py')
lista_de_tokens = lexer_final.analisar()

# Imprimir o resultado
for token in lista_de_tokens:
    print(token)