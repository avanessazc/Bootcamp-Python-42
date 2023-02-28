from datetime import datetime
from recipe import Recipe


class Book:
    """Class Book"""

    def __init__(self, name="Cookbook"):
        self.name = name
        self.creation_date = self.get_current_time()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    # https://www.programiz.com/python-programming/methods/built-in/staticmethod
    @staticmethod
    def get_current_time() -> str:
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} \
and returns the instance"""
        for meals in self.recipes_list.values():
            for m in meals:
                if (m.name == name):
                    print(str(m))
                    return (m)
        print("Recipe does not exist in the book")
        return (None)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if (recipe_type not in self.recipes_list.keys()):
            print("Recipe type does not exist in the book")
            return (None)
        meal_names = [meal.name for meal in self.recipes_list[recipe_type]]
        return (meal_names)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if (not isinstance(recipe, Recipe)):
            print("Argument is not a Recipe type")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = self.get_current_time()
