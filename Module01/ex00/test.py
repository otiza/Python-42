from book import Book
from recipe import Recipe
import sys

book = Book("My book")
bmw = Recipe("Omelette", 1, 10, ["eggs", "tomatoes", "oil"], "lunch", "bid w maticha")
pizza = Recipe("Pizza", 2, 30, ["flour", "tomatoes", "cheese"], "lunch", "mamia alberto this is not how you make a pizza")
taco = Recipe("Taco", 3, 20, ["tortilla", "tomatoes", "cheese"], "lunch", "tacos 7ssn mn dyal l akhawayn at least")
bmw_str = str(bmw)
print(bmw_str)
if __name__ != "__main__":
    sys.exit()