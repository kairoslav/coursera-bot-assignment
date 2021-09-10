import sqlite3

conn = sqlite3.connect('/home/svt/PycharmProjects/coursera-bot-assignment/utils/db_api/database.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS User(user_id INT PRIMARY KEY)")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Place(
    place_id INT PRIMARY KEY,
    name TEXT,
    longitude REAL,
    latitude REAL)
    """)
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS User_Place(
    user_id INT,
    place_id INT,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES Place(place_id) ON DELETE CASCADE
    )
""")
