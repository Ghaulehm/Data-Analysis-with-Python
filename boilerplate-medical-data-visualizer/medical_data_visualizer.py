import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from PIL.ImImagePlugin import number

# 1
df = pd.read_csv("medical_examination.csv")
# print(df.info())

# 2
df['overweight'] = (df['weight']/((df['height']/100)**2)) > 25
# print(df['overweight'])

# 3
df.loc[df['cholesterol']==1, 'cholesterol'] = 0
df.loc[df['cholesterol']!=0, 'cholesterol'] = 1
df.loc[df['gluc']==1, 'gluc'] = 0
df.loc[df['gluc']!=0, 'gluc'] = 1
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars= ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # print(df_cat)

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat.rename(columns={0: 'total'}, inplace=True)
    # print(df_cat)

    # 7
    chart = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col ='cardio', errorbar=None)


    # 8
    fig = chart.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) &
                     (df['height'] >= df['height'].quantile(0.025)) &
                     (df['height'] <= df['height'].quantile(0.975)) &
                     (df['weight'] >= df['weight'].quantile(0.025)) &
                     (df['weight'] <= df['weight'].quantile(0.975))]
    # print(df_heat)

    # 12
    corr = df_heat.corr()
    # print(corr.head())
    # print(corr.info())


    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # print(mask)

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, annot=True, fmt='.1f'.format(number) , xticklabels=True, yticklabels=True, mask=mask)

    # 16
    fig.savefig('heatmap.png')
    return fig
