#Rooms will have an id number for the room.
#There will be a name for the room.
#There will be a description of that room.
#List of connected rooms.
#list of items in the room.
#list of NPCs in the room.
#Need a dictionary of neighbors.

import json
import sqlite3

def get_room(id, dbfile):
    ret = None

    con = sqlite3.connect("dbfile")

    for row in con.execute("select json from rooms where id = ?", (id,)):

        jsontext = row[0]
        d = json.loads(jsontext) # Loads dictionary.
        d['id'] = id # #open or create a text file "1.json".
        ret = Room(**d) # I don't know what this does.
        break

    con.close()

    return ret

class Room():
    def __init__(self, id=0, name="A Room", description="An empty room", neighbors={}):
        self.id = id # room will have an id number.
        self.name = name # name of the room.
        self.description = description # description of the room.
        self.neighbors = neighbors # dictionary of neighbors.

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return: None

    def north(self):
        return self._neighbor('n')

    def south(self):
        return self._neighbor('s')

    def east(self):
        return self._neighbor('e')

    def west(self):
        return self._neighbor('w')
