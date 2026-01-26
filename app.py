import streamlit as st
import json
import random
import os

# -----------------------
# Page config (mobile first)
# -----------------------
st.set_page_config(
    page_title="Let's Eat",
    layout="centered"
)

# -----------------------
# Helpers
# -----------------------
def safe_image(path, width=90):
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
st.markdown(
    "<h2 style='text-align:center;'>Let’s Eat ✨</h2>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------
# Protein selector
# -----------------------
protein = st.selectbox(
    "Choose a protein (optional)",
    ["Anything", "Chicken", "Beef", "Seafood", "Vegetarian"]
)

# -----------------------
# Centered 2x2 grid
# -----------------------
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

choice = None

with col1:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    safe_image("drawings/dice.png")
    if st.button("Anything"):
        choice = "anything"
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    safe_image("drawings/pan.png")
    if st.button("Let's Cook"):
        choice = "cook"
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    safe_image("drawings/scooter.png")
    if st.button("Let's Order"):
        choice = "order"
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    safe_image("drawings/late.png")
    if st.button("Late Night"):
        choice = "late_night"
    st.markdown("</div>", unsafe_allow_html=True)

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
