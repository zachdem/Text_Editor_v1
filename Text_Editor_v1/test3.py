from tkinter            import (Button, Frame, Label, Menu, Text, Tk, Toplevel,
                                BOTH, END)
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk        import Notebook


START = 1.0


def save_helper(textbox):
    filename = asksaveasfilename(filetypes = (("text file", "*.txt",),
                                                ("all files", "*.*")),
                                    defaultextension = ".txt",
                                    title = "Select a file to save to")
    if filename != "":      # if file selection is cancelled
        with open(filename, 'w') as f:
            f.write(textbox.get(START, END))
        print("file saved")

def open_helper(textbox):
    filename = askopenfilename(filetypes = (("text file", "*.txt",),
                                                ("all files", "*.*")),
                                    defaultextension = ".txt",
                                    title = "Select a file to open")
    if filename != "":      # if file selection is cancelled
        with open(filename, 'r') as f:
            text = f.read()
            textbox.delete(START, END)
            textbox.insert(START, text)
        print("file opened")

def main():
    # window setup
    root = Tk()
    root.title("ZACH_CHAD_EDITOR")

    menubar = Menu(root)
    root["menu"] = menubar

    file_menu = Menu(menubar)
    menubar.add_cascade(label = "File", menu = file_menu)

    file_menu.add_command(label = "Save",
                            command = lambda: save_helper(textbox1))

    file_menu.add_command(label = "Open",
                            command = lambda: open_helper(textbox1))


    # editor setup
    tab_control = Notebook(root)
    tab1 = Frame(tab_control)
    tab2 = Frame(tab_control)
    tab_control.add(tab1, text = 'Test_Tab 1')
    tab_control.add(tab2, text = "Test_Tab 2")

    textbox1 = Text(tab1, width = 80, height = 40, undo = True)
    textbox2 = Text(tab2, width = 80, height = 40, undo = True)

    tab_control.pack(expand = True, fill = BOTH)
    textbox1.pack(expand = True, fill = BOTH)
    textbox2.pack(expand = True, fill = BOTH)


    # start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()
