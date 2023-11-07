

class UI:
    def __init__(self):
        #print("__init__() method called...")
        pass

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
        print("add_person() method called...")

    def list_people(self):
        print("list_people() method called...")

    def delete_person(self):
        print("delete_person() method called...")

