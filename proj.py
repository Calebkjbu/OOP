from blessed import Terminal

term = Terminal()

menu_items = ['Start', 'Settings', 'About', 'Quit']

colors = {
    'Start': term.green,
    'Settings': term.yellow,
    'About': term.cyan,
    'Quit': term.red
}

def main():
    selected = 0

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.home + term.clear)

            # Calculate menu dimensions without color codes
            menu_height = len(menu_items)
            menu_width = max(len(item) for item in menu_items)  # length of text only

            # Center vertically and horizontally
            start_row = (term.height // 2) - (menu_height // 2)
            start_col = (term.width // 2) - (menu_width // 2)

            # Print menu items centered
            for i, item in enumerate(menu_items):
                text = item
                row = start_row + i
                col = start_col
                if i == selected:
                    # Reverse without affecting width calculation
                    print(term.move(row, col) + term.reverse(colors[item](text)))
                else:
                    print(term.move(row, col) + colors[item](text))

            val = term.inkey()

            if val.name == 'KEY_UP':
                selected = (selected - 1) % len(menu_items)
            elif val.name == 'KEY_DOWN':
                selected = (selected + 1) % len(menu_items)
            elif val.name == 'KEY_ENTER' or val == '\n':
                choice = menu_items[selected]
                if choice == 'Quit':
                    break
                elif choice == 'Start':
                    show_start_screen()
                else:
                    msg = f"You selected: {choice}. Press any key to return."
                    # Center message horizontally, put just below menu vertically
                    print(term.move(start_row + menu_height + 1, (term.width - len(msg)) // 2) + msg)
                    term.inkey()
            elif val.lower() == 'q':
                break

def show_start_screen():
    with term.fullscreen():
        print(term.home + term.clear)
        msg = "Welcome to the Start Screen! Press any key to go back."
        print(term.move(term.height // 2, (term.width - len(msg)) // 2) + term.bold_green(msg))
        term.inkey()

if __name__ == '__main__':
    main()
