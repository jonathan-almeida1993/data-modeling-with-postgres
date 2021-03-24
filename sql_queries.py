# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS
    songplays (songplay_id SERIAL PRIMARY KEY,
        start_time BIGINT,
        user_id INTEGER REFERENCES users (user_id),
        level VARCHAR,
        song_id VARCHAR REFERENCES songs (song_id),
        artist_id VARCHAR REFERENCES artists (artist_id),
        session_id INTEGER,
        location VARCHAR,
        user_agent VARCHAR
    );
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS
    users (id SERIAL PRIMARY KEY,
        user_id INTEGER,
        first_name VARCHAR,
        last_name VARCHAR,
        gender CHAR(1),
        level VARCHAR,
        UNIQUE (user_id)
    );
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS
    songs (id SERIAL PRIMARY KEY,
        song_id VARCHAR,
        title VARCHAR,
        artist_id VARCHAR,
        year INTEGER,
        duration NUMERIC,
        UNIQUE (song_id)
    );
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS
    artists (id SERIAL PRIMARY KEY,
        artist_id VARCHAR,
        name VARCHAR,
        location VARCHAR,
        latitude REAL,
        longitude REAL,
        UNIQUE (artist_id)
    );
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS
    time (id SERIAL PRIMARY KEY,
        start_time BIGINT,
        hour SMALLINT,
        day SMALLINT,
        week SMALLINT,
        month SMALLINT,
        year SMALLINT,
        weekday SMALLINT,
        UNIQUE (start_time)
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO
    songplays (start_time, user_id, level, song_id, artist_id,
    session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO
    users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO
    songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO
    artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id)
DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO
    time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time)
DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, s.artist_id
FROM songs s
JOIN artists a ON s.artist_id=a.artist_id
WHERE s.title=%s and a.name=%s and s.duration=%s ; 
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create,
                        time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
