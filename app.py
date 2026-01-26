import streamlit as st
import json
import random
from datetime import datetime

# -----------------------------
# PAGE CONFIG (mobile-first)
# -----------------------------
st.set_page_config(
    page_title="Let's Eat!",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# MOBILE CENTERING CSS
# -----------------------------
st.markdown("""
<style>
/* Center the whole app like an iPhone screen */
.block-container {
    max-width: 390px;
    padding-top: 1.5rem;
    margin: auto;
}

/* Center buttons */
.stButton>button {
    width: 100%;
    border-radius: 18px;
    font-size: 16px;
    padding: 0.75rem;
}

/* Center images */
.icon {
    display: flex;
    justify-content: center;
    margin-bottom: 0.25rem;
}

/* Slight spacing between grid items */
.grid-item {
    margin-bottom: 1.25rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MEALS JSON
# -----------------------------
with open("meals.json", "r") as f:
    meals = json.load(f)

# -----------------------------
# TITLE
# -----------------------------
st.image("icons/logo.png", use_container_width=True)

st.write("")

# -----------------------------
# PROTEIN FILTER
# -----------------------------
protein = st.selectbox(
    "Choose a protein (optional)",
    ["Anything", "Chicken", "Beef", "Seafood", "Vegetarian"]
)

# -----------------------------
# HELPER FUNCTION
# -----------------------------
def get_random_meal(category):
    options = meals.get(category, [])
    if protein != "Anything":
        options = [
            m for m in options
            if protein.lower() in m.lower() or "vegetarian" in m.lower()
        ]
    return random.choice(options) if options else "No meals found"

# -----------------------------
# ICON GRID (2x2)
# -----------------------------
col1, col2 = st.columns(2)

# -------- TOP LEFT: ANYTHING --------
with col1:
    st.markdown('<div class="grid-item">', unsafe_allow_html=True)
    st.markdown('<div class="icon">', unsafe_allow_html=True)
    st.image("icons/dice.png", width=90)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Anything"):
        st.success(get_random_meal("cook"))
    st.markdown('</div>', unsafe_allow_html=True)

# -------- TOP RIGHT: COOK --------
with col2:
    st.markdown('<div class="grid-item">', unsafe_allow_html=True)
    st.markdown('<div class="icon">', unsafe_allow_html=True)
    st.image("icons/pan.png", width=90)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Let's Cook"):
        st.success(get_random_meal("cook"))
    st.markdown('</div>', unsafe_allow_html=True)

# -------- BOTTOM LEFT: ORDER --------
with col1:
    st.markdown('<div class="grid-item">', unsafe_allow_html=True)
    st.markdown('<div class="icon">', unsafe_allow_html=True)
    st.image("icons/scooter.png", width=90)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Let's Order"):
        st.success(get_random_meal("order"))
    st.markdown('</div>', unsafe_allow_html=True)

# -------- BOTTOM RIGHT: LATE NIGHT --------
with col2:
    st.markdown('<div class="grid-item">', unsafe_allow_html=True)
    st.markdown('<div class="icon">', unsafe_allow_html=True)
    st.image("icons/late_night.png", width=90)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Late Night"):
        st.success(get_random_meal("late_night"))
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# ADD A MEAL (PERSISTENT)
# -----------------------------
st.divider()
st.subheader("➕ Add a meal")

new_meal = st.text_input("Meal name")

meal_type = st.selectbox(
    "Category",
    ["cook", "order", "late_night"]
)

if st.button("Add meal"):
    if new_meal:
        meals.setdefault(meal_type, []).append(new_meal)

        with open("meals.json", "w") as f:
            json.dump(meals, f, indent=2)

        st.success(f"Added '{new_meal}' to {meal_type}")
    else:
        st.warning("Please enter a meal name")
