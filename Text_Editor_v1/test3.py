from tkinter            import Button, Label, Menu, Text, Tk, Toplevel, END
from tkinter.filedialog import askopenfilename, asksaveasfilename


START = 1.0


def save_helper(textbox):
    filename = asksaveasfilename(filetypes = (("text file", "*.txt",),
                                                ("all files", "*.*")),
                                    defaultextension = ".txt",
                                    title = "Select a file to save to")
    if filename != "":      # if file selection is cancelled
        f = open(filename, 'w')
        f.write(textbox.get(START, END))
        f.close()
        print("file saved")

def open_helper(textbox):
    filename = askopenfilename(filetypes = (("text file", "*.txt",),
                                                ("all files", "*.*")),
                                    defaultextension = ".txt",
                                    title = "Select a file to open")
    if filename != "":      # if file selection is cancelled
        f = open(filename, 'r')
        text = f.read()
        textbox.delete(START, END)
        textbox.insert(START, text)
        f.close()

def main():
    root = Tk()
    root.title("ZACH_CHAD_EDITOR")

    label = Label(root, text = "here Zach")
    label.pack()

    textbox = Text(root, width = 80, height = 40, undo = True)
    textbox.pack()

    menubar = Menu(root)
    root["menu"] = menubar

    file_menu = Menu(menubar)
    menubar.add_cascade(label = "File", menu = file_menu)

    file_menu.add_command(label = "Save",
                            command = lambda: save_helper(textbox))

    file_menu.add_command(label = "Open",
                            command = lambda: open_helper(textbox))

    root.mainloop()


if __name__ == "__main__":
    main()
