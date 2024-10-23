class Assortment:
    def __init__(self, clock, reset, coin_amount, button1, button2, button3, button4, button5):
        self.clock = clock
        self.reset = reset
        self.coin_amount = coin_amount
        self.button1 = button1
        self.button2 = button2
        self.button3 = button3
        self.button4 = button4
        self.button5 = button5
        self.selection_available = True
        
    def get_selection_available(self):
        return self.selection_available