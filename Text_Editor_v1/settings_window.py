from tkinter                import (Button, Label, OptionMenu, Scale, StringVar,
                                    Toplevel, font, HORIZONTAL)
from tkinter.colorchooser   import askcolor


class SettingsWindow(Toplevel):

    MIN_FONT_SIZE = 5.0
    MAX_FONT_SIZE = 50.0
    DEFAULT_SETTINGS_WIDTH = int(MAX_FONT_SIZE * 10)
    DEFAULT_SETTINGS_HEIGHT = 250

    def __init__(self, root, tab_controller, editor_settings):
        super().__init__(root)
        self.geometry("{}x{}".format(self.DEFAULT_SETTINGS_WIDTH, self.DEFAULT_SETTINGS_HEIGHT))
        self.title("Settings")
        self.tab_controller = tab_controller

        self.editor_settings = editor_settings

        self.create_font_family_chooser(self.editor_settings.font_family)
        self.create_color_picker_button(self.editor_settings.font_color)
        self.create_font_size_chooser(self.editor_settings.font_size)
        self.create_preview_label(self.editor_settings.font_family, self.editor_settings.font_color, self.editor_settings.font_size)
        self.create_confirm_button()

    def create_font_family_chooser(self, current_font):
        self.font_input_capture = StringVar(self)
        self.font_input_capture.set(current_font)
        OptionMenu(self, self.font_input_capture, *font.families(), command = lambda new_family: self.update_preview_label(family = new_family)).pack()

    def create_color_picker_button(self, current_color):
        self.color_input_capture = current_color
        Button(self, command = lambda: self.choose_color(current_color), text = "Choose Color").pack()

    def choose_color(self, current_color):
        self.color_input_capture = askcolor(parent = self, initialcolor = current_color)
        if self.color_input_capture is None:
            self.color_input_capture = current_color
        else:
            self.color_input_capture = self.color_input_capture[1]
        self.update_preview_label(color = self.color_input_capture)

    def create_font_size_chooser(self, current_size):
        self.font_size_scale = Scale(self, from_ = self.MIN_FONT_SIZE, to = self.MAX_FONT_SIZE, orient = HORIZONTAL, command = lambda new_size: self.update_preview_label(size = new_size))
        self.font_size_scale.set(current_size)
        self.font_size_scale.pack()

    def create_preview_label(self, current_font, current_color, current_size):
        self.preview_label = Label(self, text = "Zack is Wack", background = "#FFFFFF")
        self.update_preview_label(family = current_font, color = current_color, size = current_size)
        self.preview_label.pack()

    def update_preview_label(self, family = None, color = None, size = None):
        if family is None:
            family = self.font_input_capture.get()
        if color is None:
            color = self.color_input_capture
        if size is None:
            size = self.font_size_scale.get()

        self.preview_label["font"] = (family, size)
        self.preview_label["foreground"] = color

    def create_confirm_button(self):
        Button(self, text = "Confirm", command = self.confirm).pack()
        Button(self, text = "Cancel", command = self.destroy).pack()

    def confirm(self):
        self.editor_settings.font_family = self.font_input_capture.get()
        self.editor_settings.font_color = self.color_input_capture
        self.editor_settings.font_size = self.font_size_scale.get()
        self.tab_controller.update_text_tab_fonts(self.editor_settings)
        self.destroy()
