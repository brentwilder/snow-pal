import seaborn as sns
import matplotlib.pyplot as plt

def palettes(palette_str):
    '''
    INPUT = palette_str

    Options include:

    'tetons-at-twilight'

    'sunny-drive'



    '''

    all_pals = {'tetons-at-twlight': ['#E19E6D','#C7EBFF', '#2C4436', '#D6D7FF', '#FFC8E5'], 
                'sunny-drive': ['#599BFF','#FFD400','#7C8485', '#2A5315', '#C6D1D8'], 
                }
    
    return all_pals[palette_str]


sns.palplot(['#599BFF','#FFD400','#7C8485', '#2A5315', '#C6D1D8'])
plt.show()