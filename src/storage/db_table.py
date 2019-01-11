from storage import db

class DbTable():

    def __init__(self, create_query):
        self._created = False
        self._create_query = create_query

    def create(self):
        if self._created is False:
            conn = db.connect()
            # TODO - exception
            conn.execute(self._create_query)
            conn.close()
            self._created = True
