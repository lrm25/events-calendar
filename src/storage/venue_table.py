import sqlite3
from storage import db
from storage.db_table import DbTable

import time

class VenueTable(DbTable):

    def __init__(self):
        create_query = """ CREATE TABLE IF NOT EXISTS venues (
                id integer PRIMARY KEY,
                venue text NOT NULL,
                last_attempt integer NOT NULL,
                success_attempt integer NOT NULL
            );"""
        super().__init__(create_query)

    def add_entry(self, venue, connection_time, was_success):
        self.create()
        conn = db.connect()
        c = conn.cursor()

        c.execute("""SELECT * FROM venues where venue=?""", (venue,))
        if c.fetchone() is None:
            if was_success:
                c.execute("""INSERT INTO venues (venue, last_attempt,
                             success_attempt) VALUES (?, ?, ?)""",
                             (venue, connection_time, connection_time))     
            else:
                c.execute("""INSERT INTO venues (venue, last_attempt)
                             VALUES (?, ?)""", (venue, connection_time))
        else:
            if was_success:
                c.execute("""UPDATE venues SET last_attempt=?,
                             success_attempt=?
                             WHERE venue=?""",
                             (connection_time, connection_time, venue))
            else:
                c.execute("""UPDATE venues SET last_attempt=?
                             WHERE venue=?""", (connection_time, venue))
        conn.commit()
        conn.close()
