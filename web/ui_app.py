"""

Streamlit UI for the Student Performance Factor prediction demo.
Users enter study factors; the app then sends them to the FastAPI backend at http://127.0.0.1:8000/predict .
It then displays the predicted exam score with appropriate messages.

Many thanks to Mr. Savio Saldanha, who demoed a web application and shared code during Office Hours for the UC Berkeley AI & ML Certification Course, on February 16, 2026.

On March 24, 2026 Mr. Ninad Patil modified it to for his capstone project Student Performance Factor.

Please ensure you have streamlit; otherwise run `%pip install streamlit` to resolve depndencies

To run this Streamlit app, execute:
streamlit run ui_app.py

"""

import streamlit as st
import requests

st.set_page_config(
    page_title="Student Performance Factor Prediction",
    page_icon="📊",
    layout="wide"
)

# def pretty(label: str) -> str:
#     return label.replace("_", " ").title()

# def number_input_hidden(label, **kwargs):
#     st.caption(pretty(label))
#     return st.number_input(label, label_visibility="collapsed", **kwargs)

# def selectbox_hidden(label, options, index=0):
#     st.caption(pretty(label))
#     return st.selectbox(label, options, index=index, label_visibility="collapsed")

def pretty(label: str) -> str:
    return label.replace("_", " ").title()

def label_bold(label: str):
    st.markdown(f"**{pretty(label)}**")

def number_input_hidden(label, **kwargs):
    label_bold(label)
    return st.number_input(label, label_visibility="collapsed", **kwargs)

def selectbox_hidden(label, options, index=0):
    label_bold(label)
    return st.selectbox(label, options, index=index, label_visibility="collapsed")

st.title("Student Performance Factor Prediction")
st.write("Enter student details below to estimate predicted exam performance.")

with st.form("prediction_form"):
    st.subheader("Academic & Study Habits")
    c1, c2 = st.columns(2)
    with c1:
        attendance = number_input_hidden("attendance", min_value=0, value=63, step=1)
        hours_studied = number_input_hidden("hours_studied", min_value=0, value=21, step=1)
        previous_scores = number_input_hidden("previous_scores", min_value=0, value=72, step=1)
        tutoring_sessions = number_input_hidden("tutoring_sessions", min_value=0, value=2, step=1)
    with c2:
        sleep_hours = number_input_hidden("sleep_hours", min_value=4, value=7, step=1)
        physical_activity = number_input_hidden("physical_activity", min_value=0, value=1, step=1)
        motivation_level = selectbox_hidden("motivation_level", ["Medium", "High", "Low"], index=0)
        peer_influence = selectbox_hidden("peer_influence", ["Positive", "Neutral", "Negative"], index=0)

    st.subheader("Family & Resources")
    c3, c4 = st.columns(2)
    with c3:
        access_to_resources = selectbox_hidden("access_to_resources", ["Medium", "High", "Low"], index=0)
        parental_involvement = selectbox_hidden("parental_involvement", ["Medium", "High", "Low"], index=0)
        parental_education_level = selectbox_hidden(
            "parental_education_level", ["High School", "College", "Postgraduate", "Nan"], index=0
        )
    with c4:
        family_income = selectbox_hidden("family_income", ["Medium", "High", "Low"], index=0)
        internet_access = selectbox_hidden("internet_access", ["Yes", "No"], index=1)
        teacher_quality = selectbox_hidden("teacher_quality", ["Medium", "High", "Low"], index=0)

    st.subheader("School & Demographics")
    c5, c6 = st.columns(2)
    with c5:
        school_type = selectbox_hidden("school_type", ["Public", "Private"], index=0)
        learning_disabilities = selectbox_hidden("learning_disabilities", ["Yes", "No"], index=1)
        distance_from_home = selectbox_hidden("distance_from_home", ["Near", "Far", "Moderate", "NaN"], index=0)
    with c6:
        gender = selectbox_hidden("gender", ["Male", "Female"], index=0)
        extracurricular_activities = selectbox_hidden("extracurricular_activities", ["Yes", "No"], index=0)

    submitted = st.form_submit_button("Click to check your Predicted Exam Score", use_container_width=True)


if submitted:
    try:
        feature_dict = {
            "attendance": attendance,
            "hours_studied": hours_studied,
            "access_to_resources": access_to_resources,
            "previous_scores": previous_scores,
            "parental_involvement": parental_involvement,
            "tutoring_sessions": tutoring_sessions,
            "parental_education_level": parental_education_level,
            "physical_activity": physical_activity,
            "peer_influence": peer_influence,
            "sleep_hours": sleep_hours,
            "motivation_level": motivation_level,
            "internet_access": internet_access,
            "family_income": family_income,
            "teacher_quality": teacher_quality,
            "school_type": school_type,
            "learning_disabilities": learning_disabilities,
            "distance_from_home": distance_from_home,
            "gender": gender,
            "extracurricular_activities": extracurricular_activities,
        }

        # FastAPI endpoint expected to run locally; adjust if deployed elsewhere.
        url = "http://127.0.0.1:8000/predict"
        response = requests.post(url=url, json=feature_dict)
        print("Status:", response.status_code)
        print("Raw response:", response.text)
        
        if response.status_code != 200:
            st.error(f"API Error: {response.status_code}")
        else:
            output_dict = response.json()
            predicted_exam_score = output_dict.get('prediction')
            message = f"Based on the information provided, your predicted grade will be {predicted_exam_score:.2f}."
            if predicted_exam_score >= 50 and predicted_exam_score < 70:
                st.success(f"{message} You are on track to pass the exam!")
            elif predicted_exam_score >= 70 and predicted_exam_score < 85:
                st.success(f"{message} Keep up the good work!")
            elif predicted_exam_score >= 85 and predicted_exam_score < 100:
                st.success(f"{message} It's Outstanding! Keep it up! ")
            elif predicted_exam_score >= 100:
                st.success(f"You are Out of this World!")
            else:
                st.error(f"{message} Please consult with your teacher and consider additional support.")

    except Exception as e:
        # Surface any network/JSON issues to the user.
        st.error(f"Request failed: {e}")
