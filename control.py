import curses


def print_menu(stdscr, x, y, option, menu_options):
    menu_options = menu_options 
    menu_start_pos_y = y//2 - len(menu_options)//2
    
    for i, element in enumerate(menu_options):
        menu_start_pos_x = x//2 - len(element)//2
        menu_start_pos_y = menu_start_pos_y + 1

        if i == option:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(menu_start_pos_y, menu_start_pos_x, element)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(menu_start_pos_y, menu_start_pos_x, element)


def app(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    
    y = curses.LINES - 1
    x = curses.COLS - 1
    current_option = 0
    menu_options = ["CONFIG", "DATA MONITOR", "STATUS", "EXIT"]
    
    print_menu(stdscr, x, y, current_option, menu_options)
    
    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_option > 0:
            current_option = current_option - 1
        elif key == curses.KEY_DOWN and current_option < (len(menu_options)-1):
            current_option = current_option + 1
        elif key == curses.KEY_ENTER or key in (10, 13):
            if menu_options[current_option] == "CONFIG":
                stdscr.addstr("Not implemented")
            elif menu_options[current_option] == "DATA MONITOR":
                stdscr.addstr("Not implemented")
            elif menu_options[current_option] == "STATUS":
                stdscr.addstr("Not implemented")
            elif menu_options[current_option] == "EXIT":
                break

        print_menu(stdscr, x, y, current_option, menu_options)
        stdscr.refresh()


curses.wrapper(app)
