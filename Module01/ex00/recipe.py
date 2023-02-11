

class Recipe:
    
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type : str, description :str=""):
        if not isinstance(name, str) or name == "":
            raise TypeError("name must be a non-empty string")
        if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
            raise TypeError("cooking_lvl must be an integer between 1 and 5")
        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise TypeError("cooking_time must be a positive integer")
        if not isinstance(ingredients, list) or len(ingredients) == 0:
            raise TypeError("ingredients must be a non-empty list")
        if not isinstance(recipe_type, str) or recipe_type not in ["starter", "lunch", "dessert"]:
            raise TypeError("recipe_type must be 'starter', 'lunch' or 'dessert'")
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""
        return(
            f"Recipe name: {self.name}\n" 
            f"Cooking level: {self.cooking_lvl}\n"
            f"Cooking time: {self.cooking_time}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Recipe type: {self.recipe_type}\n"
            f"Description: {self.description}\n"
        )

if __name__ == "__main__":
    print("This file contains only the class Recipe")