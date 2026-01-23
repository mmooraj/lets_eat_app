import streamlit as st
import random
import json
import os

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
st.image("drawings/header.png", width=250)
st.write("")

# -----------------------------
# Load meals from file
# -----------------------------
MEALS_FILE = "meals.json"

if not os.path.exists(MEALS_FILE):
    meals = {"cook": [], "order": []}
    with open(MEALS_FILE, "w") as f:
        json.dump(meals, f, indent=2)
else:
    with open(MEALS_FILE, "r") as f:
        meals = json.load(f)

cook_meals = meals.get("cook", [])
order_meals = meals.get("order", [])

# -----------------------------
# Protein selector
# -----------------------------
protein_choice = st.selectbox(
    "Choose a protein (optional)",
    ["Anything", "Chicken", "Beef", "Seafood", "Vegetarian"]
)

st.write("")

# -----------------------------
# Buttons with icons (same row)
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.image("drawings/dice.png", width=110)
    anything = st.button("Anything")

with col2:
    st.image("drawings/pan.png", width=110)
    cook = st.button("Let's Cook")

with col3:
    st.image("drawings/scooter.png", width=110)
    order = st.button("Let's Order")

# -----------------------------
# Meal selection logic
# -----------------------------
def pick_meal(meal_list, protein):
    if not meal_list:
        return None
    if protein == "Anything":
        return random.choice(meal_list)
    filtered = [m for m in meal_list if m["protein"] == protein]
    if filtered:
        return random.choice(filtered)
    return None

# -----------------------------
# Show result ABOVE add-meal
# -----------------------------
st.write("")

if anything:
    all_meals = cook_meals + order_meals
    meal = pick_meal(all_meals, protein_choice)
    if meal:
        st.success(f"✨ You should eat: **{meal['name']}**")
    else:
        st.warning("No meals match that protein yet!")

if cook:
    meal = pick_meal(cook_meals, protein_choice)
    if meal:
        st.success(f"🍳 Let's cook: **{meal['name']}**")
    else:
        st.warning("No cooking meals match that protein yet!")

if order:
    meal = pick_meal(order_meals, protein_choice)
    if meal:
        st.success(f"🛵 Let's order: **{meal['name']}**")
    else:
        st.warning("No ordering meals match that protein yet!")

# -----------------------------
# Add meal (dropdown)
# -----------------------------
with st.expander("➕ Add a meal"):
    with st.form("add_meal_form"):
        new_meal = st.text_input("Meal name")
        meal_type = st.selectbox("Type", ["Cook", "Order"])
        meal_protein = st.selectbox(
            "Protein",
            ["Anything", "Chicken", "Beef", "Seafood", "Vegetarian"]
        )
        submitted = st.form_submit_button("Add")

        if submitted and new_meal:
            entry = {"name": new_meal, "protein": meal_protein}

            if meal_type == "Cook":
                cook_meals.append(entry)
            else:
                order_meals.append(entry)

            with open(MEALS_FILE, "w") as f:
                json.dump(meals, f, indent=2)

            st.success("Meal added! 🎉")

# -----------------------------
# Footer
# -----------------------------
st.write("")
st.image("drawings/footer.png", width=200)
