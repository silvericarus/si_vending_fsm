class CoinBank:
    def __init__(self):
        self.price1 = 0
        self.price2 = 0
        self.price3 = 0
        self.price4 = 0
        self.price5 = 0

    def get_price1(self):
        return self.price1
    
    def get_price2(self):
        return self.price2
    
    def get_price3(self):
        return self.price3
    
    def get_price4(self):
        return self.price4

    def get_price5(self):
        return self.price5
    
    def set_price1(self, price1):
        self.price1 = price1
        
    def set_price2(self, price2):
        self.price2 = price2
        
    def set_price3(self, price3):
        self.price3 = price3
        
    def set_price4(self, price4):
        self.price4 = price4
        
    def set_price5(self, price5):
        self.price5 = price5
