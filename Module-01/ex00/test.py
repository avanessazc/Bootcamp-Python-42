from book import Book
from recipe import Recipe
from time import sleep

if __name__ == "__main__":
    # Recipe tests
    # recipe = Recipe("", 1, 123, ["ing1"], "", "lunch")
    # recipe = Recipe("Recipe1", "1", 123, ["ing1"], "", "lunch")
    # recipe = Recipe("Recipe1", 1, 123, ["ing1"], "", "lunch")
    # recipe = Recipe("Recipe1", 1, 123, ("ing1"), "", "lunch")
    # recipe = Recipe("Recipe1", 1, 123, ["ing1"], "", "Hola")

    salad = Recipe("salad",
                   4,
                   5,
                   ["tomates", "concombre", "sel", "poivre"],
                   "",
                   "starter")
    to_print = str(salad)
    print(to_print)
    print("\n")

    cookbook = Book()

    def cookbook_last_update():
        print("Cookbook Last Update: ", cookbook.last_update)

    cookbook_last_update()
    print("\n")
    recipe = None
    cookbook.add_recipe(recipe)

    sleep(3)
    recipe = Recipe("RecipeOne",
                    1,
                    123,
                    ["ing1", "ing2", "ing3"],
                    "",
                    "dessert")
    cookbook.add_recipe(recipe)
    cookbook_last_update()
    print("\n")

    sleep(3)
    recipe = Recipe("RecipeTwo",
                    1,
                    123,
                    ["ing1", "ing2", "ing3"],
                    "",
                    "starter")
    cookbook.add_recipe(recipe)
    cookbook_last_update()
    print("\n")

    sleep(3)
    recipe = Recipe("RecipeThree",
                    1,
                    123,
                    ["ing1", "ing2", "ing3"],
                    "",
                    "lunch")
    cookbook.add_recipe(recipe)
    cookbook_last_update()
    print("\n")

    sleep(3)
    recipe = Recipe("RecipeFour",
                    1,
                    123,
                    ["ing1", "ing2", "ing3"],
                    "",
                    "lunch")
    cookbook.add_recipe(recipe)
    cookbook_last_update()
    print("\n")

    sleep(3)
    recipe = Recipe("RecipeFive",
                    1,
                    123,
                    ["ing1", "ing2", "ing3"],
                    "",
                    "dessert")
    cookbook.add_recipe(recipe)
    cookbook_last_update()
    print("\n")

    print("\n")
    print("RecipeOne : " + str(cookbook.get_recipe_by_name("RecipeOne")))
    print("\n")
    print("RecipeTwo : " + str(cookbook.get_recipe_by_name("RecipeTwo")))
    print("\n")
    print("RecipeThree : " + str(cookbook.get_recipe_by_name("RecipeThree")))
    print("\n")
    print("RecipeFour : " + str(cookbook.get_recipe_by_name("RecipeFour")))
    print("\n")
    print("RecipeFive : " + str(cookbook.get_recipe_by_name("RecipeFive")))
    print("\n\n")
    print("Starter : " + str(cookbook.get_recipes_by_types('starter')))
    print("Lunch : " + str(cookbook.get_recipes_by_types('lunch')))
    print("Dessert : " + str(cookbook.get_recipes_by_types('dessert')))
