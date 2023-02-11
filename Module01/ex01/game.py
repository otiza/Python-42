

class GotCharacter:
    def __init__(self, first_name :str, is_alive: bool = True):
        if not isinstance(first_name, str) or not isinstance(is_alive, bool):
            raise TypeError("first_name must be a  string, is_alive must be a boolean")
        self.first_name = first_name
        self.is_alive = is_alive

class Targryen(GotCharacter):
    """A class representing the Targryen family"""
    def __init__(self, first_name :str, is_alive: bool = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Targryen"
        self.house_words = "Fire and Blood"
    
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False


arya = Targryen("Arya")
arya.print_house_words()
print(arya.__dict__)
arya.die()
print(arya.is_alive)
