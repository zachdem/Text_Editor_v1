from tkinter                import Menu, Tk

from text_tab_controller    import TextTabController


def main():
    #Setup root TK
    root = Tk()
    root.title("BEST_FUCKING_EDITOR_OF_ALL_TIME")

    tab_controller = TextTabController(root)
    tab_controller.pack()

    menubar = Menu(root)
    root["menu"] = menubar

    file_menu = Menu(menubar)
    menubar.add_cascade(label = "File", menu = file_menu)

    file_menu.add_command(label = "New Tab",
                            command = tab_controller.create_tab)
    file_menu.add_command(label = "Delete Tab",
                            command = tab_controller.delete_current_tab)

    # file_menu.add_command(label = "Save",
    #                         command = )
    #
    # file_menu.add_command(label = "Open",
    #                         command = )
    root.mainloop()


if __name__ == "__main__":
    main()
