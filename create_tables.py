import psycopg2
from sql_queries import create_table_queries,drop_table_queries

def create_database():
    try:
        conn=psycopg2.connect("host=127.0.0.1 dbname=studentdb user=postgres password=qwerty12345")
    except psycopg2.Error as e:
        print("Error: Unable to connect to db")
        print(e) 

    try:
        cur=conn.cursor()
    except psycopg2.Error as e:
        print("Error: Unable to get cursor to db")
        print(e)

    conn.set_session(autocommit=True) 

    try:
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    except psycopg2.Error as e:
        print("Error: Could not drop Database")
        print(e)   

    try:
        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    except psycopg2.Error as e:
        print("Error: Could not create Database")
        print(e)

    conn.close()

    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=qwerty12345")
    except psycopg2.Error as e:
        print("Error: Could not make connection to the database")
        print(e)

    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: Could not get cursor to the Database")
        print(e)
    
    return cur, conn

def drop_tables(cur,conn):
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Could not drop table from query: {}".format(query))
            print(e)

def create_tables(cur, conn):
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Could not create table from query: {}".format(query))
            print(e)

        


def main():
    cur,conn=create_database()
    drop_tables(cur,conn)
    create_tables(cur,conn)
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()