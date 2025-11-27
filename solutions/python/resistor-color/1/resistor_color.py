def color_code(color):
    color_book = {
        'black'  : 0,
        'brown'  : 1,
        'red'    : 2,
        'orange' : 3,
        'yellow' : 4,
        'green'  : 5,
        'blue'   : 6,
        'violet' : 7,
        'grey'   : 8,
        'white'  : 9
    }
    return color_book.get(color,'Color Out of bound')

def colors():
    return ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
