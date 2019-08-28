from tkinter    import Frame, Text, BOTH, END
from tkinter.filedialog import askopenfilename, asksaveasfilename


class TextEditorTab(Frame):

    START = 1.0
    DEFAULT_HEIGHT = 40
    DEFAULT_WIDTH = 80

    def __init__(self, root):
        super().__init__(root)

        self.textbox = Text(self,
                            width = self.DEFAULT_WIDTH,
                            height = self.DEFAULT_HEIGHT,
                            undo = True)
        self.textbox.pack()

    def get_text(self):
        self.textbox.get(self.START, END)

    def replace(self, text):
        self.textbox.delete(self.START, END)
        self.textbox.insert(self.START, text)
