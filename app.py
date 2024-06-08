import streamlit as st
import pandas as pd
import plotly.express as px
from firebase_auth import sign_up
from meal_planner import calculate_calories, get_meal_plan
from database import insert_user_profile, get_user_profile, insert_meal_plan, get_meal_plans, insert_feedback, insert_rating_comment, get_ratings_comments

def main():
    st.title("Cloud-based Meal Planning")

    menu = ["Home", "SignUp", "Login", "Profile", "Meal Plan", "Feedback"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to the Meal Planning App")

    elif choice == "SignUp":
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        if st.button("Sign Up"):
            user = sign_up(email, password)
            st.success("You have successfully created an account")
            st.write(user)

    elif choice == "Profile":
        user_id = st.text_input("User ID")
        name = st.text_input("Name")
        age = st.number_input("Age", 0, 100)
        height = st.number_input("Height (cm)", 0, 250)
        weight = st.number_input("Weight (kg)", 0, 200)
        dietary_constraints = st.multiselect("Dietary Constraints", ["Gluten-Free", "Dairy-Free", "Nut-Free"])
        
        if st.button("Save Profile"):
            profile_data = {
                "user_id": user_id,
                "name": name,
                "age": age,
                "height": height,
                "weight": weight,
                "dietary_constraints": dietary_constraints
            }
            insert_user_profile(profile_data)
            st.success("Profile saved successfully")

    elif choice == "Meal Plan":
        age = st.number_input("Age", 0, 100)
        height = st.number_input("Height (cm)", 0, 250)
        weight = st.number_input("Weight (kg)", 0, 200)
        exercise_level = st.selectbox("Exercise Level", ["Low", "Medium", "High"])
        goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain", "Healthy Diet"])
        diet_type = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian"])
        dietary_constraints = st.multiselect("Dietary Constraints", ["Gluten-Free", "Dairy-Free", "Nut-Free"])

        if st.button("Generate Meal Plan"):
            calories = calculate_calories(age, height, weight, exercise_level, goal)
            meal_plan = get_meal_plan(calories, diet_type, dietary_constraints)
            insert_meal_plan(meal_plan)
            st.write(meal_plan)

        st.subheader("Rate & Comment on Meal Plans")
        meal_plan_id = st.text_input("Meal Plan ID")
        user_id = st.text_input("User ID")
        rating = st.slider("Rating", 1, 5)
        comment = st.text_area("Comment")
        
        if st.button("Submit"):
            insert_rating_comment(meal_plan_id, user_id, rating, comment)
            st.success("Thank you for your feedback")

    elif choice == "Feedback":
        feedback = st.text_area("Your Feedback")
        if st.button("Submit"):
            insert_feedback({"feedback": feedback})
            st.success("Thank you for your feedback")

        st.subheader("Feedback Visualization")
        ratings_data = list(get_ratings_comments())
        if ratings_data:
            df = pd.DataFrame(ratings_data)
            avg_ratings = df.groupby('meal_plan_id')['rating'].mean().reset_index()
            fig = px.bar(avg_ratings, x='meal_plan_id', y='rating', title="Average Ratings per Meal Plan")
            st.plotly_chart(fig)

if __name__ == '__main__':
    main()
