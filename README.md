# Repositório de Estudos: Python para Data Science (Alura)

Este repositório contém os notebooks e exercícios desenvolvidos durante a formação **Python para Data Science** da Alura. O objetivo é documentar o progresso e consolidar o conhecimento adquirido, desde os fundamentos da linguagem Python até as bibliotecas e técnicas essenciais para análise de dados.

## 🚀 Tópicos Abordados

A jornada de aprendizado documentada aqui é dividida em várias áreas-chave, cobrindo os pilares da programação Python aplicada a dados.

---

### 🐍 1. Fundamentos Essenciais de Python

Esta seção aborda os conceitos básicos e as estruturas de dados fundamentais da linguagem.

*   **Sintaxe e Variáveis**: Declaração, atribuição e regras de nomenclatura.
*   **Tipos de Dados Primitivos**: `int`, `float`, `str`, `bool`.
*   **Operadores**: Aritméticos, lógicos (`and`, `or`, `not`) e de pertencimento (`in`).
*   **Estruturas de Controle**:
    *   Condicionais com `if`, `elif` e `else`.
    *   Laços de repetição com `for` (usando `range()`) e `while`.
*   **Manipulação de Strings**: Métodos como `.strip()`, `.upper()`, `.lower()`, `.replace()` e formatação com f-strings, `.format()` e `%`.
*   **Entrada de Dados**: Coleta de dados do usuário com `input()` e conversão de tipos (`int()`, `float()`, `str()`).

### 🧱 2. Estruturas de Dados e Manipulação

Aprofundamento nas coleções de dados do Python e em técnicas avançadas de manipulação.

*   **Listas (`list`)**:
    *   Criação, indexação (positiva e negativa) e fatiamento (*slicing*).
    *   Métodos de manipulação: `.append()`, `.extend()`, `.insert()`, `.pop()`, `.remove()`, `.sort()`, `.index()`.
*   **Dicionários (`dict`)**:
    *   Estrutura de chave-valor.
    *   Acesso, modificação e adição de itens.
    *   Iteração com `.keys()`, `.values()` e `.items()`.
*   **Conjuntos (`set`)**:
    *   Coleções **desordenadas de elementos únicos**.
    *   Criação a partir de chaves `{}` ou da função `set()`.
    *   Uso prático para **remoção de duplicatas** em listas.
    *   **Operações de conjuntos**: União (`|`), Interseção (`&`) e verificação de disjunção (`.isdisjoint()`).
    *   **Análise de Performance**: Demonstração da alta eficiência do `set` para testes de pertencimento (`in`) em comparação com `list` e `tuple`.
*   **Estruturas Aninhadas**: Manipulação de listas de listas e listas de tuplas.
*   **Técnicas Avançadas de Criação**:
    *   **List Comprehension**: Sintaxe concisa para criar listas, com e sem condicionais. `[expr for item in lista if cond]`.
    *   **Dict Comprehension**: Criação de dicionários de forma programática. `{chave: valor for item in lista}`.

### ⚙️ 3. Programação Funcional e Boas Práticas

Conceitos que tornam o código mais limpo, reutilizável e robusto.

*   **Funções (`def`)**:
    *   Criação, parâmetros e a instrução `return`.
    *   **Escopo de variáveis**: Entendimento de variáveis locais e globais.
    *   Retorno de múltiplos valores (tuplas).
*   **Boas Práticas em Funções**:
    *   **Type Hinting**: Especificar os tipos de dados dos parâmetros e do retorno (`def func(param: list) -> float:`).
    *   **Docstrings**: Documentar o propósito, os parâmetros e o retorno de uma função.
    *   **Valores Padrão** para parâmetros.
*   **Funções Anônimas (`lambda`)**:
    *   Criação de funções simples e de uma única linha.
    *   Uso em conjunto com a função `map()` para aplicar uma transformação a todos os itens de um iterável.
*   **Funções Embutidas Úteis**: `zip()` para parear elementos de múltiplas listas, `sum()`, `len()`, `round()`.

### 🛡️ 4. Tratamento de Erros e Exceções

Técnicas para criar um código mais seguro e à prova de falhas.

*   **Estrutura `try...except`**: Captura de exceções específicas como `KeyError` e `TypeError` para evitar que o programa pare.
*   **Blocos `else` e `finally`**: Execução de código quando não há exceções (`else`) e execução de código de limpeza que sempre ocorre (`finally`).
*   **Lançando Exceções (`raise`)**: Criação de validações personalizadas e lançamento de erros, como `raise ValueError`, para impor regras de negócio no código.

### 🔬 5. Bibliotecas para Data Science

Esta seção detalha o uso prático das principais bibliotecas de Data Science, que são o foco central deste repositório.

#### 5.1 NumPy: Computação Numérica

Base para a computação científica em Python, explorada nos seguintes tópicos:

*   **Criação de Arrays**: `np.array()`, `np.arange()`, e leitura de arquivos com `np.loadtxt()`.
*   **Atributos de Arrays**: `ndim`, `size`, `shape` para entender as dimensões dos dados.
*   **Manipulação de Arrays**: Transposição (`.T`), indexação e fatiamento (*slicing*) para seleção de dados.
*   **Operações Matemáticas e Estatísticas**: Operações vetorizadas (muito mais rápidas que loops em listas), cálculo de média (`np.mean`), soma (`np.sum`), potência (`np.power`) e norma (`np.linalg.norm`).
*   **Dados Ausentes**: Identificação de valores `NaN` com `np.isnan` e técnicas de interpolação para preenchimento.
*   **Geração de Dados Aleatórios**: Uso de `np.random.seed` para reprodutibilidade e `np.random.randint`/`uniform` para criar dados sintéticos.
*   **Análise de Regressão**: Cálculo manual de coeficientes angular e linear como base para entender modelos preditivos.
*   **Persistência de Dados**: Salvamento de arrays em arquivos (`.csv`) com `np.savetxt`.

