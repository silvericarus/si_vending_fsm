class InputCoinInitialization:
    def __init__(self, clock, reset, coin_initialization):
        self.clock = clock
        self.reset = reset
        self.ci = coin_initialization
        self.insert_coin = self.ci.inserting_coin
        self.coin_signal = self.ci.coin_signal
        self.accept_coin = 0
        self.current_amount = 0
        
    def __str__(self):
        return f"Current coin you are inserting: {self.insert_coin}, ¿Is coin accepted?: {self.accept_coin}, Signal to insert coin: {self.coin_signal}, Current amount: {self.current_amount}"
    
    def set_accept_coin(self, accept_coin):
        self.ci.accept_coin = accept_coin
        
    def get_current_amount(self):
        return self.current_amount
    
    def set_current_amount(self, current_amount):
        self.current_amount = current_amount