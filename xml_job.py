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
    
    readers = ET.SubElement(root, 'readers')
    for reader in data['readers']:
        reader_element = ET.SubElement(readers, 'reader')
        for key, value in reader.items():
            child = ET.SubElement(reader_element, key)
            child.text = str(value)  

    schools = ET.SubElement(root, 'schools')
    for school in data['schools']:
        school_element = ET.SubElement(schools, 'schools')
        for key, value in school.items():
            child = ET.SubElement(school_element, key)
            child.text = str(value)  
    
    students = ET.SubElement(root, 'students')
    for student in data['students']:
        student_element = ET.SubElement(students, 'students')
        for key, value in student.items():
            child = ET.SubElement(student_element, key)
            child.text = str(value)  
    
    clubs = ET.SubElement(root, 'clubs')
    for club in data['clubs']:
        club_element = ET.SubElement(clubs, 'clubs')
        for key, value in club.items():
            child = ET.SubElement(club_element, key)
            child.text = str(value)  
    
    computers = ET.SubElement(root, 'computers')
    for computer in data['computers']:
        computer_element = ET.SubElement(computers, 'computer')
        for key, value in computer.items():
            child = ET.SubElement(computer_element, key)
            child.text = str(value) 

    gifts = ET.SubElement(root, 'gifts')
    for gift in data['gifts']:
        gift_element = ET.SubElement(gifts, 'gift')
        for key, value in gift.items():
            child = ET.SubElement(gift_element, key)
            child.text = str(value) 
    
    BOOKS = ET.SubElement(root, 'BOOKS')
    for BOOK in data['BOOKS']:
        BOOK_element = ET.SubElement(BOOKS, 'BOOK')
        for key, value in BOOK.items():
            child = ET.SubElement(BOOK_element, key)
            child.text = str(value) 

    indent(root)

    tree = ET.ElementTree(root)
    tree.write(file_name, encoding='utf-8', xml_declaration=True)

def start_xml(file_name):
    try:
        tree = ET.parse(file_name)
        root = tree.getroot()
    except FileNotFoundError:
        return {"humans": [], "readers": [], "schools": [], "student": [], "clubs": [], "computers": [], "gifts": [], "BOOKS": []}

    data = {"humans": [], "readers": [], "schools": [], "students": [], "clubs": [], "computers": [], "gifts": [], "BOOKS": []}

    humans = root.find('humans')
    if humans is not None:
        for human in humans:
            data_h = {}
            for elem in human:
                data_h[elem.tag] = elem.text
            data['humans'].append(data_h)

    readers = root.find('readers')
    if readers is not None:
        for reader in readers:
            data_r = {}
            for elem in reader:
                data_r[elem.tag] = elem.text
            data['readers'].append(data_r)

    schools = root.find('schools')
    if schools is not None:
        for school in schools:
            data_c = {}
            for elem in school:
                data_c[elem.tag] = elem.text
            data['schools'].append(data_c)
    
    students = root.find('students')
    if students is not None:
        for student in students:
            data_s = {}
            for elem in student:
                data_s[elem.tag] = elem.text
            data['students'].append(data_s)

    clubs = root.find('clubs')
    if clubs is not None:
        for club in clubs:
            data_m = {}
            for elem in club:
                data_m[elem.tag] = elem.text
            data['clubs'].append(data_m)

    computers = root.find('computers')
    if computers is not None:
        for computer in computers:
            data_H = {}
            for elem in computer:
                data_H[elem.tag] = elem.text
            data['computers'].append(data_H)  

    gifts = root.find('gifts')
    if gifts is not None:
        for gift in gifts:
            data_g = {}
            for elem in gift:
                data_g[elem.tag] = elem.text
            data['gifts'].append(data_g)   

    BOOKS = root.find('BOOKS')
    if BOOKS is not None:
        for BOOK in BOOKS:
            data_B = {}
            for elem in BOOK:
                data_B[elem.tag] = elem.text
            data['humans'].append(data_B)    

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

def add_reader(data, reader):
    data['readers'].append(reader.back_to_file())  
    save_to_xml(data, 'data.xml')  

def add_reader_1(data, reader):
    data['readers'].append(reader.back_to_file_1())  
    save_to_xml(data, 'data.xml')  

def delete_reader(data, re):
    upd = []
    for reader in data['readers']:
        if reader['ID'] != re:  
            upd.append(reader)
    
    data['readers'] = upd

def add_school(data, school):
    data['schools'].append(school.back_to_file())  
    save_to_xml(data, 'data.xml')  

def add_school_1(data, school):
    data['schools'].append(school.back_to_file_1())  
    save_to_xml(data, 'data.xml')  

def delete_school(data, sc):
    upd = []
    for school in data['schools']:
        if school['ID'] != sc:  
            upd.append(school)
    
    data['schools'] = upd

def add_student(data, student):
    data['students'].append(student.back_to_file())  
    save_to_xml(data, 'data.xml')  

def add_student_1(data, student):
    data['students'].append(student.back_to_file_1())  
    save_to_xml(data, 'data.xml')  

def delete_student(data, st):
    upd = []
    for student in data['students']:
        if student['ID'] != st:  
            upd.append(student)
    
    data['students'] = upd

def add_club(data, club):
    data['clubs'].append(club.back_to_file())  
    save_to_xml(data, 'data.xml')  

def delete_club(data, m):
    upd = []
    for club in data['clubs']:
        if club['ID'] != m:  
            upd.append(club)
    
    data['clubs'] = upd

def add_computer(data, computer):
    data['computers'].append(computer.back_to_file())  
    save_to_xml(data, 'data.xml')  

def delete_computer(data, ch):
    upd = []
    for computer in data['humans']:
        if computer['ID'] != ch:  
            upd.append(computer)
    
    data['computers'] = upd

def add_gift(data, gift):
    data['gifts'].append(gift.back_to_file())  
    save_to_xml(data, 'data.xml')  

def delete_gift(data, g):
    upd = []
    for gift in data['gifts']:
        if gift['ID'] != g:  
            upd.append(gift)
    
    data['gifts'] = upd

def add_BOOK(data, BOOK):
    data['BOOKS'].append(BOOK.back_to_file())  
    save_to_xml(data, 'data.xml')  
