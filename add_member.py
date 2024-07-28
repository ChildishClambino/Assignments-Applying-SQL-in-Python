from connect_to_db import connect_database
    

def add_member(id, name, age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_member = (id, name, age)

            query = "INSERT INTO members(id, name, age) VALUES (%s, %s, %s)"

            cursor.execute(query, new_member)
            conn.commit()
            print("New member added successfully")

        finally:
            cursor.close()
            conn.close()

add_member(765, "Jacob Sans", 26)
