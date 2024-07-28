from connect_to_db import connect_database

def update_member_age(member_id, new_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            query = "UPDATE members SET age =  %s WHERE id = %s"
            cursor.execute(query, (new_age, member_id))
            conn.commit()
            print("Customer age updated successfully!")

        finally:
            cursor.close()
            conn.close()

update_member_age(111, 18)