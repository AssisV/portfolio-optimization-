def get_all_tickers(): 
    """
    Obtém uma lista de tickers disponíveis na bolsa.
    
    :return: Lista de tickers.
    """
    return ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NFLX', 'META', 'NVDA', 'AMD', 'DIS']


def filter_valid_tickers(all_tickers, risk_limit):
    """
    Filtra tickers válidos com base no limite de risco.

    :all_tickers: Lista completa de tickers.
    :risk_limit: Limite máximo de risco aceitável.
    :return: Lista filtrada de tickers válidos.
    """
    valid_tickers = []
    
    for ticker in all_tickers:
        try:
            data = yf.download(ticker, start="2020-01-01", end="2024-01-01")['Adj Close']
            returns = data.pct_change().dropna()
            risk = returns.std() * np.sqrt(252)  # Risco anualizado
            
            if risk <= risk_limit:
                valid_tickers.append(ticker)
                
        except Exception as e:
            print(f"Erro ao processar {ticker}: {e}")
    
    return valid_tickers
