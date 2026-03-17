import streamlit as st
from database import create_table
from intern_service import *

create_table()

if "page" not in st.session_state:
    st.session_state.page = "main"

# update intern
def update_intern_page(intern):

    st.subheader("Update Intern")

    selected_id = intern[0]
    id = st.text_input("ID", value=intern[0], disabled=True)
    name = st.text_input("New Name", value=intern[1])
    email = st.text_input("New Email", value=intern[2])
    phone = st.text_input("New Phone", value=intern[3])

    department_options = ["IT", "HR", "Marketing", "Finance"]
    department = st.selectbox(
        "New Department",
        department_options,
        index=department_options.index(intern[4])
    )

    if st.button("Update"):
        update_intern(selected_id, name, email, phone, department)
        st.success("Intern updated successfully")
        st.session_state.page = "main"
        st.rerun()


if st.session_state.page == "edit":
    update_intern_page(st.session_state.edit_intern)

    if st.button("Back"):
        st.session_state.page = "main"
        st.rerun()

    st.stop()



st.title("Intern Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Intern", "View & Edit Interns", "Search Intern"]
)

# add intern
if menu == "Add Intern":

    st.subheader("Add New Intern")

    name = st.text_input("Name", key="name", value="")
    email = st.text_input("Email", key="email", value="")
    phone = st.text_input("Phone", key="phone", value="")
    department = st.selectbox(
        "Department",
        ["IT", "HR", "Marketing", "Finance"]
    )

    if st.button("Add"):
        add_intern(name, email, phone, department)
        st.success("Intern added successfully")

# view interns
elif menu == "View & Edit Interns":

    st.subheader("All Interns")

    interns = get_interns()

    for intern in interns:

        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

        col1.write(intern[0])
        col2.write(intern[1])
        col3.write(intern[2])
        col4.write(intern[3])
        col5.write(intern[4])


        if col6.button("Edit", key=f"e{intern[0]}"):
            st.session_state.edit_intern = intern
            st.session_state.page = "edit"
            st.rerun()


        if col7.button("Delete", key=f"d{intern[0]}"):
            delete_intern(intern[0])
            st.rerun()


# search intern
elif menu == "Search Intern":

    st.subheader("Search Intern")

    search_type = st.radio(
        "Search By",
        ["Name", "Department"]
    )

    if search_type == "Name":

        search = st.text_input("Enter name")

        if st.button("Search"):
            results = search_intern(search)

            st.dataframe(results)

    elif search_type == "Department":

        department = st.selectbox(
            "Select Department",
            ["IT", "HR", "Marketing", "Finance"]
        )

        if st.button("Search"):
            results = search_by_department(department)

            st.dataframe(results)
