import pandas as pd
from pathlib import Path

mod_path = Path(__file__).parent

def scale_recipe(recipe: dict, recipe_serving_size:int,  servings: int):
    """
    scale the given recipe based on the user's desired serving size

    :param:
        recipe_serving_size (int): original serving size as per the given recipe
        servings (int): serving the user wants to modify the amount of recipe
    """
    servings_ratio = servings / recipe_serving_size
    print("servings_ratio ", servings_ratio)

    scaled_recipe = {ingredient: {'Quantity': amount['Quantity'] * servings_ratio 
                                  if amount['Quantity'] > 0 else None,
                                  'Unit': amount['Unit']
                                }
                      for ingredient, amount in recipe.items()}

    return scaled_recipe

def get_recipe(file_name: str)-> dict:
    """
    format the recipe given the data
    """
    file = mod_path /f"data/{file_name}"
    carbonara_recipe_df = pd.read_csv(file)
    carbonara_recipe_df['Quantity'] = carbonara_recipe_df['Quantity'].astype(float)
    carbonara_recipe_df = carbonara_recipe_df.where(pd.notnull(carbonara_recipe_df), 0)
    converted_dict = carbonara_recipe_df.set_index('Ingredient').to_dict(orient='index')
    print(converted_dict)

    return converted_dict
