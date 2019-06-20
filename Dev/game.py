#What's Missing?
# -Status bar - curses module is the key?
# -Npc's
# -Puzzles
# -"Advanced" text parsing
import cmd
from yaml import load, dump
from Dev.Room import get_room
import textwrap
import shutil
import tempfile
import sys
import os
import time
import random

screen_width = 100


class Game(cmd.Cmd): # This is a functional cmd prompt that sub classes Cmd
    def __init__(self):
        cmd.Cmd.__init__(self)

        self.dbfile = tempfile.mktemp()
        # shutil.copyfile("game.db", self.dbfile)

        self.loc = get_room(1, self.dbfile)
        # self.look()
    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper
    
    with open('Dev/1.yaml') as stream:
        data = load(stream, Loader = Loader)

    output = dump(data, Dumper = Dumper)

    #### Title Screen ####

    def title_screen_selections(self):
        option = input("> ")
        if option.lower() == ("play"):
            pass
            # start_game() # placeholder until written
        elif option.lower() == ("help"):
            self.help_menu()
        elif option.lower() == ("quit"):
            self.do_quit()
        while option.lower() not in ['play', 'help', 'quit']:
            print("Please enter a valid command")
            option = input("> ")
            if option.lower() == ("play"):
                pass
                # start_game() # placeholder until written
            elif option.lower() == ("help"):
                self.help_menu()
            elif option.lower() == ("quit"):
                self.do_quit()

    def title_screen(self):
        os.system('clear')
        print('##############################')
        print(' # Welcome to the Game! # ')
        print('         - Play -         ')
        print('         - Help -         ')
        print('  Copyright 2019 dcdegmd  ')
        # title_screen_selections()

    def help_menu(self):
        print('##############################')
        print(' # Help Menu:                         ')
        print(' - Use up, down, left, right to move. ')
        print(' - Type your commands to do them.     ')
        print(' - Use "look" to inspect something.   ')
        print(' - Good luck and have fun!            ')
        # title_screen_selections
        
    #### End Title Screen ####
    
    def move(self, dir):
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print("you can't go that way")
        else:
            self.loc = get_room(newroom, self.dbfile)
            self.look()

        if newroom == 13:
            exit()

    def look(self):
        print(self.loc.name)
        print("")
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    def do_up(self, args):
        """Go up"""
        self.move('up')

    def do_down(self,args):
        """Go down"""
        self.move('down')

    def do_left(self,args):
        """Go left"""
        self.move('left')

    def do_right(self,args):
        """Go right"""
        self.move('right')

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
    def do_quit(self): # "do" is a Command for cmd prompt.
        """Leaves the game""" # help for the method. Prints that it left the game.
        print("Thank you for playing")
        return True

    def do_save(self):
        """Saves the game"""
        # shutil.copyfile(self.dbfile, args)
        # print("the game was saved to {0}".format(args))
