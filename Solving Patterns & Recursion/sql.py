import sqlite3

# connect to database
conn = sqlite3.connect("Company.db")
cursor = conn.cursor()

# create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments(
    department_id INTEGER PRIMARY KEY,
    department_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees(
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary REAL,
    department_id INTEGER,
    FOREIGN KEY(department_id) REFERENCES Departments(department_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Projects(
    project_id INTEGER PRIMARY KEY,
    project_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee_Project(
    employee_id INTEGER,
    project_id INTEGER,
    PRIMARY KEY(employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
)
""")

# insert departments
departments = [
    (1, "HR"),
    (2, "Engineering"),
    (3, "Marketing")
]

cursor.executemany(
    "INSERT INTO Departments VALUES (?, ?)", departments
)

# insert employees
employees = [
    (1, "Mohamed", 30, 5000, 2),
    (2, "Ahmed", 28, 4500, 2),
    (3, "Ali", 35, 4000, 1),
    (4, "Adam", 29, 4200, 3)
]

cursor.executemany(
    "INSERT INTO Employees VALUES (?, ?, ?, ?, ?)", employees
)

# insert projects
projects = [
    (1, "Website"),
    (2, "Mobile App"),
    (3, "Marketing Campaign")
]

cursor.executemany(
    "INSERT INTO Projects VALUES (?, ?)", projects
)

# employee-project relations
employee_projects = [
    (1,1),
    (1,2),
    (2,1),
    (3,3),
    (4,3)
]

cursor.executemany(
    "INSERT INTO Employee_Project VALUES (?, ?)", employee_projects
)

conn.commit()