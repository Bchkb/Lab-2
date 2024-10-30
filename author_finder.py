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

def author_finder(data, title, author):
    find = []

    for line in data:
        string = get_object(line, title)
        author_value = string['Book-Author']
        year_value = string['Year-Of-Publication']
        if author_value == str(author) and int(year_value) >= 2018:
            if string['Book-Title'] not in find:
                find.append(string['Book-Title'])
    
    data.seek(0)
    return find


if __name__ == '__main__':
    with open(DATA_PATH) as data:
        title = get_title(data)
        line = next(data)
        author = input()
        res = author_finder(data, title, author)
        print(res)
        
        