import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("medical_examination.csv", header=0)

df["bmi"] = df["weight"] / ((df["height"] / 100) ** 2)
df["overweight"] = None
df.loc[df["bmi"] > 25, "overweight"] = 0
df.loc[df["bmi"] <= 25, "overweight"] = 1
df = df.drop(columns=["bmi"])

df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1


def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    fig = sns.catplot(data = df_cat, kind='count',  x='variable', hue='value', col='cardio').set(ylabel = 'total').fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    def draw_heat_map():
        df_heat = df[ 
            ( df['ap_lo'] <= df['ap_hi'] ) & 
            ( df['height'] >= df['height'].quantile(0.025) ) & 
            ( df['height'] <= df['height'].quantile(0.975) ) & 
            ( df['weight'] >= df['weight'].quantile(0.025) ) & 
            ( df['weight'] <= df['weight'].quantile(0.975) ) 
        ]

        corr = df_heat.corr()

        mask = np.triu(corr)


        fig, ax =  plt.subplots()
        
        ax = sns.heatmap(corr, mask=mask, annot=True, fmt='0.1f', square=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
