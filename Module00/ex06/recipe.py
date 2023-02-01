import sys
cookbook = {
    "sandwich" : {
        'ingredients': ['ham','bread','cheese','tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    "Cake" : {
        'ingredients': ['flour','sugar','eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    "Salad" : {
        'ingredients': ['avocado','arugala','tomatoes','spinach'],
        'meal': 'lunch',
        'prep_time': 15
        
        ,
    },
}

def printAllRecipes():
    for x in cookbook:
        print(x)

def printRecipe(name):
    try:
        print(f"Recipe for {name}:")
        print(f"\tIngredients list: {cookbook[name]['ingredients']}")
        print(f"\tTo be eaten for {cookbook[name]['meal']}.")
        print(f"\tTakes {cookbook[name]['prep_time']} minutes of cooking.")
    except:
        print("recipe not found")

def deletRecipe(name):
    try:
        cookbook.pop(name)
    except:
        print("recipe not found")

def addRecipe():
    name = input(">>> Enter a name:\n")
    print(">>> Enter ingredients:")
    ingredient = []
    while True:
        line = input()
        if line:
            ingredient.append(line)
        else:
            break
    type = input(">>> Enter a meal type:\n")
    try:
        time = int(input(">>> Enter a  preparation time:\n"))
    except:
        print("time should be a positive number")
        sys.exit()
    meal = dict(ingredients= ingredient, meal= type, prep_time = time)
    try:
        cookbook[name] = meal
    except:
        print('meal already exist')


def printmenu():
    print('''
welcome to the Python Cookbook !
List of available option:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit
''')

def main():
    printmenu()
    inp = 0
    while inp != 5:
        try:
            inp = int(input("Please select an option:\n>> "))
        except:
            print("Sorry, this option does not exist.")
        if inp == 1:
            addRecipe()
        elif inp == 2:
            deletRecipe(input("Recipe name:\n>> "))
        elif inp == 3:
            printRecipe(input("Recipe name:\n>> "))
        elif inp == 4:
            printAllRecipes()       
        else : 
            print("Sorry, this option does not exist.")
#print(cookbook)
if __name__ == '__main__':
    main()
