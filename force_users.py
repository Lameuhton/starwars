import starwars.entity as entity


class ForceUsers(entity.Entity):

    def __init__(self, name, HP, damage_points):
        super().__init__(name, HP)
        self.damage_points = damage_points

    def use_force_on(self, target):
        target.take_hit(self.damage_points)
        return f"{self.name} projette la force sur {target.name}. Dégâts causés: {self.damage_points}. \nHP de {target.name}: {target.HP}"


class Jedi(ForceUsers):

    def __init__(self, name, HP, damage_points):
        super().__init__(name, HP, damage_points)

    def use_force_on(self, target):
        if self.HP <= 2:
            target.take_hit(self.damage_points*10)
            p = f"{self.name} utilise la rage de la force sur {target.name}. Dégâts causés : {self.damage_points * 10}. \nHP de {target.name}: {target.HP}"
        else:
            p = super().use_force_on(target)
        return p


class Sith(ForceUsers):

    def __init__(self, name, HP, damage_points):
        super().__init__(name, HP, damage_points)
        self.use_count = 0

    def use_force_on(self, target):
        self.use_count += 1

        if self.use_count %3 == 0:
            if self.use_count %5 == 0:
                target.take_hit(self.damage_points*5)
                p = f"{self.name} lance des éclairs sur {target.name}. Dégâts causés : {self.damage_points * 5}"
            else:
                target.take_hit(self.damage_points*2)
                p = f"{self.name} étrangle {target.name}. Dégâts causés : {self.damage_points * 2}"
        elif self.use_count %5 == 0:
            target.take_hit(self.damage_points * 5)
            p = f"{self.name} lance des éclairs sur {target.name}. Dégâts causés : {self.damage_points * 5}"
        else:
            p = super().use_force_on(target)

        return p


