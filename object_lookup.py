import xlwings as xw
from xlwings import constants, Range

app = xw.apps
wb = app.active.books.active
rng = Range('B2:B21')

obj = {'2476' : 'North Consortium',
        '2877' : 'Correction Tape',
        '2592' : 'Guayaba Fields',
        '2695' : 'Guayaba Consortium',
        '2441' : 'Family Place',
        '2117' : 'Family Homes'}


for x in rng:
    if str(x.value).strip() in obj.keys():
        x.offset(0, 1).value = 'Categorized'
        x.offset(0, 2).value = obj[str(x.value).strip()]
    else:
        x.offset(0, 1).value = 'Uncategorized'
        x.offset(0, 2).value = ''
 
 

