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

def delete_human(data, hu):
    data["humans"] = [human for human in data["humans"] if human['hu'] != hu]  

