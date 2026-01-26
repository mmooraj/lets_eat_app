import streamlit as st
import json
import random
import os

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="Let's Eat",
    layout="centered"
)

# -----------------------
# Helpers
# -----------------------
def safe_image(path, width=80):
    if os.path.exists(path):
        st.image(path, width=width)

def load_meals():
    with open("meals.json", "r") as f:
        return json.load(f)

def save_meals(data):
    with open("meals.json", "w") as f:
        json.dump(data, f, indent=2)

# -----------------------
# Load data
# -----------------------
meals = load_meals()

# -----------------------
# Title
# -----------------------
st.title("Let’s Eat 🍽️")

# -----------------------
# Protein selector
# -----------------------
protein = st.selectbox(
    "Choose a protein (optional)",
    ["Anything", "Chicken", "Beef", "Seafood", "Vegetarian"]
)

st.markdown("---")

# -----------------------
# Choice buttons (OLD VERSION)
# -----------------------
choice = None

safe_image("icons/dice.png")
if st.button("Anything"):
    choice = "anything"

safe_image("icons/pan.png")
if st.button("Let's Cook"):
    choice = "cook"

safe_image("icons/scooter.png")
if st.button("Let's Order"):
    choice = "order"

safe_image("icons/late_night.png")
if st.button("Late Night"):
    choice = "late_night"

# -----------------------
# Pick a meal
# -----------------------
if choice:
    options = meals.get(choice, [])

    if protein != "Anything":
        options = [
            m for m in options
            if protein.lower() in m.lower()
        ]

    if options:
        st.success(f"✨ You should eat: **{random.choice(options)}**")
    else:
        st.warning("No meals match that yet — add one below 👇")

# -----------------------
# Add a meal
# -----------------------
with st.expander("➕ Add a meal"):
    meal_name = st.text_input("Meal name")

    category = st.selectbox(
        "Category",
        ["anything", "cook", "order", "late_night"]
    )

    if st.button("Add meal"):
        if meal_name:
            meals[category].append(meal_name)
            save_meals(meals)
            st.success("Added! 🍽️")
        else:
            st.error("Please enter a meal name")
