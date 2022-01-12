#!usr/bin/env python3
"""main file for a basic python roguelike"""

import curses
from curses import wrapper


def generate_room(width: int, height: int) -> list:
    """Generate a rectangular room with given width and height"""
    room = []

    for i in range(height):
        string = ""
        for j in range(width):
            if i in (0, width - 1):
                string += "-"
            else:
                if j in (0, width - 1):
                    string += "|"
                else:
                    string += "."
        room.append(string)
    return room


def main(stdscr):
    """main function"""

    height, width = stdscr.getmaxyx()
    player_y = height//2
    player_x = width//2

    curses.noecho()
    curses.curs_set(0)

    while True:
        stdscr.clear()
        new_room = generate_room(10, 10)
        for i, level in enumerate(new_room):
            stdscr.addstr(i + 1, 1, level)
        stdscr.addstr(player_y, player_x, "@")
        stdscr.refresh()

        char = stdscr.getch()
        if char == curses.KEY_RIGHT:
            player_x += 1
        elif char == curses.KEY_LEFT:
            player_x -= 1
        elif char == curses.KEY_UP:
            player_y -= 1
        elif char == curses.KEY_DOWN:
            player_y += 1


if __name__ == '__main__':
    wrapper(main)
