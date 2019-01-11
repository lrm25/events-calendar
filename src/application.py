from venue_manager import *

from storage import db

#
# main function
#
def main():
    event_list = get_events()
    for event in event_list:
        print("Name:  %s, Date:  %s, Time:  %s, More info:  %s" %
              (event.get_name(), event.get_date(), event.get_show_time(),
               event.get_info()))
        print("Event ID:  %s" % (event.get_id()))
        db.get_event_table().add_entry(event.get_id(), event.get_name(),
            event.get_show_time(), event.get_link(), event.get_info())

if __name__ == "__main__":
    main()
