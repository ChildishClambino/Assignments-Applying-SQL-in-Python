from connect_to_db import connect_database


def delete_workout_session(session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor= conn.cursor()         
            query = "DELETE FROM workoutsessions WHERE session_id = %s"
            cursor.execute(query, (session_id,))
            conn.commit()
            print("Session successfully deleted")
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

delete_workout_session(1)