from tkinter.ttk        import Notebook

from text_editor_tab    import TextEditorTab


class TextTabController(Notebook):

    FILETYPES = (("text file", "*.txt",), ("all files", "*.*"))
    TEXT_EXTENSION = ".txt"

    def __init__(self, root):
        super().__init__(root)
        self.enable_traversal()
        self.tabs = []

    def create_tab(self):
        temp_tab = TextEditorTab(self)
        self.tabs.append(temp_tab)
        self.add(temp_tab, text = 'Untitled')

    def delete_current_tab(self):
        current_tab_id = self.select()
        if current_tab_id != "":
            current_index = self.index(current_tab_id)
            self.forget(current_tab_id)
            self.tabs.pop(current_index)

    def save_current_tab(self):
        pass

    def open_to_current_tab(self):
        pass
