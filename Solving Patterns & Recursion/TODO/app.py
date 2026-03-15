import streamlit as st
from database import create_table
from task_service import add_task, get_tasks, complete_task, delete_task

create_table()

st.title("TODO Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Task", "View Tasks"]
)

if menu == "Add Task":

    st.subheader("Add New Task")

    task = st.text_input("Task name")

    if st.button("Add Task"):
        add_task(task)
        st.success("Task added successfully")

if menu == "View Tasks":

    st.subheader("Your Tasks")

    tasks = get_tasks()

    for task in tasks:

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.write(task[0])
        col2.write(task[1])
        col3.write(task[2])

        if col4.button("Complete", key=f"c{task[0]}"):
            complete_task(task[0])
            st.rerun()

        if col5.button("Delete", key=f"d{task[0]}"):
            delete_task(task[0])
            st.rerun()