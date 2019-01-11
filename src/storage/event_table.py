import sqlite3
from storage import db
from storage.db_table import DbTable

import time

class EventTable(DbTable):

    def __init__(self):
        create_query = """ CREATE TABLE IF NOT EXISTS events (
            id integer PRIMARY KEY,
            event_id text,
            name text NOT NULL,
            event_time integer NOT NULL,
            event_link text NOT NULL,
            other_info text
        );"""
        super().__init__(create_query)

    def add_entry(self, event_id, name, event_time, event_link, other_info):
        self.create()
        conn = db.connect()
        c = conn.cursor()

        c.execute("""SELECT * FROM events where event_id=?""", (event_id,))
        if c.fetchone() is None:
            c.execute("""INSERT INTO events (event_id, name, event_time,
                         event_link, other_info) VALUES (?, ?, ?, ?, ?)""",
                         (event_id, name, event_time, event_link, other_info))
        else:
            c.execute("""UPDATE events SET name=?, event_time=?, event_link=?,
                         other_info=? WHERE event_id=?""",
                         (name, event_time, event_link, other_info, event_id))
        conn.commit()
        conn.close()
