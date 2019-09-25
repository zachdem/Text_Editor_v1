from pathlib            import Path
from tkinter            import BOTH
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk        import Notebook

from text_editor_tab    import TextEditorTab



class TextTabController(Notebook):

    FILETYPES = (("text file", "*.txt",), ("all files", "*.*"))
    TEXT_EXTENSION = ".txt"

    def __init__(self, root, editor_settings):
        super().__init__(root)
        self.editor_settings = editor_settings
        self.enable_traversal()

        self.tabs = []
        self.create_tab()   # start with an untitled tab

        self.pack(expand = True, fill = BOTH)


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
        #Grab the object of the current tab
        current_tab = self.get_current_text_editor_tab()
        #Prompt user to save file
        if current_tab is not None:
            filename = asksaveasfilename(filetypes = self.FILETYPES,
                                            defaultextension = self.TEXT_EXTENSION,
                                            title = "Select a file to save to")
            #Protect against empty file name
            if filename != "":
                with open(filename, 'w') as f:
                    f.write(current_tab.get_text())

    def open_to_current_tab(self):
        filename = askopenfilename(filetypes = self.FILETYPES,
                                        defaultextension = self.TEXT_EXTENSION,
                                        title = "Select a file to open")

        if filename != "":
            current_tab = self.get_current_text_editor_tab()
            if current_tab is None:
                self.create_tab()
                current_tab = self.get_current_text_editor_tab()

            with open(filename, 'r') as f:
                text = f.read()
                current_tab_id = self.select()
                self.tab(current_tab_id, text = Path(filename).name)
                current_tab.replace(text)

    def get_current_text_editor_tab(self):
        current_tab = None
        current_tab_id = self.select()
        if current_tab_id != "":
            current_index = self.index(current_tab_id)
            current_tab = self.tabs[current_index]

        return current_tab


    # methods to call text editor tab font changing methods for all tabs
