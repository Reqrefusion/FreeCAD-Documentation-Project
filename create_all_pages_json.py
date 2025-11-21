
'''
Fetches all pages from the FreeCAD wiki using the MediaWiki API.
https://www.mediawiki.org/wiki/API:Allpages
'''

from requests import get
from typing import TypedDict , Optional , List , Any
from time import sleep
from json import dump
from os import system , name


class Page ( TypedDict ):
    pageid : int
    title : str
    ns : int

class Query ( TypedDict ):
    allpages : List[ Page ]


Data = TypedDict('Data',{
    'continue' : Optional[ dict[ Any , Any ] ] ,
    'query' : Query
})


Server = 'https://wiki.freecad.org/api.php'
Output = 'all_pages.json'


pointer : None | dict[ Any , Any ] = {}
'''Optional pointer to the next pages'''

page_list : List[ Page ] = []


def clearConsole ():
    system('cls' if name == 'nt' else 'clear')


def writePages ( pages : List[ Page ] ):

    file = open(
        encoding = 'utf-8' ,
        file = Output ,
        mode = 'w'
    )

    with file :
        dump(
            ensure_ascii = False ,
            indent = 4 ,
            obj = pages ,
            fp = file
        )


def fetchPage () -> None | bool :

    global page_list , pointer

    clearConsole()

    print(f'Fetching pages ..',end = ' ')

    params = {
        ** ( pointer or {} ) ,
        'aplimit' : 'max' ,
        'action' : 'query' ,
        'format' : 'json' ,
        'list' : 'allpages'
    }

    response = get(Server,params)

    if not response.ok :
        print(f'❌')
        print(f'Status : { response.status_code }')
        print(f'Message : { response.text }')
        pass

    print(f'✅')

    data : Data = response.json()

    pages = data[ 'query' ][ 'allpages' ]

    print(f'Fetched pages : { len(page_list) } ( +{ len(pages) } )')

    page_list.extend(pages)

    pointer = data.get('continue')

    if pointer :
        print(f'Found more pages.')
        return True


def fetchAllPages ():

    while True :

        if fetchPage() :
            sleep(1)
            continue

        break



fetchAllPages()

writePages(page_list)

clearConsole()

print(f'Wrote { len(page_list) } pages to { Output }')
