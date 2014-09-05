class counter(object):
    def __init__(self):
        self.num = 3
    def countup(self):
        self.num += 1
        return self.num
    def countdown(self):
        self.num -= 1
        if self.num == 0:
            return "fire!"
        return self.num

rocket = counter()
print rocket.countdown()
print rocket.countdown()
print rocket.countdown()