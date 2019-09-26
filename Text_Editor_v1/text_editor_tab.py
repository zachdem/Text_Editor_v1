from tkinter    import Frame, Text, BOTH, END
from tkinter.filedialog import askopenfilename, asksaveasfilename


class TextEditorTab(Frame):

    START = 1.0
    DEFAULT_HEIGHT = 40
    DEFAULT_WIDTH = 80

    def __init__(self, root):
        super().__init__(root)

        self.textbox = Text(self, undo = True)
        self.textbox.pack(expand = True, fill = BOTH)

    def get_text(self):
        return self.textbox.get(self.START, END)

    def replace(self, text):
        self.textbox.delete(self.START, END)
        self.textbox.insert(self.START, text)

    def update_font(self, font_tuple, font_color):
        self.textbox["font"] = font_tuple
        self.textbox["foreground"] = font_color
