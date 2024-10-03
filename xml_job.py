import xml.etree.ElementTree as ET

def indent(start, lenn = 0):
    i = "\n" + lenn * "  "
    if len(start):
        if not start.text or not start.text.strip():
            start.text = i + "  "
        if not start.tail or not start.tail.strip():
            start.tail = i
        for subelem in start:
            indent(subelem, lenn + 1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i
    else:
        if lenn and (not start.tail or not start.tail.strip()):
            start.tail = i

def save_to_xml(data, file_name):
    root = ET.Element('data')

    humans = ET.SubElement(root, 'humans')
    for human in data['humans']:
        human_element = ET.SubElement(humans, 'human')
        for key, value in human.items():
            child = ET.SubElement(human_element, key)
            child.text = str(value)  

    indent(root)

    tree = ET.ElementTree(root)
    tree.write(file_name, encoding='utf-8', xml_declaration=True)
    #убрать!
    print(f"Данные успешно сохранены в файл '{file_name}'")

def start_xml(file_name):
    try:
        tree = ET.parse(file_name)
        root = tree.getroot()
    except FileNotFoundError:
        return {"humans": []}

    data = {"humans": []}

    humans = root.find('humans')
    if humans is not None:
        for human in humans:
            data_h = {}
            for elem in human:
                data_h[elem.tag] = elem.text
            data['humans'].append(data_h)

    return data


def add_human(data, human):
    data['humans'].append(human.back_to_file())  
    save_to_xml(data, 'data.xml')  

def delete_human(data, hu):
    upd = []
    for human in data['humans']:
        if human['ID'] != hu:  
            upd.append(human)
    
    data['humans'] = upd