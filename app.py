# app.py

import streamlit as st
import json
import pandas as pd

from planner_engine import (
    allocate_days,
    generate_study_plan,
    carry_forward_tasks
)

st.set_page_config(page_title="AI Study Planner", layout="wide")
st.title("🎯 AI-Powered Personalized Study Plan Generator")


exam = st.selectbox(
    "Choose Competitive Exam",
    ["UPSC", "NEET", "JEE", "GATE", "SSC", "CAT"]
)

with open(f"syllabus/{exam.lower()}.json", "r", encoding="utf-8") as f:
    syllabus = json.load(f)


st.subheader("⏳ Preparation Timeline")

total_days = st.number_input(
    "Total Preparation Days",
    min_value=10,
    max_value=365,
    value=100
)

daily_hours = st.slider("Daily Study Hours", 1, 12, 6)
daily_questions = st.slider("Daily Question Practice Target", 10, 100, 20)
total_mocks = st.number_input("Total Mock Tests", 1, 50, 10)


st.subheader("📊 Subject-wise Self Assessment")

subject_levels = {}
for subject in syllabus.keys():
    subject_levels[subject] = st.selectbox(
        subject,
        ["Weak", "Medium", "Strong"]
    )


if st.button("🚀 Generate Study Plan"):

    allocation = allocate_days(total_days, subject_levels)

    plan = generate_study_plan(
        total_days=total_days,
        allocation=allocation,
        syllabus=syllabus,
        daily_questions=daily_questions,
        total_mocks=total_mocks
    )

    st.session_state.plan = plan
    st.success("Study plan generated successfully!")


if "plan" in st.session_state:
    st.subheader("📅 Complete Study Plan")
    df = pd.DataFrame(st.session_state.plan)
    st.dataframe(df, use_container_width=True)


if "plan" in st.session_state:
    st.subheader("✅ Daily Checklist & Progress Tracker")

    day_to_update = st.number_input(
        "Select Day to Update",
        min_value=1,
        max_value=total_days,
        value=1
    )

    today_tasks = [
        t for t in st.session_state.plan
        if t["Day"] == day_to_update
    ]

    incomplete_tasks = []

    for idx, task in enumerate(today_tasks):
        label = (
            f"{task['Subject']} | "
            f"{task['Major Topic']} → {task['Sub Topic']} | "
            f"{task['Task']}"
        )

        done = st.checkbox(
            label,
            value=task["Done"],
            key=f"{day_to_update}_{idx}"
        )

        if done:
            task["Done"] = True
        else:
            incomplete_tasks.append(task)

    if st.button("💾 Save Day Progress"):
        if incomplete_tasks:
            st.session_state.plan = carry_forward_tasks(
                st.session_state.plan,
                day_to_update,
                incomplete_tasks
            )
        st.success("Progress saved. Pending tasks moved to next day!")
