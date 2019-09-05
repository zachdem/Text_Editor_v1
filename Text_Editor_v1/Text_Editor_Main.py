from tkinter                import Menu, Tk

from text_tab_controller    import TextTabController


DEFAULT_WINDOW_SIZE = "500x500"

def main():
    #Setup root TK
    root = Tk()
    root.geometry(DEFAULT_WINDOW_SIZE)
    root.title("PAY_LOTS_OF_MONEY_AND_BUY_THIS_EDITOR")

    tab_controller = TextTabController(root)

    menubar = Menu(root)
    root["menu"] = menubar

    file_menu = Menu(menubar)
    menubar.add_cascade(label = "File", menu = file_menu)

    file_menu.add_command(label = "New Tab",
                            command = tab_controller.create_tab)
    file_menu.add_command(label = "Delete Tab",
                            command = tab_controller.delete_current_tab)
    file_menu.add_command(label = "Save",
                            command = tab_controller.save_current_tab)
    file_menu.add_command(label = "Open",
                            command = tab_controller.open_to_current_tab)
    root.mainloop()


if __name__ == "__main__":
    main()
