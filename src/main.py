import uvicorn
from fastapi import UploadFile
from starlette import status
from starlette.responses import JSONResponse
from settings import app

from utils import scale_recipe, get_recipe

@app.post("/api/scale-recipe")
def scale_recipe_servings(serving_size: int):
    
    default_servings = 4
    file_name = "carbonara_recipe.csv"
    recipe = get_recipe(file_name)
    response = scale_recipe(recipe, default_servings, serving_size)
    print(response)
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"code": 200, "data": response},
    )
   

    

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)