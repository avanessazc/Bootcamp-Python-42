cookbook = {
            'Sandwich': {
                'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                'meal': 'lunch',
                'prep_time': 10},
            'Cake': {
                'ingredients': ['flour', 'sugar', 'eggs'],
                'meal': 'dessert',
                'prep_time': 60},
            'Salad': {
                'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                'meal': 'lunch',
                'prep_time': 15}
}


def ft_print_recipe_names():
    for recipe_name in cookbook:
        print(recipe_name)


def ft_print_recipe_details(name):
    for recipe_name, recipe_info in cookbook.items():
        if (recipe_name == name):
            print("Recipe for {}:".format(recipe_name))
            print("    Ingredients list: {ingredients}\n\
    To be eaten for {meal}.\n\
    Takes {prep_time} minutes of cooking.".format(**recipe_info))
            return
    print("Recipe {} does not exist.".format(name))


def ft_delete_recipe(name):
    if name in cookbook:
        del cookbook[name]
        print("Recipe {} was deleted".format(name))
    else:
        print("Recipe {} does not exist.".format(name))


def ft_add_recipe():
    ingredients_list = []
    # Recipe name
    print("Enter a name:")
    recipe_name = input()
    while (recipe_name == ''):
        print("Enter a name:")
        recipe_name = input()
    # Recipe ingredients
    while (1):
        print("Enter ingredients:")
        ingredient = input()
        while (ingredient != ''):
            ingredients_list.append(ingredient)
            ingredient = input()
        if (len(ingredients_list) > 0):
            break
    # Recipe meal type
    print("Enter a meal type:")
    meal_type = input()
    while (meal_type == ''):
        print("Enter a meal type:")
        meal_type = input()
    # Recipe preparation time
    print("Enter a preparation time:")
    preparation_time = input()
    while preparation_time.isdigit() is False:
        print("Enter a preparation time:")
        preparation_time = input()
    # Adding recie to cookbook
    cookbook[recipe_name] = {'ingredients': ingredients_list,
                             'meal': meal_type,
                             'prep_time': preparation_time}


if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    while (1):
        try:
            print("List of available option:")
            print("  1: Add a recipe")
            print("  2: Delete a recipe")
            print("  3: Print a recipe")
            print("  4: Print the cookbook")
            print("  5: Quit")
            print("\nPlease select an option:")
            option = input()
            if (option.isdigit() is False or
                    int(option) < 1 or int(option) > 5):
                print("Sorry, this option does not exist.\n")
                continue
            if (option == '1'):
                ft_add_recipe()
                print("\n")
            elif (option == '2'):
                print("Enter a name:")
                name = input()
                ft_delete_recipe(name)
                print("\n")
            elif (option == '3'):
                print("Enter a name:")
                name = input()
                ft_print_recipe_details(name)
                print("\n")
            elif (option == '4'):
                ft_print_recipe_names()
                print("\n")
            elif (option == '5'):
                print("\nCookbook closed. Goodbye !")
                break
        except Exception:
            break
