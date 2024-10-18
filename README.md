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
