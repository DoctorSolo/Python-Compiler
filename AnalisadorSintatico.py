from TipoToken import TipoToken
from Nos import NoAST, NoBloco, NoAtribuicao, NoVariavel, NoNumero, NoOperacaoBinaria, NoIf, NoWhile
from TabelaDeSimbolos import TabelaDeSimbolos   


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
        """Um bloco é uma sequência de declarações."""
        bloco = NoBloco()
        # Simplificação: Nosso bloco não tem delimitadores como {}
        # Apenas parseamos uma declaração por enquanto
        bloco.declaracoes.append(self._parse_declaracao())
        return bloco

    def _parse_declaracao(self):
        """Decide qual tipo de declaração estamos vendo."""
        token_tipo = self._token_atual().tipo
        
        if token_tipo == TipoToken.IDENTIFICADOR:
            return self._parse_atribuicao()
        # Adicionar aqui a lógica para IF, WHILE, etc.
        else:
            raise SyntaxError(f"Declaração inválida iniciada com {token_tipo}")

    def _parse_atribuicao(self):
        """Parseia: IDENTIFICADOR = expressao"""
        var_token = self._consumir(TipoToken.IDENTIFICADOR)
        self.tabela_de_simbolos.definir(var_token.valor) # Adiciona à tabela
        
        self._consumir(TipoToken.ATRIBUICAO)
        
        valor = self._parse_expressao()
        
        return NoAtribuicao(NoVariavel(var_token), valor)

    def _parse_expressao(self):
        """Por enquanto, uma expressão é apenas um número ou uma variável."""
        token = self._token_atual()
        if token.tipo == TipoToken.NUMERO_INTEIRO:
            self._consumir(TipoToken.NUMERO_INTEIRO)
            return NoNumero(token)
        elif token.tipo == TipoToken.IDENTIFICADOR:
            self._consumir(TipoToken.IDENTIFICADOR)
            self.tabela_de_simbolos.obter(token.valor) # Verifica se existe
            return NoVariavel(token)
        else:
            raise SyntaxError(f"Expressão inválida. Esperado NÚMERO ou IDENTIFICADOR, mas encontrado {token.tipo}")