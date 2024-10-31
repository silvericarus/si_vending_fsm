class Clock:
    def ___init___(self):
        self.seconds = 0
        self.clock_tick()
        
    def get_time(self):
        return self.seconds
    
    def clock_tick(self):
        if self.seconds == 60:
            self.seconds = 0
        else:
            self.seconds += 1