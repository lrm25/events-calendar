# import libraries
import urllib3
from bs4 import BeautifulSoup
import re

from bus.venue import Venue
from bus.event import Event

NAME="Gothic Theatre"
HOME_LINK='https://www.gothictheatre.com'
EVENT_LINK='https://www.gothictheatre.com/events/all'
event_id_header='https://www.gothictheatre.com/events/detail/'

class GothicTheatre(Venue):

    def __init__(self, conn_manager):
        super().__init__(NAME, HOME_LINK, EVENT_LINK, conn_manager)

    def retrieve_events(self):

        event_list = []
        global event_id_header

        soup_events = self._soup.findAll('div', attrs={'class',"info"})
        for soup_event in soup_events:
            # Get name

            event_name_raw = soup_event.find('a', attrs={'title':"More Info"})
            event_link = event_name_raw['href']
            event_id = event_link[len(event_id_header):]
            event_name = event_name_raw.text.strip()
            #print("Name: \t\t%s" % (event_name))
            date_raw = soup_event.find('span', attrs={'class':'date'})
            date = date_raw.text.strip()
            #print("Date: \t\t%s" % (date))
            time_raw = soup_event.find('span', attrs={'class':'time'})
            m = re.search('\d+:\d+\s[AP]M', time_raw.text)
            time = m.group(0)
            #print("Time: \t\t%s" % (time))
            more_info_raw = soup_event.find('h4', attrs={'class':'animated'})
            more_info = more_info_raw.text.strip()
            #print("More info: \t%s" % (more_info))
            e = Event(event_name, date, time, more_info)
            e.set_id(event_id)
            e.set_link(event_link)
            event_list.append(e)
        return event_list
