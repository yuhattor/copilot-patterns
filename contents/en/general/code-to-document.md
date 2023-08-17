---
name: "Code to Document"
description: "Generating documentation from code"
category: "general"
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: 100
---

## Code to Document

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

Chat-based AI tools can be used to automatically generate descriptions as well as longer texts such as documentation. For example, GitHub Copilot Chat can be leveraged to generate a full code synopsis, API documentation, and even output the entire code with it embedded within the code.

#### Sample Code

The following is a code snippet written for a Ruby on Rails Controller.

```ruby
class RecipesController < ApplicationController
   before_action :set_recipe, only: [:show, :edit, :update, :destroy]
   
   # GET /recipes
   # GET /recipes.json
   def index
      @recipes = Recipe.all
   end
   
   # GET /recipes/1
   # GET /recipes/1.json
   def show
   end
   
   # GET /recipes/new
   def new
      @recipe = Recipe.new
   end
   
   # GET /recipes/1/edit
   def edit
   end
   
   # POST /recipes
   # POST /recipes.json
   def create
      @recipe = Recipe.new(recipe_params)
      
      respond_to do |format|
         if @recipe.save
            format.html { redirect_to @recipe, notice: 'Recipe was successfully created.' }
            format.json { render :show, status: :created, location: @recipe }
         else
            format.html { render :new }
            format.json { render json: @recipe.errors, status: :unprocessable_entity }
         end
      end
      
   end
   
   # PATCH/PUT /recipes/1
   # PATCH/PUT /recipes/1.json
   def update
      respond_to do |format|
         if @recipe.update(recipe_params)
            format.html { redirect_to @recipe, notice: 'Recipe was successfully updated.' }
            format.json { render :show, status: :ok, location: @recipe }
         else
            format.html { render :edit }
            format.json { render json: @recipe.errors, status: :unprocessable_entity }
         end
      end
      
   end
   
   # DELETE /recipes/1
   # DELETE /recipes/1.json
   def destroy
      @recipe.destroy
         respond_to do |format|
         format.html { redirect_to recipes_url, notice: 'Recipe was successfully destroyed.' }
         format.json { head :no_content }
      end
   end
   
   private
   
   # Use callbacks to share common setup or constraints between actions.
   def set_recipe
      @recipe = Recipe.find(params[:id])
   end
   
   # Never trust parameters from the scary internet, only allow the white list through.
   def recipe_params
      params.require(:recipe).permit(:title, :instructions)
   end
end
```

#### Sample Result

Here is the specification document generated from the above Ruby code, displayed in markdown format.

```md
## RecipesController

RecipesController provides operations for creating, viewing, editing, and deleting recipes, etc.

### Actions

#### `index`

- Description: Retrieves a list of recipes.
- Method: GET
- Path: `/recipes`
- Response: List of recipes

#### `show`

- Description: Retrieves detailed information about a specific recipe.
- Method: GET
- Path: `/recipes/:id`
- Parameter: `id` - Recipe's ID
- Response: Detailed information about the recipe

#### `new`

- Description: Displays the creation screen for a new recipe.
- Method: GET
- Path: `/recipes/new`

#### `edit`

- Description: Displays the editing screen for a specific recipe.
- Method: GET
- Path: `/recipes/:id/edit`
- Parameter: `id` - Recipe's ID

#### `create`

- Description: Creates a new recipe.
- Method: POST
- Path: `/recipes`
- Parameter: `recipe` - Recipe information
- Response: Detailed information about the created recipe

#### `update`

- Description: Updates a specific recipe.
- Method: PATCH/PUT
- Path: `/recipes/:id`
- Parameters: `id` - Recipe's ID, `recipe` - Information to update
- Response: Detailed information about the updated recipe

#### `destroy`

- Description: Deletes a specific recipe.
- Method: DELETE
- Path: `/recipes/:id`
- Parameter: `id` - Recipe's ID
- Response: Detailed information about the deleted recipe
```

### Exercise

- **Exercise 1**: Utilize the provided Ruby code and experiment with generating different types of documentation, such as user manuals, API references, or code comments. Compare the differences and similarities.
- **Exercise 2**: Modify the Ruby code to include more complex functionalities, and then use GitHub Copilot Chat to generate the corresponding documentation. Analyze the generated documentation for accuracy and completeness.
- **Exercise 3**: Create a set of guidelines that would be important to follow when using AI tools like GitHub Copilot Chat for generating documentation. These guidelines should include considerations for clarity, accuracy, consistency, and maintainability.

### Checklist for Further Learning

- Does the generated documentation appropriately describe each action and functionality of the code?
- Does the documentation clearly represent the specifications of the API?
- What should be taken into account when generating documentation from code?
