import mysql.connector


def db_connection(host, user, password):
    database = mysql.connector.connect(host=host, user=user, password=password, database="taskyy")
    return database


def get_todos(database):
    cursor = database.cursor()
    cursor.execute('SELECT * FROM Todo')
    todo_id, name, status = 0, '', ''

    records = cursor.fetchall()
    print('Total number of rows in table: ', cursor.rowcount)
    for row in records:
        todo_id = row[0]
        name = row[1]
        status = row[2]
    return todo_id, name, status

