import streamlit as st
import random
import json

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="Let's Eat!",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.image("drawings/header.png", width=260)
st.write("")

# -----------------------------
# Load meals JSON
# -----------------------------
MEALS_FILE = "meals.json"

with open(MEALS_FILE, "r") as f:
    meals = json.load(f)

cook_meals = meals["cook"]
order_meals = meals["order"]
late_night_meals = meals["late_night"]
us_two_meals = meals["us_two"]

# -----------------------------
# Protein selector
# -----------------------------
protein_choice = st.selectbox(
    "Choose a protein (optional)",
    ["Anything", "Chicken", "Beef", "Seafood", "Vegetarian"]
)

st.write("")

# -----------------------------
# Buttons row
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("drawings/dice.png", width=90)
    anything = st.button("Anything")

with col2:
    st.image("drawings/pan.png", width=90)
    cook = st.button("Let's Cook")

with col3:
    st.image("drawings/scooter.png", width=90)
    order = st.button("Let's Order")

with col4:
    st.image("drawings/late.png", width=90)
    late = st.button("Late Night")

with col5:
    st.image("drawings/us_two.png", width=90)
    us_two = st.button("Us Two")

# -----------------------------
# Meal picker function
# -----------------------------
def pick_meal(meal_list, protein):
    if not meal_list:
        return None

    if protein == "Anything":
        return random.choice(meal_list)

    filtered = [m for m in meal_list if m["protein"] == protein]
    if filtered:
        return random.choice(filtered)

    return random.choice(meal_list)

# -----------------------------
# Show result
# -----------------------------
st.write("")

if anything:
    all_meals = cook_meals + order_meals + late_night_meals + us_two_meals
    meal = pick_meal(all_meals, protein_choice)
    if meal:
        st.success(f"✨ You should eat: **{meal['name']}**")

if cook:
    meal = pick_meal(cook_meals, protein_choice)
    if meal:
        st.success(f"🍳 Let's cook: **{meal['name']}**")

if order:
    meal = pick_meal(order_meals, protein_choice)
    if meal:
        st.success(f"🛵 Let's order: **{meal['name']}**")

if late:
    meal = pick_meal(late_night_meals, protein_choice)
    if meal:
        st.success(f"🌙 Late night vibes: **{meal['name']}**")

if us_two:
    meal = pick_meal(us_two_meals, protein_choice)
    if meal:
        st.success(f"🫶 We should get: **{meal['name']}**")

# -----------------------------
# Add meal section
# -----------------------------
with st.expander("➕ Add a meal"):
    with st.form("add_meal_form"):
        new_meal = st.text_input("Meal name")

        meal_type = st.selectbox(
            "Type",
            ["Cook", "Order", "Late Night", "Us Two"]
        )

        meal_protein = st.selectbox(
            "Protein",
            ["Anything", "Chicken", "Beef", "Seafood", "Vegetarian"]
        )

        submitted = st.form_submit_button("Add")

        if submitted and new_meal:
            entry = {"name": new_meal, "protein": meal_protein}

            if meal_type == "Cook":
                cook_meals.append(entry)
            elif meal_type == "Order":
                order_meals.append(entry)
            elif meal_type == "Late Night":
                late_night_meals.append(entry)
            elif meal_type == "Us Two":
                us_two_meals.append(entry)

            with open(MEALS_FILE, "w") as f:
                json.dump(meals, f, indent=2)

            st.success("Meal added! 🎉")

# -----------------------------
# Footer
# -----------------------------
st.write("")
st.image("drawings/footer.png", width=200)
