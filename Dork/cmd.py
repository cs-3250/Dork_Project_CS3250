import cmd
from room import get_room

class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        self.loc = get_room(1)
        self.look()

    def move(self, dir):
        newroom = self.loc._neighbors(dir)
        if newroom is None:
            print("you can't go that way")
        else:
            self.loc = get_room(newroom)
            self.look()

    def look(self)
        print(self.loc.name)
        print("")
        print(self.loc.description)

    def do_n(self, args):
        """Go North"""
        self.move('n')

    def do_s(self, args):
        """Go South"""
        self.move('s')

    def do_e(self, args):
        """Go East"""
        self.move('e')

    def do_w(self, args):
        """Go West"""
        self.move('w')
    
    # Want to be able to exit game.
    def do_quit(self, args):
        """Leaves the game"""
        print("Thank you for playing")
        return True

if __name__ == "__main__":
    g = Game()
    g.cmdloop()