import pandas as pd
import numpy as np
import statistics as st

df = pd.read_csv('/Users/juanpablocarranza/Desktop/Analisis de Inversión/Binan e/Analisisvelas15mTodo.csv')


def mm(x,y):
    media = []
    for e in range(len(x)):
        m = 0
        if e<= y:
            m = round(df.loc[e,'close'],3)
        else:
            m2 = 0
            for i in range(y):
                m3 = df.loc[e-i,'close']
                m2 += m3
            m = round(m2/y,3)
        media.append(m)
    return media

# 57370.984500000006
# 57408.09299999999
# 57459.56799999999
# 57521.556

df['MediaMovil20'] = mm(df.index,20)

df.to_csv('/Users/juanpablocarranza/Desktop/Analisis de Inversión/Binan e/Velas15minyMM20.csv', index=True, header=True)