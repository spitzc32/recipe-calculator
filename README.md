# recipe-calculator

A recipe calculator endpoint that calculates a recipe given the data of recipe.

## Setup (Docker)
To build the image:

`docker build -t recipe-calc .`

To run the container, port 5001 must be available:

`docker run  -t -i --rm --name recipe-calc-cont -p 5001:5001 recipe-calc`
