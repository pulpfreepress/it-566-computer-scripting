from app import App

class UI:
    def __init__(self):
        self.app = App()

    def _print_menu(self):
        print("\t\tPeople List Application")
        print("\n")
        print("\t1. Add New Person")
        print("\t2. List People")
        print("\t3. Delete Person")
        print("\t4. Exit")
        print("\n")

    def _process_menu_choice(self):
        user_input = input("Enter Menu Choice: ")

        match(user_input[0]):
            case "1": self.add_person()
            case "2": self.list_people()
            case "3": self.delete_person()
            case "4": quit()
            case _: print("Invalid menu choice!")

    def start_ui(self):
        while True:
            self._print_menu()
            self._process_menu_choice()


    def add_person(self):
        first_name = input("First Name: ")
        middle_name = input("Middle Name: ")
        last_name = input("Last Name: ")
        self.app.add_person(first_name=first_name, middle_name=middle_name, \
                            last_name=last_name)


    def list_people(self):
        print("list_people() method called...")

    def delete_person(self):
        print("delete_person() method called...")

