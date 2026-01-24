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
# Header (centered & smaller)
# -----------------------------
st.image("drawings/header.png", width=260)
st.write("")

# -----------------------------
# Load meals
# -----------------------------
MEALS_FILE = "meals.json"

with open(MEALS_FILE, "r") as f:
    meals = json.load(f)

cook_meals = meals["cook"]
order_meals = meals["order"]
late_night_meals = meals["late_night"]

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
col1, col2, col3, col4 = st.columns(4)

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

# -----------------------------
# Meal picker
# -----------------------------
def pick_meal(meal_list, protein):
    if protein == "Anything":
        return random.choice(meal_list)
    filtered = [m for m in meal_list if m["protein"] == protein]
    if filtered:
        return random.choice(filtered)
    return None

# -----------------------------
# Show result
# -----------------------------
st.write("")

if anything:
    all_meals = cook_meals + order_meals + late_night_meals
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

# -----------------------------
# Add meal (dropdown style)
# -----------------------------
with st.expander("➕ Add a meal"):
    with st.form("add_meal_form"):
        new_meal = st.text_input("Meal name")

        meal_type = st.selectbox(
            "Type",
            ["Cook", "Order", "Late Night"]
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
            else:
                late_night_meals.append(entry)

            with open(MEALS_FILE, "w") as f:
                json.dump(meals, f, indent=2)

            st.success("Meal added! 🎉")

# -----------------------------
# Footer
# -----------------------------
st.write("")
st.image("drawings/footer.png", width=200)
