import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")
print(df.head())
df["overweight"] = df["weight"] / ((df["height"] / 100) ** 2)
df["overweight"] = df["overweight"].apply(lambda x: 1 if x > 25 else 0)
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)
def draw_cat_plot():
    df_cat_plt = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )
    df_cat_plt = (
        df_cat_plt.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    )
    plot = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        data=df_cat_plt,
        kind="bar",
        height=6,
        aspect=1,
    )
    fig = plot.figure  # Accessing the figure object from FacetGrid
    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    df_heat_map = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]
    corr = df_heat_map.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".1f",
        mask=mask,
        square=True,
        cbar_kws={"shrink": 0.5},
        linewidths=0.5,
        cmap="coolwarm",
        ax=ax,
    )
    fig.savefig("heatmap.png")
    return fig
