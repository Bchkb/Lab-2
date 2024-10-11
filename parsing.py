from xml.dom.minidom import *

DATA_PATH = 'currency.xml'

def diction_maker():
    dictionary = {}
    charcodes = document.getElementsByTagName('CharCode')
    names = document.getElementsByTagName('Name')
    for i in range(len(charcodes)):
        name = names[i]
        charcode = charcodes[i]
        dictionary[name.firstChild.data] = charcode.firstChild.data
    return dictionary

if __name__ == '__main__':
    with parse(DATA_PATH) as document:
        print(diction_maker())