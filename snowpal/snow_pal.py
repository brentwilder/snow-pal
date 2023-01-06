
def palettes(palette_str):
    '''
    INPUT = palette_str

    Options include: 'tetons-at-twilight', 'sunny-drive', 'construction', 'foggy-ldp', 'dusty1', 'snow-school',
    'isothermal'



    '''

    all_pals = {'tetons-at-twilight': ['#4f3632','#a67f7a', '#404563', '#9ea7d0', '#e3c0d8'], 
                'sunny-drive': ['#599BFF','#FFD400','#7C8485', '#2A5315', '#C6D1D8'], 
                'construction': ['#9cb96b','#5c5d5d','#15161a', '#9d989f', '#916573'], 
                'foggy-ldp': ['#5c6c69','#858485','#85735c','#494038', '#845042'], 
                'dusty1': ['#d2dadd', '#aba7a4','#a59189','#736e60', '#403d37'], 
                'snow-school': ['#065ead','#ee8330','#986166', '#383845','#d7b329'], 
                'isothermal': ['#358fdb','#93a8be','#cad3db','#6b8c9d','#626663'],  
                }

    try:
        all_pals[palette_str]
    except:
        print('Must be either "tetons-at-twilight", "sunny-drive", "construction", "foggy-ldp", "dusty1",\
               "snow-school", "isothermal"')

    return all_pals[palette_str]