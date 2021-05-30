import sqlite3

con = sqlite3.connect("todo_db.db")


def create_table():
    global con
    try:
        con.execute('''CREATE TABLE TASKS
             (ID INTEGER PRIMARY KEY,
             USERID INTEGER NOT NULL,
             TITLE           TEXT    NOT NULL,
             CATEGORY           TEXT    NOT NULL,
             DESC           TEXT    NOT NULL,
             IS_COMPLETE            INT     NOT NULL);''')
        con.execute('''CREATE TABLE USERS
             (ID INTEGER PRIMARY KEY,
             NAME           TEXT    NOT NULL,
             USERNAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             BLOOD        CHAR(50)      NOT NULL,
             PASSWORD         CHAR(50)     NOT NULL);''')
    except Exception:
        print("")


def register(name, username, blood, age, password):
    global con
    con.execute("INSERT INTO USERS (NAME,USERNAME,AGE,BLOOD,PASSWORD) \
          VALUES (?,?,?,?,?)", (name, username, age, blood, password))
    con.commit()


def login(username, password):
    global con
    cursor = con.execute("SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD=?", (username, password))
    for row in cursor:
        return row[0]
    else:
        return -1


def get_name(uid):
    global con
    cursor = con.execute("SELECT NAME FROM USERS WHERE ID=?", (uid,))
    for row in cursor:
        return row[0]


def add_task(title, category, desc, is_complete, uid):
    global con
    con.execute("INSERT INTO TASKS (TITLE,CATEGORY,DESC,IS_COMPLETE,USERID) VALUES (?,?,?,?,?)",
                (title, category, desc, is_complete,uid))
    con.commit()


def get_all_task(uid):
    global con
    cursor = con.execute("SELECT * FROM TASKS WHERE USERID=?", (uid,))
    return cursor


def get_task(task_id):
    global con
    cursor = con.execute("SELECT * FROM TASKS WHERE ID=?", (task_id,))
    return cursor


def delete_task(task_id):
    global con
    con.execute("DELETE FROM TASKS WHERE ID=?", (task_id,))
    con.commit()
    if con.total_changes > 0:
        return True
    else:
        return False


def update_task(task_id, title, category, desc, is_complete):
    global con
    con.execute("UPDATE TASKS SET TITLE=?, CATEGORY=?, DESC=?, IS_COMPLETE=? WHERE ID=?",
                (title, category, desc, is_complete, task_id))
    con.commit()
    if con.total_changes > 0:
        return True
    else:
        return False
