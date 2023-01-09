
def palettes(palette_str, reverse=False):
    '''
    INPUT = palette_str

    Options include: 'tetons-at-twilight', 'sunny-drive', 'construction', 'foggy-ldp', 'dusty1', 'snow-school',
    'isothermal', 'greenbelt', 'bogus-blue', 'wildcats', 'xyz', 'ponderosa1'

    Optional argument is reverse (Bool). User can select if they would like to reverse the palatte. Default is False.

    '''

    all_pals = {'tetons-at-twilight': ['#404563','#4f3632','#a67f7a','#9ea7d0', '#e3c0d8'], 
                'sunny-drive': ['#599BFF','#FFD400','#7C8485', '#2A5315', '#C6D1D8'], 
                'construction': ['#9cb96b','#916573','#9d989f','#5c5d5d','#15161a'], 
                'foggy-ldp': ['#5c6c69','#858485','#85735c','#845042','#494038'], 
                'dusty1': ['#d2dadd', '#aba7a4','#a59189','#736e60', '#403d37'], 
                'snow-school': ['#065ead','#ee8330','#986166', '#383845','#d7b329'], 
                'isothermal': ['#358fdb','#6b8c9d','#93a8be','#cad3db','#626663'],  
                'greenbelt': ['#efd2be','#ac966d','#5f4526','#939391','#14191c'], 
                'bogus-blue': ['#214872','#1a78c7','#6284a2','#8ea9c0','#d3d0c0'],
                'wildcats': ['#d6a316','#945c14','#07568f','#7396b0','#2d3039'],
                'xyz': ['#8fa694','#354f46','#385167','#657376','#a3abad'],
                'ponderosa1': ['#beb94d','#828155','#4f581d','#30401c','#272b1c'],                  
                }

    try:
        all_pals[palette_str]
    except:
        print('Must be either "tetons-at-twilight", "sunny-drive", "construction", "foggy-ldp", "dusty1","snow-school", "isothermal", "greenbelt", "bogus-blue", "wildcats", "xyz", "ponderosa1"')

    
    pal = all_pals[palette_str]

    if reverse is True:
        pal.reverse()

    return pal