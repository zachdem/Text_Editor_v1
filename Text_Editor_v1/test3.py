from tkinter            import Button, Label, Text, Tk, Toplevel, END
from tkinter.filedialog import asksaveasfilename


def save_helper(textbox):
    filename = asksaveasfilename(defaultextension = "txt")
    with open(filename, 'w') as f:
        f.write(textbox.get(1.0, END))
    print("file saved")

def main():
    root = Tk()
    root.title("ZACH_CHAD_EDITOR")

    side_window = Toplevel(root)

    label = Label(root, text = "here Zach")
    label.pack()

    textbox = Text(root, width = 80, height = 40)
    textbox.pack()

    button = Button(root,
                    text = "save",
                    command = lambda: save_helper(textbox)
                    )
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
