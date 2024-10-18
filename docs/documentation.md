# Documentação do Projeto de Otimização de Carteira

## Índice
1. [Introdução](#introdução)
2. [Estrutura do Código](#estrutura-do-código)
3. [Classes e Funções Principais](#classes-e-funções-principais)
   - [PortfolioOptimizer](#portfoliooptimizer)
   - [Funções de Visualização](#funções-de-visualização)
   - [Gerenciamento de Tickers](#gerenciamento-de-tickers)
4. [Processo de Otimização](#processo-de-otimização)
5. [Gráficos Gerados](#gráficos-gerados)

## Introdução
Este projeto visa desenvolver um algoritmo que otimize a alocação de ativos em uma carteira de investimentos, maximizando o retorno esperado enquanto respeita um limite de risco definido. O algoritmo utiliza programação linear para encontrar a melhor combinação de ativos.

## Estrutura do Código
O código está organizado em diretórios que contêm diferentes componentes do projeto:
```
portfolio-optimization/
│
├── src/
│ ├── portfolio_optimizer.py # Lógica principal da otimização da carteira
│ ├── visualization.py # Funções para visualização dos resultados
│ └── ticker_manager.py # Gerenciamento de tickers e filtragem
│
├── tests/
│ └── test_portfolio_optimizer.py # Testes unitários para garantir a funcionalidade
│
├── docs/
│ └── documentation.md # Este arquivo
│
├── README.md # Informações gerais sobre o projeto
└── requirements.txt # Dependências necessárias para o projeto
```

## Classes e Funções Principais

### PortfolioOptimizer

**Descrição**: Esta classe é responsável pela lógica principal da otimização da carteira.

#### Métodos

- **`__init__(self, tickers, risk_limit)`**
  - **Parâmetros**:
    - `tickers`: Lista de símbolos dos ativos.
    - `risk_limit`: Limite máximo de risco aceitável.
  - **Descrição**: Inicializa a classe e calcula os retornos e riscos dos ativos.

- **`get_data(self)`**
  - **Retorno**: DataFrame com os retornos diários dos ativos.
  - **Descrição**: Coleta dados históricos dos ativos usando a biblioteca `yfinance`.

- **`optimize_portfolio(self)`**
  - **Retorno**: Tuple contendo os pesos da carteira, retorno esperado e risco da carteira.
  - **Descrição**: Realiza a otimização da carteira usando programação linear, maximizando o retorno esperado sob a restrição de risco.

### Funções de Visualização

Estas funções são responsáveis por gerar gráficos que ajudam na análise dos resultados da otimização.

- **`plot_asset_allocation(weights, tickers)`**
  - **Parâmetros**:
    - `weights`: Lista com os pesos dos ativos na carteira.
    - `tickers`: Lista com os símbolos dos ativos.
  - **Descrição**: Plota a alocação dos ativos na carteira em um gráfico de barras.

- **`plot_efficient_frontier(returns_list, risks_list)`**
  - **Parâmetros**:
    - `returns_list`: Lista com os retornos simulados.
    - `risks_list`: Lista com os riscos simulados.
  - **Descrição**: Plota a fronteira eficiente em um gráfico disperso.

- **`plot_performance_over_time(dates, returns)`**
  - **Parâmetros**:
    - `dates`: Datas correspondentes aos retornos acumulados.
    - `returns`: Retornos acumulados ao longo do tempo.
  - **Descrição**: Plota a evolução do retorno ao longo do tempo em um gráfico de linha.

### Gerenciamento de Tickers

Esta parte do código é responsável por obter e filtrar os tickers disponíveis.

- **`get_all_tickers()`**
  - **Retorno**: Lista com todos os tickers disponíveis na bolsa.
  - **Descrição**: Utiliza a biblioteca `get-all-tickers` para obter todos os tickers disponíveis.

- **`filter_valid_tickers(all_tickers, risk_limit)`**
  - **Parâmetros**:
    - `all_tickers`: Lista completa de tickers.
    - `risk_limit`: Limite máximo de risco aceitável.
  - **Retorno**: Lista filtrada de tickers válidos.
  - **Descrição**: Filtra os tickers com base no limite de risco especificado.

## Processo de Otimização
O processo de otimização envolve as seguintes etapas:

1. Obter todos os tickers disponíveis usando `get_all_tickers()`.
2. Filtrar os tickers válidos com base no limite de risco usando `filter_valid_tickers()`.
3. Criar uma instância da classe `PortfolioOptimizer` com os tickers válidos e o limite de risco.
4. Chamar o método `optimize_portfolio()` para calcular os pesos ótimos da carteira, o retorno esperado e o risco.

## Gráficos Gerados

O projeto gera gráficos que ajudam na visualização dos resultados da otimização:

1. **Fronteira Eficiente**: Mostra a relação entre risco e retorno esperado, permitindo visualizar as melhores combinações possíveis.
   
2. **Alocação de Ativos**: Exibe como os ativos estão distribuídos na carteira, facilitando a identificação de concentrações indesejadas.

3. **Histórico de Desempenho da Carteira**: Mostra a evolução do retorno ao longo do tempo, permitindo avaliar o desempenho da carteira.

## Conclusão

Esta documentação fornece uma visão geral das principais classes e funções utilizadas no projeto, além do processo envolvido na otimização da carteira. Para mais detalhes ou sugestões, consulte o arquivo README.md ou entre em contato com o autor do projeto.
