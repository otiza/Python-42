from book import Book
from recipe import Recipe
import sys

book = Book("My book")
bmw = Recipe("Omelette", 1, 10, ["eggs", "tomatoes", "oil"], "lunch", "bid w maticha")
pizza = Recipe("Pizza", 2, 30, ["flour", "tomatoes", "cheese"], "lunch", "mamia alberto this is not how you make a pizza")
taco = Recipe("Taco", 3, 20, ["tortilla", "tomatoes", "cheese"], "dessert", "tacos 7ssn mn dyal l akhawayn at least")
print("############# testing the recipe str method #############")
print(taco)
print("####################################################")
print("###### testing the book add_recipe method ###########")
book.add_recipe(bmw)
book.add_recipe(pizza)
book.add_recipe(taco)
print("####################################################")
print("###### testing the book get_recipe_by_name method ###########")
print(book.get_recipe_by_name("Pizza"))
print(book.get_recipe_by_name("Taco"))
print(book.get_recipe_by_name("Omelette"))
print("####################################################")
print("###### testing the book get_recipes_by_types method ###########")
recipes = book.get_recipes_by_types("lunch")
for recipe in recipes:
    print(recipe)
print("####################################################")
if __name__ != "__main__":
    sys.exit()