import math

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections
        
    def hit_rate(self):
        return self.hits / (self.hits + self.misses)
    
    def false_alarm_rate(self):
        return self.false_alarms / (self.false_alarms + self.correct_rejections)
    
    def d_prime(self):
        hit_rate = self.hit_rate()
        false_alarm_rate = self.false_alarm_rate()
        return math.sqrt(2) * (math.erfinv(2 * hit_rate - 1) - math.erfinv(2 * false_alarm_rate - 1))
    
    def criterion(self):
        hit_rate = self.hit_rate()
        false_alarm_rate = self.false_alarm_rate()
        return -(math.erfinv(2 * hit_rate - 1) + math.erfinv(2 * false_alarm_rate - 1)) / 2
