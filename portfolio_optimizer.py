class PortfolioOptimizer:
    def __init__(self, tickers, risk_limit):
        """
        Inicializa o otimizador de carteira com os ativos e limite de risco.
        
        :tickers: Lista de símbolos dos ativos.
        :risk_limit: Limite máximo de risco aceitável (capacidade da mochila).
        """
        self.tickers = tickers
        self.risk_limit = risk_limit
        self.returns = self.get_data()
        self.expected_returns = self.returns.mean() * 252  # Retorno anualizado
        self.risks = self.returns.std() * np.sqrt(252)      # Risco anualizado

    def get_data(self):
        """
        Coleta dados históricos dos ativos usando yfinance.
        
        :return: DataFrame com os retornos diários.
        """
        data = yf.download(self.tickers, start="2020-01-01", end="2024-01-01")['Adj Close']
        return data.pct_change().dropna()

    def optimize_portfolio(self):
        """
        Otimiza a carteira para maximizar o retorno esperado respeitando o limite de risco.
        
        :return: Pesos da carteira, retorno esperado e risco da carteira.
        """
        c = -self.expected_returns.values  # Coeficientes para maximizar o retorno
        A = [self.risks.values]            # Matriz de restrições (risco)
        b = [self.risk_limit]               # Limite de risco máximo

        bounds = [(0.05, 0.2) for _ in range(len(self.tickers))]
        
        # Resolvendo o problema de otimização
        result = linprog(c, A_ub=A, b_ub=b, bounds=bounds)

        if result.success:
            weights = result.x
            portfolio_return = -result.fun
            portfolio_risk = np.dot(weights, self.risks)
            return weights, portfolio_return, portfolio_risk
        else:
            raise ValueError("Otimização falhou!")
