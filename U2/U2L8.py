import pandas as pd
import numpy as np
df = pd.DataFrame(columns=['toBull','toBear','toStag'], data={'toBull':[.9,.15,.25], 'toBear':[.075,.8,.25], 'toStag':[.025,.05,.5]},
                  index=['frBull','frBear','frStag'])   #columns= to set col order, otherwise directly inputting data={} will cause col auto sort

print(df)
print(np.dot(df,df))
print(np.linalg.matrix_power(df,5))
print(np.linalg.matrix_power(df,100))

