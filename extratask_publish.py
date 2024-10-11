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

def publisher_sort(data, title):
    publishers = []

    for line in data:
        string = get_object(line, title)
        publisher_value = string['Publisher']
        if publisher_value not in publishers:
            publishers.append(publisher_value)

    publishers.sort()
    data.seek(0)
    return publishers 



if __name__ == '__main__':
    with open(DATA_PATH) as data:
        title = get_title(data)
        line = next(data)
        res = publisher_sort(data, title)
        for i in range(len(res)):
            print(res[i])