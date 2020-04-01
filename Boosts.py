class Boosts:
    def __init__(self, name, boost, cost):
        self.name = name
        self.boost = boost
        self.cost = cost

    def get_name(self):
        return self.name

    def get_boost(self):
        return self.boost

    def get_cost(self):
        return self.cost