# Compilador em Python

Este é um projeto de um **compilador educacional** desenvolvido em Python para a disciplina de **Compiladores**, com o objetivo de demonstrar os principais conceitos da construção de compiladores: análise léxica, sintática, semântica, estrutura de símbolos, tipos de tokens, entre outros.

## 📁 Estrutura do Projeto

COMPILADOR/
├── AnalizadorLexico.py          # Responsável pelo scanner (analisador léxico)
├── AnalizadorSintatico.py       # Responsável pelo parser (analisador sintático)
├── TabelaDeSimbolos.py          # Estrutura para armazenar os identificadores e seus atributos
├── TipoToken.py                 # Enumeração ou classe com os tipos de tokens definidos
├── Token.py                     # Definição da estrutura dos tokens
├── Nos.py                       # Definições das estruturas de nós da árvore sintática
├── compilador.py                # Arquivo principal de orquestração do compilador
├── codigo.py                    # Código-fonte de entrada a ser analisado (exemplo)
└── **pycache**/                 # Cache do Python (ignorado)

## ⚙️ Como executar

### 1. Clone o repositório

git clone https://github.com/voidmmn/compilador.git
cd compilador

### 2. Execute o arquivo principal

bash python compilador.py

Certifique-se de ter o Python 3 instalado. Recomendamos usar um ambiente virtual.

## 🧠 Funcionalidades

* ✅ Analisador léxico com reconhecimento de tokens
* ✅ Analisador sintático com geração de árvore
* ✅ Tabela de símbolos
* ✅ Sistema modular para fácil expansão
* ✅ Exemplo de código de entrada (`codigo.py`)

## 👨‍🏫 Sobre o projeto

Este projeto foi desenvolvido como parte da disciplina **Compiladores**, com fins **educacionais**. O código está organizado para facilitar a compreensão dos diferentes componentes que compõem um compilador.

## 📄 Licença

Este projeto é de uso livre para fins acadêmicos. Para fins comerciais, consulte o autor.

## ✉️ Contato

Prof. Milton Miranda Neto
GitHub: [@voidmmn](https://github.com/voidmmn)
Uberlândia - MG