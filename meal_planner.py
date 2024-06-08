def calculate_calories(age, height, weight, exercise_level, goal):
    base_calories = 10 * weight + 6.25 * height - 5 * age
    if exercise_level == "Low":
        base_calories *= 1.2
    elif exercise_level == "Medium":
        base_calories *= 1.5
    else:
        base_calories *= 1.8
    
    if goal == "Weight Loss":
        base_calories -= 500
    elif goal == "Weight Gain":
        base_calories += 500

    return base_calories

def get_meal_plan(calories, diet_type, dietary_constraints):
    meal_plan = [
        {"meal": "Breakfast", "items": ["Oatmeal", "Fruit"], "calories": 300},
        {"meal": "Lunch", "items": ["Salad", "Chicken"], "calories": 500},
        {"meal": "Dinner", "items": ["Vegetables", "Fish"], "calories": 400},
    ]

    if dietary_constraints:
        meal_plan = apply_dietary_constraints(meal_plan, dietary_constraints)

    return meal_plan

def apply_dietary_constraints(meal_plan, constraints):
    filtered_meal_plan = []
    for meal in meal_plan:
        meets_constraints = all(item not in constraints for item in meal["items"])
        if meets_constraints:
            filtered_meal_plan.append(meal)
    return filtered_meal_plan
