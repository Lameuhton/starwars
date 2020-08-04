class Entity:

    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def take_hit(self, damage):
        self.HP = self.HP - damage

    def is_alive(self):
        return True if self.HP > 0 else False



