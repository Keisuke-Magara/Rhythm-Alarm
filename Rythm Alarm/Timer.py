import time

class MusicTimer:
    def __init__ (self):
        self.start_time = None
        self.stop_time = None
        self.lap_time = None
        self.total_time = None
        self.moving = False
        self.reset()

    def start(self):
        self.start_time = time.time()*1000
        self.moving = True

    def stop(self):
        self.stop_time = time.time()*1000
        self.total_time += (self.stop_time - self.start_time)
        self.moving = False
        return self.total_time
    
    def reset(self):
        self.start_time = 0
        self.stop_time = 0
        self.lap_time = 0
        self.total_time = 0
        self.moving = False
    
    def get_time(self):
        self.lap_time = self.total_time
        if (self.moving == True):
            self.lap_time += (time.time()*1000 - self.start_time)
        return self.lap_time