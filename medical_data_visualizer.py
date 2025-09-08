import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = np.where(df['weight'] / np.square(df['height'] / 100) > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# 4
def draw_cat_plot():
    # 5 & 6
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 7
    fig = sns.catplot(x='variable', col='cardio', hue='value', kind='count', data=df_cat).set_axis_labels('variable', 'total').fig
    
    # 8
    fig.savefig('catplot.png')
    return fig

# 9
def draw_heat_map():
    # 10
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 11
    corr = df_heat.corr()

    # 12
    mask = np.triu(corr)

    # 13
    fig, ax = plt.subplots(figsize=(12, 12))

    # 14
    sns.heatmap(corr, linewidths=1, annot=True, square=True, mask=mask, fmt=".1f", center=0.08, cbar_kws={"shrink":0.5}, ax=ax)

    # 15
    fig.savefig('heatmap.png')
    return fig

# Call the functions to generate and save the plots
draw_cat_plot()
draw_heat_map()