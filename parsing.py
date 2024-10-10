from xml.dom.minidom import *

DATA_PATH = 'currency.xml'


def get_title(data):
    data.seek(0)
    title = next(data)
    title = title.split(';')
    title = [el.strip() for el in title]
    return title


def get_object(line, title):
    pass


if __name__ == '__main__':
    with parse(DATA_PATH, 'r') as file:
        data = file.read()
        print(data)