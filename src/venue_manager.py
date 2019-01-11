#
# Module which manages scraping from all venues
#

from conn_manager import ConnManager

from bus.venues.bluebird_theater import BluebirdTheater
from bus.venues.gothic_theatre import GothicTheatre

conn_manager = None

#
# get events from all venues
#
# return:  events in list format
#
def get_events():

    events = []

    global conn_manager
    if(conn_manager is None):
        conn_manager = ConnManager()

    bluebird_theater = BluebirdTheater(conn_manager)
    events.extend(bluebird_theater.get_events())
    gothic_theatre = GothicTheatre(conn_manager)
    events.extend(gothic_theatre.get_events())

    return events
