import random

class Star:
    def __init__(self, x, y, z, size):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.change_fl = 0
        self.growing = random.choice([True, False])

    def update_size(self):
        change_chance = random.randint(1, 1000)
        
        if change_chance > 999:
            self.change_fl = 1

        if self.change_fl == 1:
            if self.growing:
                self.size += 0.005
            else:
                self.size -= 0.005
