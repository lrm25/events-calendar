from bs4 import BeautifulSoup

from abc import ABC, abstractmethod

#
# Abstract base class representing venue
#
class Venue(ABC):

    #
    # init function
    #
    # params:
    # name:  name of venue
    # home_line:  venue's homepage URL
    # event_link:  venue's event page URL
    # conn_manager:  connection manager to handle comms between this object
    #   and the venue website
    #
    def __init__(self, name, home_link, event_link, conn_manager):
        self._name = name
        self._home_link = home_link
        self._event_link = event_link
        self._conn_manager = conn_manager

    #
    # get venue's scheduled events
    # return:  list of events objects containing events data
    #
    def get_events(self):
        self._soup = self._conn_manager.get(self._event_link, self)
        if (self._soup is not None):
            self._events = self.retrieve_events()
        else:
            self._events = []
        return self._events
        # TODO retrieve events
        # TODO check for duplicates (using ID)
        # TODO check for missing events
        
    #
    # get URL for venue's event page
    #
    def get_event_link(self):
        return self._event_link

    #
    # get URL for venue's home page
    #
    def get_home_link(self):
        return self._home_link

    #
    # get venue's common name
    #
    def get_name(self):
        return self._name

    #
    # Parse soup object into local events object
    #
    @abstractmethod
    def retrieve_events(self):
        pass
