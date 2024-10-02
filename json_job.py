import json

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

#создаёт ячейки по кодовым словам
def start_json(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'human': []}

def add_human(data, movie):
    data['human'].append(movie.to_dict())

def delete_movie(data, title):
    data['movies'] = [movie for movie in data['movies'] if movie['title'] != title]

