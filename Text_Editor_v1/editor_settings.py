

class EditorSettings:

    DEFAULT_COLOR = "#000000"
    DEFAULT_SIZE = 12
    DEFAULT_FAMILY = "Times New Roman"

    def __init__(self):
        self.font_color = self.DEFAULT_COLOR
        self.font_size = self.DEFAULT_SIZE
        self.font_family = self.DEFAULT_FAMILY
        # maybe style later

    def get_font_tuple(self):
        return (self.font_family, self.font_size)
