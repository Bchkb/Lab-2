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

def biblio_list(data, line, title):
    biblio = []

    for line in data:
        string = get_object(line, title)
        author = string['Book-Author']
        name = string['Book-Title']
        year = string['Year-Of-Publication']
        if len(biblio) <= 20:
            biblio.append(f'{author}. {name} - {year}')
    
    return biblio


if __name__ == '__main__':
    with open(DATA_PATH) as data:
        title = get_title(data)
        line = next(data)
        res = biblio_list(data, line, title)

    with open('Biblio_list', 'w+') as file_biblio_list:
        for i in range(1, 21):
            file_biblio_list.write(f'{i}. {res[i]}\n')


        