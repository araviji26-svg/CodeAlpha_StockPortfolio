stock_prices = {
    "AAPL": 180.50,
    "TSLA": 240.00,
    "GOOGL": 140.25,
    "MSFT": 410.00,
    "AMZN": 175.10,
}

def main():
  print("--- Welcome to Your Stock Portfolio Tracker ---")
  print("Available stocks and prices per share:")
  for symbol, price in stock_prices.items():
    print(f"  {symbol}: ${price}")

  portfolio = {}
  total_investment = 0.0
  while True:
    ticker = input("\nEnter stock symbol to buy (or type 'done' to finish): ").upper()
    if ticker == "DONE":
      break

    if ticker not in stock_prices:
      print("Stock not found in price list. Try again.")
      continue

    try:
      shares = int(input(f"Enter number of shares for {ticker}: "))
      if shares < 0:
        print("Number of shares cannot be negative.")
        continue
    except ValueError:
      print("Please enter a valid integer for shares.")
      continue

    portfolio[ticker] = shares
    cost = shares * stock_prices[ticker]
    total_investment += cost
    print(f"Added {shares} shares of {ticker} for a cost of ${cost:.2f}")

  print("\n--- Portfolio Summary ---")
  summary_lines = ["--- Stock Portfolio Summary ---\n"]

  for ticker, shares in portfolio.items():
    price = stock_prices[ticker]
    value = shares * price
    line = f"{ticker}: {shares} shares @ ${price:.2f} each = ${value:.2f}"
    print(line)
    summary_lines.append(line + "\n")

  total_line = f"\nTotal Portfolio Value: ${total_investment:.2f}"
  print(total_line)
  summary_lines.append(total_line)

  filename = "portfolio_summary.txt"
  with open(filename, "w") as file:
    file.writelines(summary_lines)
      
  print(f"\nPortfolio successfully saved to {filename}!")
if __name__ == "__main__":
  main()
