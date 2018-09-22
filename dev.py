import pandas as pd
import numpy as np
from sklearn import linear_model

sales = [{'x1':1, 'x2': 2, 'x3': 3, 'o': 6},
         {'x1': 2 ,  'x2': 3, 'x3': 4, 'o': 9},
         {'x1': 2, 'x2': 1, 'x3': 4, 'o': 7 },
        {'x1': 5, 'x2': 3, 'x3': 2, 'o': 10 },
        {'x1': 2, 'x2': 1, 'x3': 2, 'o': 5}
]

df = pd.DataFrame(sales)

reg = linear_model.LinearRegression()
reg.fit(df[['x1','x2','x3']],df.o)
prediction = reg.predict([[3, 4, 5]])[0]

