import json

def save_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

#создаёт ячейки по кодовым словам
def start_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_human(data, human):
    data['humans'].append(human.back_to_file())

def delete_human(data, ID):
    data["humans"] = [human for human in data["humans"] if human['ID'] != ID]  

def add_reader(data, reader):
    data['readers'].append(reader.back_to_file())

def add_reader_1(data, reader):
    data['readers'].append(reader.back_to_file_1())

def delete_reader(data, ID):
    data["readers"] = [reader for reader in data["readers"] if reader['ID'] != ID]  

def add_school(data, school):
    data['schools'].append(school.back_to_file())

def add_school_1(data, school):
    data['schools'].append(school.back_to_file_1())

def delete_school(data, ID):
    data["schools"] = [school for school in data["schools"] if school['ID'] != ID]  