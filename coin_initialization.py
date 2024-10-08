class CoinInitialization:
    def __init__(self):
        self.inserting_coin = 0 #Current coin you are inserting
        self.accept_coin = 0 #Is coin accepted?
        self.coin_signal = 0 #Signal to insert coin

    def __str__(self):
        return f"Current coin you are inserting: {self.inserting_coin}, ¿Is coin accepted?: {self.accept_coin}, Signal to insert coin: {self.coin_signal}"
    
    def get_coin_signal(self):
        return self.coin_signal
    
    def set_coin_signal(self, coin_signal):
        self.coin_signal = coin_signal
        
    def insert_coin(self):
        self.set_coin_signal(1)
        self.inserting_coin = True