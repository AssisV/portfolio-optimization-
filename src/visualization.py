def plot_asset_allocation(weights, tickers): 
    """
    Plota a alocação dos ativos na carteira.

    :weights: Pesos dos ativos na carteira.
    :tickers: Lista de símbolos dos ativos.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=tickers, y=weights)
    plt.title('Alocação de Ativos na Carteira')
    plt.ylabel('Peso')
    plt.xlabel('Ativos')
    plt.show()

def plot_efficient_frontier(returns_list, risks_list):
    """
    Plota a fronteira eficiente.

    :returns_list: Lista de retornos simulados.
    :risks_list: Lista de riscos simulados.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(risks_list, returns_list, alpha=0.1)
    plt.title('Fronteira Eficiente')
    plt.xlabel('Risco (Volatilidade)')
    plt.ylabel('Retorno Esperado')
    plt.grid()
    plt.show()

def plot_performance_over_time(dates, returns):
    """
    Plota a evolução do retorno ao longo do tempo.

    :dates: Datas correspondentes aos retornos.
    :returns: Retornos acumulados ao longo do tempo.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(dates, returns)
    plt.title('Evolução do Retorno ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Retorno Acumulado')
    plt.grid()
    plt.show()
