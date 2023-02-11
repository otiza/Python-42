import datetime
from recipe import Recipe
class Book:
    def __init__(self, name: str):
        if not isinstance(name, str) or name == "":
            raise TypeError("name must be a non-empty string")

        self.name = name
        
        self.creation_date = datetime.datetime.now()
        self.recipes_list : dict[str, list[Recipe]]= {
            "starter": [],
            "lunch": [],
            "dessert": []
        }
        self.last_update = datetime.datetime.now()

        def get_recipe_by_name(self, name):
            if not isinstance(name, str):
                raise TypeError("name must be a string")
            search_result = list(filter(lambda x: x.name == name, self.recipes_list["starter"] + self.recipes_list["lunch"] + self.recipes_list["dessert"]))
            if len(search_result) == 0:
                return None
            print(search_result[0])
            return search_result[0]
        
        def get_recipes_by_types(self, recipe_type):
            if not isinstance(recipe_type, str):
                raise TypeError("recipe_type must be a string")
            if not recipe_type in ["starter", "lunch", "dessert"] or not recipe_type:
                raise TypeError("recipe_type must be 'starter', 'lunch' or 'dessert'")
            return self.recipes_list[recipe_type]
        def add_recipe(self, recipe):
            if not isinstance(recipe, Recipe):
                raise TypeError("recipe must be a Recipe")
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()

if __name__ == "__main__":
    print("This file contains only the class Book")
