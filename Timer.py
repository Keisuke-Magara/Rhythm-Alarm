import time

class MusicTimer:
    start_time = 0
    stop_time = 0
    lap_time = 0
    total_time = 0
    def start(self):
        self.start_time = time.time()*1000

    def stop(self):
        self.stop_time = time.time()*1000
        self.total_time += (self.stop_time - self.start_time)
        return self.total_time
    
    def reset(self):
        self.start_time = 0
        self.stop_time = 0
        self.lap_time = 0
        self.total_time = 0
    
    def get_time(self):
        return self.total_time