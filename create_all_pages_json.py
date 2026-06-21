class Query ( TypedDict ):
    allpages : List[ Page ]

class Data ( TypedDict ):
    continue : Optional[ dict[ Any , Any ] ]
    query : Query

Server = 'https://wiki.freecad.org/api.php'
Output = 'all_macros.json'
Namespace = '102'  # Macro namespace

pointer : None | dict[ Any , Any ] = {}
'''Optional pointer to the next pages'''

page_list : List[ Page ] = []

def clearConsole ():
    system('cls' if name == 'nt' else 'clear')

def writePages ( pages : List[ Page ] ):
    with open(Output,'w',encoding='utf-8') as f:
        dump(pages,f,ensure_ascii=False,indent=4)

def getPages ():
    global pointer
    params = {
        'action' : 'query',
        'format' : 'json',
        'list' : 'allpages',
        'apnamespace' : Namespace,
        'aplimit' : '500'
    }
    if pointer:
        params.update(pointer)
    response = get(Server,params=params)
    data : Data = response.json()
    page_list.extend(data['query']['allpages'])
    pointer = data.get('continue',None)
    return pointer is not None