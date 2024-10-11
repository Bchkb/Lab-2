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

def most_popular_books(data, title):
    books = {}

    for line in data:
        string = get_object(line, title)
        download_value = int(string['Downloads'])
        book_name = string['Book-Title']
        books[book_name] = download_value
    
    popular_books = sorted(books.items(), key=lambda x: x[1])
    popular_books = popular_books[len(popular_books):len(popular_books)-21: -1]
    return popular_books

if __name__ == '__main__':
    with open(DATA_PATH) as data:
        title = get_title(data)
        line = next(data)
        res = most_popular_books(data, title)
        for i in range(len(res)):
            print(res[i][0])
        