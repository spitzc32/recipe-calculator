import pandas as pd

df = pd.read_csv('src/data/carbonara_recipe.csv')

# Convert DataFrame to dictionary
converted_dict = df.set_index('Ingredient').to_dict(orient='index')

# Display the converted dictionary
print(converted_dict)