# Otimização de Carteira de Investimentos

## Descrição do Projeto
Este projeto tem como objetivo desenvolver um algoritmo de otimização de carteira que maximize o retorno esperado, respeitando um limite de risco aceitável. Utilizando técnicas de programação linear, o algoritmo permite que os investidores construam uma carteira diversificada com base em dados históricos de preços de ações.

## Objetivo do Trabalho
O objetivo principal deste trabalho é:
- Criar uma ferramenta que ajude investidores a otimizar suas carteiras de ações.
- Proporcionar uma análise visual dos resultados da otimização, permitindo uma melhor compreensão da alocação de ativos e do desempenho da carteira ao longo do tempo.

## Abordagem Utilizada para a Otimização
A otimização da carteira é realizada utilizando a biblioteca `scipy.optimize` para resolver problemas de programação linear. O algoritmo considera:
- **Retorno Esperado**: Calculado com base na média dos retornos diários anualizados.
- **Risco**: Medido pelo desvio padrão dos retornos diários anualizados.
- **Limites**: Os pesos dos ativos na carteira são restritos a um intervalo definido (por exemplo, entre 5% e 20%).

## Estrutura do Repositório
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
│ └── documentation.md # Documentação detalhada das funções e métodos
│
├── README.md # Este arquivo
└── requirements.txt # Dependências necessárias para o projeto


## Instruções de Instalação e Execução

### Pré-requisitos
Certifique-se de ter o Python 3.x instalado em seu sistema. Você pode baixar o Python em [python.org](https://www.python.org/downloads/).

### Passo a Passo

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/AssisV/portfolio-optimization.git
   cd portfolio-optimization

