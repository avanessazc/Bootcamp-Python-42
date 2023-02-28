class Recipe:
    """Class Recipe"""

    def __init__(self, name=None,
                 cooking_lvl=None,
                 cooking_time=None,
                 ingredients=None,
                 description=None,
                 recipe_type=None):
        if None in locals().values():
            print("Some argument is missing")
            exit()
        try:
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = list(ingredients)
            self.description = str(description)
            self.recipe_type = str(recipe_type)
            if (type(name) != str or name == ''):
                raise Exception("You must enter the recipe's name")
            elif (type(cooking_lvl) != int or (
                    cooking_lvl < 1 or cooking_lvl > 5)):
                raise Exception("\
You must enter cooking_lvl. A number(int) between 1 and 5")
            elif (type(cooking_time) != int or cooking_time < 0):
                raise Exception("You must enter cooking_time in minutes. \
A positive number")
            elif (type(ingredients) != list):
                raise Exception("You must enter the ingredients list")
            elif (type(ingredients) == list and len(ingredients) == 0):
                raise Exception("The ingredients list cannot be empty")
            elif (recipe_type not in ["starter", "lunch", "dessert"]):
                raise Exception("You must enter the recipe type: starter, \
lunch or dessert")
        except (Exception, ValueError) as e:
            print("Recipe class error:", repr(e))
            exit()

    def __str__(self):
        txt = "Recipe's name is: {}\n".format(self.name) \
            + "The lvl is: {}\n".format(self.cooking_lvl) \
            + "It takes {} minutes of cooking\n".format(self.cooking_time) \
            + "The ingredients are: {}\n".format(", ".join(self.ingredients)) \
            + "Description: {}\n".format(self.description) \
            + "To be eaten for {}.".format(self.recipe_type)
        return txt
