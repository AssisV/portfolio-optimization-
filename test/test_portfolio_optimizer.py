def main(): 
   all_tickers = get_all_tickers()  # Obtenha todos os tickers disponíveis
   
   risk_limit = 0.38  # Limite de risco 0.38

   # Filtra os tickers válidos com base no limite de risco
   valid_tickers = filter_valid_tickers(all_tickers, risk_limit)
   
   if not valid_tickers:
       print("Nenhum ticker válido encontrado dentro do limite de risco.")
       return
   
   print("Tickers Válidos:", valid_tickers)

   optimizer = PortfolioOptimizer(valid_tickers, risk_limit)
   
   # Otimização da carteira
   weights, portfolio_return, portfolio_risk = optimizer.optimize_portfolio()

   print("Pesos da Carteira:", weights)
   print("Retorno Esperado da Carteira:", portfolio_return)
   print("Risco da Carteira:", portfolio_risk)

   plot_asset_allocation(weights, valid_tickers)

   returns_list = []
   risks_list = []

   for _ in range(10000):
       random_weights = np.random.random(len(valid_tickers))
       random_weights /= np.sum(random_weights)

       simulated_return = np.dot(random_weights, optimizer.expected_returns)
       simulated_risk = np.sqrt(np.dot(random_weights.T,
                                         np.dot(optimizer.returns.cov() * 252,
                                                random_weights)))

       returns_list.append(simulated_return)
       risks_list.append(simulated_risk)

   plot_efficient_frontier(returns_list, risks_list)

   daily_returns = optimizer.returns.dot(weights)
   cumulative_returns = (1 + daily_returns).cumprod() - 1
   dates = cumulative_returns.index

   plot_performance_over_time(dates, cumulative_returns)

if __name__ == "__main__":
   main()
