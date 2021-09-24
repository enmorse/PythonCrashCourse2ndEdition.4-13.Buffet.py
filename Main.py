# A buffet - stlye restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple.

# Use a for loop to print each food the restaurant offers.

# Try to modify one of the items, and make sure Python
# rejects the change.

# The restaurant changes its menu, replacing two of the
# items with different foods.

# Add a line that rewrites the tuple, and then uses a for
# loop to print each of the items on the revised menu.

basic_foods = (
    "steak",
    "sweet potato",
    "chicken",
    "pineapple",
    "avocado",
)
print("Original Menu")
for food in basic_foods:
    print(food.title(), end=" ")

# basic_foods[0] = "steak and eggs"

basic_foods = (
    "steak",
    "yam",
    "raw tuna poke bowl",
    "pineapple",
    "avocado",
)
print("\nModified Menu")
for food in basic_foods:
    print(food.title(), end=" ")
