from src.TipoToken import TipoToken
from src.Nos import NoAST, NoBloco, NoAtribuicao, NoVariavel, NoNumero, NoOperacaoBinaria, NoIf, NoWhile
from src.TabelaDeSimbolos import TabelaDeSimbolos  
from src.Token import Token


class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicao = 0
        self.tabela_de_simbolos = TabelaDeSimbolos()

    def _token_atual(self):
        if self.posicao < len(self.tokens):
            return self.tokens[self.posicao]
        return self.tokens[-1] # Retorna EOF

    def _avancar(self):
        self.posicao += 1

    def _consumir(self, tipo_esperado):
        """Verifica o tipo do token atual, o consome e avança."""
        token = self._token_atual()
        if token.tipo == tipo_esperado:
            self._avancar()
            return token
        else:
            raise SyntaxError(f"Erro de Sintaxe: Esperado {tipo_esperado}, mas encontrado {token.tipo}")

    def analisar(self):
        """Ponto de entrada para iniciar a análise."""
        arvore = self._parse_bloco()
        if self._token_atual().tipo != TipoToken.EOF:
            raise SyntaxError("Erro de Sintaxe: Código extra encontrado após o fim do programa.")
        return arvore

    # A seguir, as funções para cada regra da gramática

    def _parse_bloco(self):
        """Um bloco é uma sequência de declarações dentro de {}."""
        self._consumir(TipoToken.CHAVE_ABERTA)
        bloco = NoBloco()
        
        while self._token_atual().tipo != TipoToken.CHAVE_FECHADA and self._token_atual().tipo != TipoToken.EOF:
            bloco.declaracoes.append(self._parse_declaracao())
        
        self._consumir(TipoToken.CHAVE_FECHADA)
        return bloco

    def _parse_declaracao(self):
        """Decide qual tipo de declaração estamos vendo."""
        token_tipo = self._token_atual().tipo
        
        if token_tipo == TipoToken.IDENTIFICADOR:
            return self._parse_atribuicao()
        elif token_tipo == TipoToken.IF:
            return self._parse_if()
        elif token_tipo == TipoToken.WHILE:
            return self._parse_while()
        elif token_tipo == TipoToken.FOR:
            return self._parse_for()
        elif token_tipo == TipoToken.RETURN:
            return self._parse_return()
        elif token_tipo in [TipoToken.INT, TipoToken.FLOAT, TipoToken.VOID]:
            return self._parse_declaracao_variavel()
        else:
            raise SyntaxError(f"Declaração inválida iniciada com {token_tipo}")

    def _parse_atribuicao(self):
        """Parseia: IDENTIFICADOR = expressao;"""
        var_token = self._consumir(TipoToken.IDENTIFICADOR)
        self.tabela_de_simbolos.definir(var_token.valor) # Adiciona à tabela
        
        self._consumir(TipoToken.ATRIBUICAO)
        
        valor = self._parse_expressao()
        
        self._consumir(TipoToken.PONTO_VIRGULA)  # Requer ; no final
        return NoAtribuicao(NoVariavel(var_token), valor)

    # Expression parsing (supports binary ops and parentheses)
    def _parse_expressao(self):
        return self._parse_comparacao()

    def _parse_comparacao(self):
        node = self._parse_termo()
        comparadores = [TipoToken.IGUALDADE, TipoToken.DIFERENCA, TipoToken.MAIOR, TipoToken.MAIOR_IGUAL, TipoToken.MENOR, TipoToken.MENOR_IGUAL]
        while self._token_atual().tipo in comparadores:
            op = self._consumir(self._token_atual().tipo)
            right = self._parse_termo()
            node = NoOperacaoBinaria(node, op, right)
        return node

    def _parse_termo(self):
        node = self._parse_fator()
        while self._token_atual().tipo in (TipoToken.SOMA, TipoToken.SUBTRACAO):
            op = self._consumir(self._token_atual().tipo)
            right = self._parse_fator()
            node = NoOperacaoBinaria(node, op, right)
        return node

    def _parse_fator(self):
        node = self._parse_unario()
        while self._token_atual().tipo in (TipoToken.MULTIPLICACAO, TipoToken.DIVISAO, TipoToken.MODULO):
            op = self._consumir(self._token_atual().tipo)
            right = self._parse_unario()
            node = NoOperacaoBinaria(node, op, right)
        return node

    def _parse_unario(self):
        # Handle unary + and -
        if self._token_atual().tipo == TipoToken.SOMA:
            self._consumir(TipoToken.SOMA)
            return self._parse_unario()
        if self._token_atual().tipo == TipoToken.SUBTRACAO:
            op = self._consumir(TipoToken.SUBTRACAO)
            right = self._parse_unario()
            zero_token = Token(TipoToken.NUMERO_INTEIRO, 0)
            return NoOperacaoBinaria(NoNumero(zero_token), op, right)
        return self._parse_primario()

    def _parse_primario(self):
        token = self._token_atual()
        if token.tipo == TipoToken.NUMERO_INTEIRO:
            self._consumir(TipoToken.NUMERO_INTEIRO)
            return NoNumero(token)
        elif token.tipo == TipoToken.IDENTIFICADOR:
            self._consumir(TipoToken.IDENTIFICADOR)
            self.tabela_de_simbolos.obter(token.valor) # Verifica se existe
            return NoVariavel(token)
        elif token.tipo == TipoToken.PARENTESE_ABERTA:
            self._consumir(TipoToken.PARENTESE_ABERTA)
            expr = self._parse_expressao()
            self._consumir(TipoToken.PARENTESE_FECHADA)
            return expr
        else:
            raise SyntaxError(f"Expressão inválida. Esperado NÚMERO, IDENTIFICADOR ou '(', mas encontrado {token.tipo}")

    def _parse_if(self):
        """Parseia: if (condicao) { corpo } [else { corpo }]"""
        self._consumir(TipoToken.IF)
        self._consumir(TipoToken.PARENTESE_ABERTA)
        condicao = self._parse_expressao()
        self._consumir(TipoToken.PARENTESE_FECHADA)
        
        corpo_if = self._parse_bloco()
        corpo_else = None
        
        if self._token_atual().tipo == TipoToken.ELSE:
            self._consumir(TipoToken.ELSE)
            corpo_else = self._parse_bloco()
        
        return NoIf(condicao, corpo_if, corpo_else)

    def _parse_while(self):
        """Parseia: while (condicao) { corpo }"""
        self._consumir(TipoToken.WHILE)
        self._consumir(TipoToken.PARENTESE_ABERTA)
        condicao = self._parse_expressao()
        self._consumir(TipoToken.PARENTESE_FECHADA)
        
        corpo = self._parse_bloco()
        return NoWhile(condicao, corpo)

    def _parse_for(self):
        """Placeholder: for (init; condicao; incremento) { corpo }"""
        self._consumir(TipoToken.FOR)
        self._consumir(TipoToken.PARENTESE_ABERTA)
        # Simplificado - implementação completa do for fica para depois
        self._consumir(TipoToken.PARENTESE_FECHADA)
        corpo = self._parse_bloco()
        return corpo

    def _parse_return(self):
        """Parseia: return expressao;"""
        self._consumir(TipoToken.RETURN)
        valor = self._parse_expressao()
        self._consumir(TipoToken.PONTO_VIRGULA)
        return valor

    def _parse_declaracao_variavel(self):
        """Parseia: int x = 5; ou float y = 3.14;"""
        tipo_token = self._token_atual()
        self._consumir(tipo_token.tipo)  # int, float, etc
        
        var_token = self._consumir(TipoToken.IDENTIFICADOR)
        self.tabela_de_simbolos.definir(var_token.valor)
        
        if self._token_atual().tipo == TipoToken.ATRIBUICAO:
            self._consumir(TipoToken.ATRIBUICAO)
            valor = self._parse_expressao()
            self._consumir(TipoToken.PONTO_VIRGULA)
            return NoAtribuicao(NoVariavel(var_token), valor)
        else:
            self._consumir(TipoToken.PONTO_VIRGULA)
            return NoVariavel(var_token)