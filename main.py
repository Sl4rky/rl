#!usr/bin/env python3

import curses
from curses import wrapper


def main(stdscr):
    height, width = stdscr.getmaxyx()
    player_y = height//2
    player_x = width//2

    curses.noecho()
    curses.curs_set(0)

    while True:
        stdscr.clear()
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
