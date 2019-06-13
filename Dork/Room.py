#Rooms will have an id number for the room.
#There will be a name for the room.
#There will be a description of that room.
#List of connected rooms.
#list of items in the room.
#list of NPCs in the room.
#Need a dictionary of neighbors.

import json

def get_room(id):
    ret = None
    with open(str(id) + ".json", "r") as F:
        jsontext = f.read()
        d = json.loads(jsontext) #open or create a text file "1.json".
        d['id'] = id # not sure what this does either.
        ret = Room(**d) # I don't know what this does.
    return ret

class Room():
    def __init__(self, id=0, name="A Room", description="An empty room", neighbors={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbors = neighbors

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