#### 5.2 Pandas: Análise e Manipulação de Dados

A principal ferramenta para análise de dados em Python, cobrindo todo o ciclo de vida da manipulação de dados.

*   **I/O (Leitura e Escrita de Dados)**:
    *   **CSV**: `pd.read_csv()` (com parâmetros como `sep`, `usecols`, `nrows`) e `pd.to_csv()`.
    *   **Excel**: `pd.read_excel()` (com `sheet_name`), `pd.ExcelFile()` e `pd.to_excel()`.
    *   **JSON**: Leitura de JSON simples com `pd.read_json()` e normalização de JSON aninhado com `pd.json_normalize()`.
    *   **HTML & XML**: Leitura de tabelas diretamente de páginas web (`pd.read_html()`) e arquivos XML (`pd.read_xml()`).
    *   **Banco de Dados (SQL)**: Interação com um banco de dados (SQLite) usando `SQLAlchemy`, com operações de escrita (`.to_sql()`) e leitura (`pd.read_sql()`, `pd.read_sql_table()`).

*   **Inspeção e Análise Exploratória**:
    *   Visualização inicial com `.head()`, `.tail()`.
    *   Análise estrutural com `.info()`, `.shape`, `.columns`.
    *   Resumo estatístico com `.describe()`.
    *   Contagem de valores únicos com `.unique()` e `.value_counts()`.

*   **Seleção e Filtragem de Dados**:
    *   Seleção de colunas (sintaxe `['coluna']` e `[['col1', 'col2']]`).
    *   **Filtros Condicionais**: Indexação booleana para criar subconjuntos de dados. Ex: `df[df['coluna'] > 100]`.
    *   **Query Language**: Uso do método `.query()` para filtros mais legíveis. Ex: `df.query('Tipo == "Apartamento"')`.
    *   **Cross-Section**: Seleção de dados em múltiplos níveis de índice com `.xs()`.

*   **Limpeza e Tratamento de Dados (Data Cleaning)**:
    *   **Dados Nulos**: Detecção com `.isna()` e `.isnull()`, remoção com `.dropna()`, e preenchimento com `.fillna()` ou valores calculados.
    *   **Dados Duplicados**: Identificação com `.duplicated()` e remoção com `.drop_duplicates()`.
    *   **Outliers**: Detecção visual com **Boxplots** (usando Seaborn) e cálculo de limites com o método **IQR (Intervalo Interquartil)** para identificação e remoção de valores atípicos.
    *   **Conversão de Tipos**: Ajuste de colunas para os tipos corretos (`int`, `float`, `datetime`) usando `.astype()` e `pd.to_numeric()` (com `errors='coerce'`).

*   **Manipulação e Transformação de DataFrames**:
    *   **Criação e Remoção de Colunas**: Criação de colunas a partir de operações aritméticas ou lógicas e remoção com `.drop()`.
    *   **Manipulação de Strings (`.str`)**: Limpeza de texto com `.replace()`, `.strip()`, `.lower()` e tokenização com `.split()`.
    *   **Manipulação de Datas (`.dt`)**: Conversão para o tipo `datetime` e extração de componentes como ano e mês com o acessador `.dt`.
    *   **Reestruturação de Formato**:
        *   **`melt()`**: Transformação de DataFrames do formato "largo" (wide) para "longo" (long).
        *   **`explode()`**: Expansão de listas dentro de células em múltiplas linhas.
    *   **Aplicação de Funções**: Uso de `.apply()` com `lambda` para transformações complexas em colunas.

*   **Agrupamento e Agregação (`groupby`)**:
    *   Agrupamento por uma ou mais colunas para agregação de dados.
    *   Uso de funções como `.sum()`, `.mean()`, `.max()`, `.count()` nos grupos.
    *   **Multi-Index**: Criação e manipulação de índices hierárquicos para análises mais complexas.
    *   Uso de `.idxmax()` para encontrar o índice do maior valor dentro de cada grupo.

*   **Junção de DataFrames**:
    *   Combinação de diferentes fontes de dados em um único DataFrame com `pd.merge()`.

*   **Visualização de Dados com Pandas**:
    *   Criação rápida de gráficos de barras (`.plot(kind='bar')`) e de dispersão (`.plot.scatter()`) para análise visual.
    *   Integração com **Plotly Express** para gráficos interativos.
    *   **Personalização de Gráficos**: Adição de títulos, rótulos e legendas para tornar as visualizações mais claras e informativas.

*   **Automatização de Tarefas**:
    *   Criação de funções para automatizar tarefas repetitivas de limpeza, transformação e análise de dados.

---

## 🛠️ Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/silvaBreno/alura-python-datascience.git
    cd alura-python-datascience
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Linux/macOS
    # ou
    .venv\Scripts\activate      # No Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install notebook pandas numpy matplotlib seaborn sqlalchemy openpyxl
    ```

4.  **Abra no VS Code:**
    - Abra a pasta do projeto no VS Code.
    - Assegure-se de que as extensões **Python** e **Jupyter** da Microsoft estão instaladas.
    - Abra um arquivo `.ipynb` e selecione o interpretador Python do ambiente virtual (`.venv`).
    - Execute as células para explorar os estudos.

## 🔧 Ferramentas de Desenvolvimento

- **nbdime**: Este projeto está configurado para usar `nbdime` para facilitar a visualização de diferenças (`diff`) e a resolução de conflitos (`merge`) em notebooks Jupyter. Para usar, instale e configure no Git:
  ```bash
  pip install nbdime
  nbdime config-git --enable --global
  ```