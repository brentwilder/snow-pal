## Snow inspired palettes for your everyday plots (testing how to make packages..)

Snow-pal is a fast and easy-to-use color palette dictionary based on real life photos from great winter locations. Try snow-pal and create cool snow figures to share with your colleagues. Snow-pal is compatible with Python 2.7x and 3.4+. 

```
$ pip install snow-pal
```

<img src="https://github.com/brentwilder/snow-pal/blob/master/docs/pals_v2.jpg" width="1600">


### For example...
```python
# Import typical plotting libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import the pals
import snowpal
pal = snowpal.palettes('tetons-at-twilight')

# Generate some fake data and plot
data = np.array([1,2,3,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,7,7,7,8,9,10])
sns.boxplot(
    data=[data, data*1.2, data*1.7, data*2.1, data*2.6],
    palette=pal,
)
plt.show()
```
<img src="https://github.com/brentwilder/snow-pal/blob/master/docs/demo.png" width="600">
