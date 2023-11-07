import json

class FileManager:
    def __init__(self):
        self.people_dictionary = {}

    def add_person(self, first_name, middle_name, last_name):
        self.people_dictionary[last_name] = {}
        self.people_dictionary[last_name]["firstName"] = first_name
        self.people_dictionary[last_name]["middleName"] = middle_name
        self.people_dictionary[last_name]["lastName"] = last_name
        
        with open("people_list.json",mode="w") as f:
            f.write(json.dumps(self.people_dictionary))