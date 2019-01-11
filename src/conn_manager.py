import urllib3
import certifi
from bs4 import BeautifulSoup

from http.client import responses

from storage import db

import time

#
# Module which manages HTTP connections between this application and the venue
# websites
# 
class ConnManager():

    #
    # init function
    #
    def __init__(self):
        self._http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                                         ca_certs=certifi.where())
        
    #
    # return the beautiful soup object containing the info from the events
    # page
    #
    # params:
    # events page:  events page URL for venue
    # venue:  object containing venue name
    #
    def get(self, events_page, venue):

        soup = None

        r = self._http.request('GET', events_page)
        status = r.status
        attempt_time = int(time.time())
        connection_success = False
        if (r.status is not 200):
            # Store response in error table if HTTP reply status is not OK
            db.get_error_table().add_entry(venue.get_name(), "",
                str(r.status) + ": " + responses[r.status])
        else:
            connection_success = True
            soup = BeautifulSoup(r.data, 'html.parser')
        r.release_conn()

        # Store last connection info in venue table
        db.get_venue_table().add_entry(venue.get_name(), attempt_time,
                                       connection_success)
        return soup
        
