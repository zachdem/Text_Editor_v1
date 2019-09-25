from tkinter                import Menu, Tk

from editor_settings        import EditorSettings
from settings_window        import SettingsWindow
from text_tab_controller    import TextTabController


DEFAULT_WINDOW_SIZE = "500x500"

def main():
    root = Tk()
    root.geometry(DEFAULT_WINDOW_SIZE)
    root.title("PAY_LOTS_OF_MONEY_AND_BUY_THIS_EDITOR")

    editor_settings = EditorSettings()
    tab_controller = TextTabController(root, editor_settings)

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
    file_menu.add_command(label = "Settings",
                            command = lambda: SettingsWindow(root, tab_controller, editor_settings))

    # Settings will be for all documents open not just the current textbox
    # What will be the interface for this? A new window pops up to display settings?
    # Need a spot to store current settings
    # Need a spot that manages diplaying window to configure settings
    # How do we change the font in a text box?
    # How do we change the color in a text box?
    # Text["font"] = ("Times New Roman", 12, "bold"))
    # from tkinter import font
    # font.families() to get list of available fonts
    # possible to highlight pieces
    # https://stackoverflow.com/questions/14786507/how-to-change-the-color-of-certain-words-in-the-tkinter-text-widget


    # add new style menu, with command to create settings window and display to user
    # settings window is a subclass of Toplevel, so it is a separate viewing area
    # provide checkboxes, radio buttons, sliders, dropdowns, etc for configurable settings
    # SettingsWindow class needs a reference to the tab controller so it can call the
    # appropriate methods to update the text tabs
    root.mainloop()


if __name__ == "__main__":
    main()
