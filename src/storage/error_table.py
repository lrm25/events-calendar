import sqlite3
from storage import db
from storage.db_table import DbTable

import time

class ErrorTable(DbTable):
    
    def __init__(self):
        create_query = """ CREATE TABLE IF NOT EXISTS errors (
                id integer PRIMARY KEY,
                time integer NOT NULL,
                venue text NOT NULL,
                event text,
                description text
            );"""
        super().__init__(create_query)

    def add_entry(self, time, venue, event, description):
        self.create()
        conn = DB.connect()
        sql_add_entry = """INSERT INTO errors (time, venue, event,
            description) VALUES (?, ?, ?, ?)"""
        conn.execute(sql_add_entry, (time, venue, event, description))
        conn.commit()
        conn.close()
        
