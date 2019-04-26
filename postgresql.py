import psycopg2


def connect():
    connection = psycopg2.connect(user="msobiczewski",
                                  password="msobiczewski",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="nozbe")
    return connection


def execute(connection, sql_stmt):
    cursor = connection.cursor()
    cursor.execute(sql_stmt)
    record = cursor.fetchone()
    return record


def insert(connection, sql_stmt):
    cursor = connection.cursor()
    cursor.execute(sql_stmt)
    connection.commit()


def close_conn(connection):
    # closing database connection.
    if (connection):
        connection.close()
        print("PostgreSQL connection is closed")