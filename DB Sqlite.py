import sqlite3
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Table created successfully")
    except sqlite3.Error as e:
        print(e)

def insert_data(conn, user):
    insert_sql = '''
    INSERT INTO users (name, email)
    VALUES (?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(insert_sql, user)
        conn.commit()
        print("Inserted data successfully")
    except sqlite3.Error as e:
        print(e)

def query_data(conn):
    query_sql = 'SELECT * FROM users'
    try:
        cursor = conn.cursor()
        cursor.execute(query_sql)
        rows = cursor.fetchall()
        print("Queried data successfully")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def update_data(conn, user):
    update_sql = '''
    UPDATE users
    SET email = ?
    WHERE name = ?
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(update_sql, user)
        conn.commit()
        print("Updated data successfully")
    except sqlite3.Error as e:
        print(e)

def delete_data(conn, user_name):
    delete_sql = '''
    DELETE FROM users
    WHERE name = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(delete_sql, (user_name))
        conn.commit()
        print("Deleted data successfully")
    except sqlite3.Error as e:
        print(e)

def main():
    database = 'example.db'

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        create_table(conn)

        insert_data(conn, ('Alice', 'alice@example.com'))
        insert_data(conn, ('Bob', 'bob@example.com'))

        query_data(conn)

        update_data(conn, ('alice_new@example.com', 'Alice'))

        query_data(conn)

        # delete_data(conn, 'Bob')

        query_data(conn)

        # close the connection
        conn.close()
        print("Connection closed")
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
