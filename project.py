# BMI Calculator

import streamlit as st
import time

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Main Title
st.title("⚖️ BMI Calculator In Python")

# Section Header
st.header("🏋️‍♂️ Calculate Your Body Mass Index")

# Subheading for Input Section
st.subheader("🔢 Enter Your Weight and Height to Check Your BMI 📊")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("⚖️ Weight (kg): ", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("📏 Height (m): ", min_value=1.0, format="%.2f")

# BMI Calculation & Display
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)  # BMI Formula

    # Subheading for BMI Result
    st.subheader("📊 Your BMI Is:")
    st.markdown(f"**{bmi:.2f}**", unsafe_allow_html=True)

    # Categorization Based on BMI
    st.subheader("📌 BMI Category:")
    if bmi < 18.5:
        st.error("🏋️‍♂️ You are underweight 🍽️ (Consider a balanced diet)")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ You are normal weight 💪 (Keep it up!)")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ You are overweight 🏃‍♂️ (Try to stay active)")
    else:
        st.error("🚨 You are obese 🥗 (Consider healthier food choices)")
else:
    st.error("⚠️ Please enter a valid weight and height")
