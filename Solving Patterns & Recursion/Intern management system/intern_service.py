from database import connect

def add_intern(name, email, phone, department):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO interns (name, email, phone, department) VALUES (?, ?, ?, ?)",
        (name, email, phone, department)
    )

    conn.commit()
    conn.close()


def get_interns():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interns")
    interns = cursor.fetchall()

    conn.close()
    return interns


def search_intern(name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM interns WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    results = cursor.fetchall()
    conn.close()
    return results


def delete_intern(intern_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM interns WHERE id=?",
        (intern_id,)
    )

    conn.commit()
    conn.close()


def update_intern(intern_id, name, email, phone, department):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE interns
        SET name=?, email=?, phone=?, department=?
        WHERE id=?
        """,
        (name, email, phone, department, intern_id)
    )

    conn.commit()
    conn.close()


def search_by_department(department):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM interns WHERE department=?",
        (department,)
    )

    results = cursor.fetchall()
    conn.close()
    return results