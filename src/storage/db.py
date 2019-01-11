import sqlite3
from sqlite3 import Error

from storage.error_table import ErrorTable
from storage.venue_table import VenueTable
from storage.event_table import EventTable

DB_FILENAME="events-calendar.db"

error_table=None
venue_table=None
event_table=None

def connect():

    try:
        conn = sqlite3.connect(DB_FILENAME)
    except Error as e:
        print(e)
        conn = None
    return conn

def get_error_table():
    global error_table
    if error_table is None:
        error_table = ErrorTable()
    return error_table
    
def get_venue_table():
    global venue_table
    if venue_table is None:
        venue_table = VenueTable()
    return venue_table

def get_event_table():
    global event_table
    if event_table is None:
        event_table = EventTable()
    return event_table
