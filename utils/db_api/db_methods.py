import sqlite3
from my_types import User, Place

conn = sqlite3.connect('/home/svt/PycharmProjects/coursera-bot-assignment/utils/db_api/database.db')
cursor = conn.cursor()


def _insert(table: str, column_values: dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ', '.join('?' * len(column_values.keys()))
    cursor.executemany(
        f"INSERT OR IGNORE INTO {table} "
        f"({columns})"
        f"VALUES ({placeholders})",
        values
    )
    conn.commit()


def add_user(user: User):
    _insert("User", {"user_id": user.user_id})
    # cursor.execute(
    #     f"INSERT OR IGNORE INTO User"
    #     f"(user_id) VALUES ({user.user_id})"
    # )


def add_place_for_user(user: User, place: Place):
    _insert("Place", {
        "place_id": place.place_id,
        "name": place.name,
        "latitude": place.latitude,
        "longitude": place.longitude
    })
    _insert("User_Place", {
        "user_id": user.user_id,
        "place_id": place.place_id
    })


def get_user_places(user_id: int):
    cursor.execute(f"""
        SELECT UP.place_id, name, longitude, latitude  FROM Place 
            JOIN User_Place UP on Place.place_id = UP.place_id
            JOIN User U on UP.user_id = U.user_id
            WHERE U.user_id = {user_id}
    """)
    return cursor.fetchall()


def delete_user_places(user_id: int):
    cursor.execute(f"""
        DELETE FROM Place 
        WHERE place_id IN (SELECT User_Place.place_id from User_Place WHERE user_id = {user_id})
    """)
    conn.commit()
    cursor.execute(f"""
            DELETE FROM User_Place WHERE user_id={user_id}
        """)
    conn.commit()


def get_last_place_id():
    cursor.execute("SELECT max(place_id) from Place")
    return cursor.fetchone()[0] or 0


if __name__ == "__main__":
    pass
    # DROP ALL TABLES
    # cursor.execute("DROP TABLE User_Place;")
    # conn.commit()
    # cursor.execute("DROP TABLE User;")
    # conn.commit()
    # cursor.execute("DROP TABLE Place")
    # conn.commit()
    # user = User(1)
    # add_user(user)
