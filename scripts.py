import os
import sys
import django
from datetime import timedelta

# Set up Django environment
sys.path.append("project")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

# Function to interact with Django models
def main():
    # Import necessary models
    from recipes.models import Recipe, Ingredient, RecipeIngredient, Instruction, Category, RecipeImage
    
    # Function to create Leaves Grep recipe
    def create_leaves_grep_recipe():
        # Leaves Grep recipe
        leaves_grep_recipe = Recipe.objects.create(
            title="Leaves Grep",
            description="Leaves Grep is a traditional dish from the Mediterranean region made with grape leaves stuffed with a mixture of rice, onions, tomatoes, and various herbs and spices.",
            prep_time=timedelta(hours=1),   # Use timedelta object
            cook_time=timedelta(hours=2),    # Use timedelta object
            cuisine="Mediterranean",
            avg_rating=4.9,
            difficulty="Medium"
        )

        # Ingredients for Leaves Grep
        grape_leaves = Ingredient.objects.create(name="Grape Leaves")
        rice = Ingredient.objects.create(name="Rice")
        onion = Ingredient.objects.create(name="Onion")
        tomato = Ingredient.objects.create(name="Tomato")
        herbs = Ingredient.objects.create(name="Herbs and Spices")

        # Add RecipeIngredients for Leaves Grep
        RecipeIngredient.objects.create(recipe=leaves_grep_recipe, ingredient=grape_leaves, quantity="1 jar")
        RecipeIngredient.objects.create(recipe=leaves_grep_recipe, ingredient=rice, quantity="1 cup")
        RecipeIngredient.objects.create(recipe=leaves_grep_recipe, ingredient=onion, quantity="1 large, finely chopped")
        RecipeIngredient.objects.create(recipe=leaves_grep_recipe, ingredient=tomato, quantity="2 medium, diced")
        RecipeIngredient.objects.create(recipe=leaves_grep_recipe, ingredient=herbs, quantity="To taste")

        # Instructions for Leaves Grep
        Instruction.objects.create(recipe=leaves_grep_recipe, step_number=1, description="Prepare grape leaves by rinsing and draining.")
        Instruction.objects.create(recipe=leaves_grep_recipe, step_number=2, description="Cook rice according to package instructions.")
        Instruction.objects.create(recipe=leaves_grep_recipe, step_number=3, description="Mix cooked rice with chopped onion, diced tomato, and herbs.")
        Instruction.objects.create(recipe=leaves_grep_recipe, step_number=4, description="Place a spoonful of the rice mixture onto each grape leaf and fold into a compact parcel.")
        Instruction.objects.create(recipe=leaves_grep_recipe, step_number=5, description="Arrange stuffed grape leaves in a baking dish, cover with water, and bake until tender.")

        # Assign recipe to appropriate categories
        mediterranean_category, _ = Category.objects.get_or_create(name="Mediterranean Cuisine")
        mediterranean_category.recipes.add(leaves_grep_recipe)

        # Add images if available
        # Replace the image URL with the local file path
        RecipeImage.objects.create(recipe=leaves_grep_recipe, image_url="/home/sarah/Documents/images/leaves_grep.jpg")

    # Call the function to create Leaves Grep recipe
    create_leaves_grep_recipe()

# Call the main function
if __name__ == "__main__":
    main()
