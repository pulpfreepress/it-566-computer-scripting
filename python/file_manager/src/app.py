from file_manager import FileManager


class App:
    def __init__(self):
        self.file_manager = FileManager()

    def add_person(self, first_name, middle_name, last_name):
        self.file_manager.add_person(first_name, middle_name, last_name)