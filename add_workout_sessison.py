from connect_to_db import connect_database


def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "INSERT INTO workoutsessions (member_id, date, duration_minutes, calories_burned) VALUES(%s, %s, %s,%s)"
            cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
            conn.commit()
            print("Workout added successfully")

        finally:
            cursor.close()
            conn.close()

add_workout_session(111, '2024-02-15', 45, 200)