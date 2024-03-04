spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisin e": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

spicy_foods = [
    {"name": "Green Curry", "spiciness": "Medium"},
    {"name": "Buffalo Wings", "spiciness": "Hot"},
    {"name": "Mapo Tofu", "spiciness": "Spicy"}
]

result = get_names(spicy_foods)
print(result)
# Output: ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

#spiciest_foods
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level", 0) > 5]

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 4},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 8}
]

result = get_spiciest_foods(spicy_foods)
print(result)

#print_spicy_foods
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name", "Unknown")
        cuisine = food.get("cuisine", "Unknown")
        heat_level = food.get("heat_level", 0)
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

print_spicy_foods(spicy_foods)

#spicy_food_by_cuisine
def get_spicy_food_by_cuisine(spicy_foods, target_cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == target_cuisine:
            return food
        return None
    
    spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]
    
result1 = get_spicy_food_by_cuisine(spicy_foods, "American")
result2 = get_spicy_food_by_cuisine(spicy_foods, "Thai")

print(result1)
# Output: {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}
print(result2)
# Output: {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}

#print_spiciest_foods
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

print_spiciest_foods(spicy_foods)
# Output:
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

def average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  

    total_heat  = sum(food.get("heat_level", 0) for food in spicy_foods)
    average = total_heat / len(spicy_foods)
    return round(average) 

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

result = average_heat_level(spicy_foods)
print(result)
# Output: 6


def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods

# Example usage:
spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

new_spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

result = create_spicy_food(spicy_foods, new_spicy_food)
print(result)
# Output: new list with the new spicy food added
