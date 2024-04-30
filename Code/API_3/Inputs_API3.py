class InputAPI3:
    def __init__(self, api_url, api_key, market_data_pair, trade_pair, trade_type, quantity, price):
        self.api_url = api_url
        self.api_key = api_key
        self.market_data_pair = market_data_pair
        self.trade_pair = trade_pair
        self.trade_type = trade_type
        self.quantity = quantity
        self.price = price

    def get_market_data_input(self):
        return {
            "URL de l'API": self.api_url,
            "Clé de l'API": self.api_key,
            "Paire de Marché": self.market_data_pair
        }

    def get_trade_input(self):
        return {
            "URL de l'API": self.api_url,
            "Clé de l'API": self.api_key,
            "Paire de Trade": self.trade_pair,
            "Type d'Ordre": self.trade_type,
            "Quantité": self.quantity,
            "Prix": self.price
        }
