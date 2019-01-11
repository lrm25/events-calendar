#
# Object containing event info
# NOTE:  many of the parameters are optional
#
class Event:
    
    #
    # init function
    #
    # params:
    # name:  official name of event
    # date:  duh
    # time:  time that show or event starts (not door time)
    # info:  any additional info about the event (e.g. other bands)
    #
    def __init__(self, name, date, time, info):
        self._name = name
        self._date = date
        self._time = time
        self._info = info
        self._id = None
        
    def get_date(self):
        return self._date
    def set_date(self, date):
        self._date = date

    def get_show_time(self):
        return self._time
    def set_show_time(self, time):
        self._time = time

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_info(self):
        return self._info
    def set_info(self, info):
        self._info = info

    # Id used to differentiate venue's events from one another
    # can be any form of ID (venue site provided ID, string, etc.)
    def get_id(self):
        return self._id
    def set_id(self, id_):
        self._id = id_

    # Link for this specific event, if it exists
    def get_link(self):
        return self._link
    def set_link(self, link):
        self._link = link

    # Ages allowed at the event
    def set_ages(self, ages):
        self._ages = ages
    def get_ages(self):
        return self._ages

    # Event price
    # TODO:  separate into early, day-of
    def set_price(self, price):
        self._price = price
    def get_price(self):
        return self._price

    # Day of show price
    def set_dos_price(self, dos_price):
        self._dos_price = dos_price
    def get_dos_price(self):
        return _dos_price

    # Time that doors open
    def set_doors_time(self, doors_time):
        self._doors_time = doors_time
    def get_doors_time(self):
        return _doors_time
