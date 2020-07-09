class Item:
    def __init__(self, name, description, light_source=False, treasure=False):
        self.name = name
        self.description = description
        self.light_source = light_source
        self.treasure = treasure
    def on_take(self):
        print(f"You have picked up {self.name}.")
    def on_drop(self):
        print(f"You have dropped {self.name}.")