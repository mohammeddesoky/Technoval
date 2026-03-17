# Intern Management System

## 📌 Overview

This project is a simple **Intern Management System** built using Python.
It allows users to manage interns efficiently through a clean user interface.

The system supports adding, viewing, searching, updating, and deleting interns.

---

## 🚀 Features

* Add new interns
* View all interns
* Search interns by name
* Update intern information
* Delete interns
* Simple UI built with Streamlit

---

## 🛠️ Technologies Used

* Python
* SQLite (Database)
* Streamlit (User Interface)

---

## 🏗️ System Design

The project follows a modular design:

* `database.py` → Handles database connection and table creation
* `intern_service.py` → Contains business logic (CRUD operations)
* `app.py` → Handles UI using Streamlit

---

## ⚡ Algorithm Optimization

A database **index** was added on the `department` column:

```sql
CREATE INDEX idx_department ON interns(department);
```

This improves performance when filtering or searching interns by department.

---

## 📊 Data Structures

* List → Used to store query results
* Tuple → Each intern record from the database

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install streamlit
```

### 2. Run the application

```bash
streamlit run app.py
```

---

## 💡 Example Usage

* Add an intern with name, email, phone, and department
* View all interns in a table
* Click **Edit** to update intern information
* Click **Delete** to remove an intern

---


