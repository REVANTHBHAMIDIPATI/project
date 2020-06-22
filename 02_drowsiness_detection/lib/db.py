import sqlite3 as lite

# connect to the database
def connect(database_name):
    try:
        conn = lite.connect(database_name)
        return conn
    except lite.Error as e:
        print("Some error - " + e)

# To execute sql query
def execute(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except lite.Error as e:
        print("Some error - " , e)
# insert one record into table
def insert(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit() # commit will save the data
    except lite.Error as e:
        print("Some error - ", e)
# fetch all records from table
def fetchall(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except lite.Error as e:
        print("Some error - " , e)

# fetch one record from table
def fetchone(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except lite.Error as e:
        print("Some error - ", e)
# update one record in the table
def update(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except lite.Error as e:
        print("Some error - " , e)

# delete one record from table
def delete(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except lite.Error as e:
        print("Some error - " , e)

# close the connection
def close(conn):
    conn.close()
