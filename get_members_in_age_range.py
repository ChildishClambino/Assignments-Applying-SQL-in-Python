from connect_to_db import connect_database

def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM members WHERE age BETWEEN %s AND %s"
            cursor.execute(query, (start_age, end_age))

            for row in cursor.fetchall():
                print(row)
        finally:
            cursor.close()
            conn.close()

get_members_in_age_range(25, 30)

