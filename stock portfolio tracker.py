def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 135,
        "MSFT": 300
    }
    
    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    portfolio = {}  # store user stocks and quantities
    
    while True:
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        
        if stock == "DONE":
            break
        elif stock not in stock_prices:
            print("⚠️ Stock not available. Please choose from:", ", ".join(stock_prices.keys()))
            continue
        
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty <= 0:
                print("⚠️ Quantity must be positive.")
                continue
        except ValueError:
            print("⚠️ Invalid number, try again.")
            continue
        
        portfolio[stock] = portfolio.get(stock, 0) + qty
    
    # Calculate total investment
    total_value = 0
    print("\n📊 Your Portfolio:")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_value += value
        print(f"{stock} - {qty} shares × ${stock_prices[stock]} = ${value}")
    
    print(f"\n💰 Total Investment Value = ${total_value}")
    
    # Optional: Save to file
    save = input("\nDo you want to save portfolio to file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("========================\n")
            for stock, qty in portfolio.items():
                value = qty * stock_prices[stock]
                f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
            f.write(f"\nTotal Investment = ${total_value}")
        print("✅ Portfolio saved to portfolio.txt")

# Run the tracker
stock_portfolio_tracker()
