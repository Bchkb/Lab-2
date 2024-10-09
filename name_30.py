import csv

DATA_PATH = 'books-en.csv'


def get_title(data):
    data.seek(0)
    title = next(data)
    title = title.split(';')
    title = [el.strip() for el in title]
    return title


def get_object(line, title):
    read = csv.DictReader([line], title, delimiter=';')
    res = next(read)
    return res

def symbol_count(data, title, length):
    count = 0
    for line in data:
        name = get_object(line, title)
        name_value = name['Book-Title']
        if len(name_value) > length:
            count += 1
    
    data.seek(0)
    return count



if __name__ == '__main__':
    with open(DATA_PATH) as data:
        title = get_title(data)
        line = next(data)
        print(symbol_count(data, title, 30))
        