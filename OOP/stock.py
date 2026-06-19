class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"


# Main

stock1 = Stock("AAPL", 150, "Apple Inc.")
stock2 = Stock("GOOG", 2800, "Alphabet Inc.")

print(stock1.get_description())
print(stock2.get_description())