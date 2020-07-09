# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[], is_light=True):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.n_to = self.e_to = self.s_to = self.w_to = False
        self.items = items