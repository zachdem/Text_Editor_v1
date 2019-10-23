from tkinter                import Menu, Tk

from editor_settings        import EditorSettings
from settings_window        import SettingsWindow
from text_tab_controller    import TextTabController


DEFAULT_WINDOW_SIZE = "500x500"

def main():
    root = Tk()
    root.geometry(DEFAULT_WINDOW_SIZE)
    root.title("The New Notepad, TM")

    editor_settings = EditorSettings()
    tab_controller = TextTabController(root, editor_settings)

    menubar = Menu(root)
    root["menu"] = menubar

    file_menu = Menu(menubar)
    menubar.add_cascade(label = "File", menu = file_menu)

    file_menu.add_command(label = "New Tab",
                            command = lambda: tab_controller.create_tab(editor_settings))
    file_menu.add_command(label = "Delete Tab",
                            command = tab_controller.delete_current_tab)
    file_menu.add_command(label = "Save",
                            command = tab_controller.save_current_tab)
    file_menu.add_command(label = "Open",
                            command = tab_controller.open_to_current_tab)
    file_menu.add_command(label = "Settings",
                            command = lambda: SettingsWindow(root, tab_controller, editor_settings))

    root.mainloop()


if __name__ == "__main__":
    main()
