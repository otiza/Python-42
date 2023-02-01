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
        print(cookbook[name])
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
    print(meal)
    try:
        cookbook[name] = meal
    except:
        print('meal already exist')

addRecipe()
#print(cookbook)